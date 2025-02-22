# -*- coding: utf-8 -*-
#
# This file is part of BGPhoria.
#
# Copyright (C) 2025 Interstellio IO (PTY) LTD.
#
# BGPhoria is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or any later version.
#
# BGPhoria is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with BGPhoria. If not, see https://www.gnu.org/licenses/.
#
import socket
import struct
import ipaddress

from bgphoria.constants import (AFI,
                                SAFI,
                                BGP_HEADER_MARKER,
                                MESSAGE_TYPE)
from bgphoria.exceptions import BGPInvalidMessage


async def read_message(conn):
    """
    INTERNAL USE ONLY, Reads a BGP message header and payload from a socket.

    **Important**: This is an internal function intended for use within the
    package. External users should avoid relying on it as part of the public
    API because its implementation or API may change in future versions
    without notice.

    This function reads the BGP message header from a given socket, extracts
    the message length, message type, and the payload (data following the
    message type). It ensures the entire header (19 bytes) is read first,
    validates the message header for correctness, then reads the remaining
    payload based on the specified length.

    Parameters:
        socket (socket.socket): The socket object to read the BGP message from.
            The socket should already be connected and ready for reading.

    Returns:
        tuple: A tuple containing:
            - int: The total length of the BGP message, including the header.
            - int: The BGP message type.
            - bytes: The payload (data following the message type).

    Raises:
        ConnectionError: If the connection is closed before receiving enough
            data for the header or the complete message.
        struct.error: If the header format is invalid and cannot be unpacked.
        InvalidMessage: If the BGP message header is corrupt or reports an
            invalid size.

    Example:
        # Read a BGP message from a socket
        message_length, message_type, payload = read_message(my_socket)

    Notes:
        - The function expects the socket to operate in blocking mode.
        - It assumes the BGP message header is exactly 19 bytes long, per the
          BGP protocol specification.
        - The `readall` function ensures that the specified number of bytes is
          reliably read from the socket.
    """
    # Read the fixed-size BGP header (19 bytes)
    buffer = await conn.read(19)

    try:
        # Unpack the BGP header:
        #   marker (16 bytes), length (2 bytes), type (1 byte)
        _, length, message_type = struct.unpack('!16sHB', buffer)
    except struct.error as e:
        raise BGPInvalidMessage(f"Failed to unpack BGP message header: {e}")

    # Validate the length reported in the header
    if length < 19 or length > 4096:  # 19 is the minimum; 4096 is the maximum.
        raise BGPInvalidMessage(f"Invalid message length: {length}")

    # Read the payload based on the reported length
    payload = await conn.read(length - 19)

    return length, message_type, payload


def parse_notification(payload):
    error_code = payload[0]
    error_subcode = payload[1]
    data = payload[2:]
    return error_code, error_subcode, data


# BGP Open Message
def create_open_message(as_number, hold_time, bgp_identifier,
                        ipv4_unicast=True, ipv6_unicast=False,
                        ipv4_unicast_add_path=None,
                        ipv6_unicast_add_path=None):
    """
    INTERNAL USE ONLY, Constructs a BGP Open message.

    **Important**: This is an internal function intended for use within the
    package. External users should avoid relying on it as part of the public
    API because its implementation or API may change in future versions
    without notice.

    Args:
        as_number (int): The local Autonomous System (AS) number.
        hold_time (int): The hold time (in seconds) advertised by the sender.
        bgp_identifier (str): The BGP Identifier (IPv4 address format) of
            the sender.
        ipv4_unicast (bool, optional): If True, includes the IPv4 Unicast
            capability in the optional parameters. Defaults to True.
        ipv6_unicast (bool, optional): If True, includes the IPv6 Unicast
            capability in the optional parameters. Defaults to False.
        ipv4_unicast_add_path (int, optional): If provided, includes the
            Add-Path capability for IPv4 Unicast. The value indicates the
            Send/Receive mode:
            - None: Disabled.
            - 1: Send-only.
            - 2: Receive-only.
            - 3: Send and receive.
            Defaults to None (Add-Path not advertised).
        ipv6_unicast_add_path (int, optional): If provided, includes the
            Add-Path capability for IPv6 Unicast. The value indicates the
            Send/Receive mode (same as above). Defaults to None (Add-Path
            not advertised).

    Returns:
        bytes: A binary-encoded BGP Open message ready to be sent over
        the connected socket.

    Raises:
        ValueError: If `bgp_identifier` is not a valid IPv4 address.
        struct.error: If there are issues packing the binary data.

    Notes:
        - 4-byte AS number support is defined in RFC 6793.
        - The Multiprotocol Extensions capability is defined in RFC 4760.
        - The Add-Path capability is defined in RFC 7911.
    """
    if ipv4_unicast_add_path:
        ipv4_unicast_add_path = ipv4_unicast_add_path.value

    if ipv6_unicast_add_path:
        ipv6_unicast_add_path = ipv6_unicast_add_path.value

    as_number_2bytes = as_number if as_number <= 65535 else 23456
    # Use AS_TRANS for 4-byte AS numbers
    optional_params = b''

    # Add support for 4-byte AS numbers capabilities parameters
    if as_number > 65535:
        four_byte_as_capability = struct.pack(
            '!BBBBL',
            2,   # Capability parameter type.
            6,   # Length: 2 (header) + 4 (value)
            65,  # Capability Code: 4-byte AS
            4,   # Capability Length
            as_number
        )
        optional_params += four_byte_as_capability

    if ipv4_unicast:
        # Add IPv4 Unicast Capability
        ipv4_unicast_capability = struct.pack(
            '!BBBBHBB',
            2,  # Capability parameter type.
            6,  # Total length of this parameter (6 bytes).
            1,  # Capability Code: Multiprotocol Extension
            4,  # Capability Length
            1,  # AFI: Address Family Identifier (IPv4).
            0,  # Reserved (must be set to 0).
            1   # SAFI: Subsequent Address Family Identifier (Unicast).
        )
        optional_params += ipv4_unicast_capability

        if ipv4_unicast_add_path is not None:
            # Add IPv4 Unicast Add-Path Capability
            ipv4_unicast_add_path_capability = struct.pack(
                '!BBBBHBB',
                2,   # Capability parameter type.
                6,   # Total length of this parameter (6 bytes).
                69,  # Capability Code: Add-Path Extension
                4,   # Capability Length
                1,   # AFI: Address Family Identifier (IPv4).
                1,   # SAFI: Subsequent Address Family Identifier (Unicast).
                ipv4_unicast_add_path
            )
            optional_params += ipv4_unicast_add_path_capability

    if ipv6_unicast:
        # Add IPv6 Unicast Capability
        ipv6_unicast_capability = struct.pack(
            '!BBBBHBB',
            2,  # Capability parameter type.
            6,  # Total length of this parameter (6 bytes).
            1,  # Capability Code: Multiprotocol Extension
            4,  # Capability Length
            2,  # AFI: Address Family Identifier (IPv6).
            0,  # Reserved (must be set to 0).
            1   # SAFI: Subsequent Address Family Identifier (Unicast).
        )
        optional_params += ipv6_unicast_capability

        if ipv6_unicast_add_path is not None:
            # Add IPv6 Unicast Add-Path Capability
            ipv6_unicast_add_path_capability = struct.pack(
                '!BBBBHBB',
                2,   # Capability parameter type.
                6,   # Total length of this parameter (6 bytes).
                69,  # Capability Code: Add-Path Extension
                4,   # Capability Length
                2,   # AFI: Address Family Identifier (IPv6).
                1,   # SAFI: Subsequent Address Family Identifier (Unicast).
                ipv6_unicast_add_path
            )
            optional_params += ipv6_unicast_add_path_capability

    # Calculate the total length of optional parameters
    optional_params_length = len(optional_params)

    # Assemble the BGP Open message
    open_message = struct.pack(
        '!16sHBBHH4sB',
        BGP_HEADER_MARKER,
        29 + optional_params_length,  # Length of Open message
                                      # including optional parameters
        MESSAGE_TYPE.OPEN.value,
        4,                            # BGP Version 4
        as_number_2bytes,
        hold_time,
        socket.inet_aton(bgp_identifier),
        optional_params_length  # Length of optional parameters
    )
    open_message += optional_params

    return open_message


def parse_open_message(payload):
    open_message = struct.unpack(
        '!BHH4sB', payload[:10])

    version = open_message[0]
    peer_as = open_message[1]
    hold_time = open_message[2]
    identifier = open_message[3]
    opt_param_len = open_message[4]
    opt_params = payload[10:10 + opt_param_len]

    asn_4byte = False
    found_cap_code_1 = False
    ipv4_unicast = False
    ipv6_unicast = False
    ipv4_unicast_add_path_send = False
    ipv4_unicast_add_path_recv = False
    ipv6_unicast_add_path_send = False
    ipv6_unicast_add_path_recv = False

    while opt_params:
        param_type = opt_params[0]
        param_len = opt_params[1]
        param_value = opt_params[2:2 + param_len]

        if param_type == 2:
            cap_code = param_value[0]
            # cap_len = param_value[1]
            cap_value = param_value[2:]

            if cap_code == 1:
                found_cap_code_1 = True
                afi = struct.unpack('!H', cap_value[0:2])[0]
                safi = cap_value[3]
                if afi == 1 and safi == 1:
                    ipv4_unicast = True
                elif afi == 2 and safi == 1:
                    ipv6_unicast = True
            elif cap_code == 65:
                peer_as = struct.unpack('!L', cap_value)
                asn_4byte = True
            elif cap_code == 69:
                afi = struct.unpack('!H', cap_value[0:2])[0]
                safi = cap_value[2]
                send_receive = cap_value[3]
                if afi == 1 and safi == 1 and send_receive == 1:
                    ipv4_unicast_add_path_recv = True
                elif afi == 1 and safi == 1 and send_receive == 2:
                    ipv4_unicast_add_path_send = True
                elif afi == 1 and safi == 1 and send_receive == 3:
                    ipv4_unicast_add_path_send = True
                    ipv4_unicast_add_path_recv = True
                elif afi == 2 and safi == 1 and send_receive == 1:
                    ipv6_unicast_add_path_recv = True
                elif afi == 2 and safi == 1 and send_receive == 2:
                    ipv6_unicast_add_path_send = True
                elif afi == 2 and safi == 1 and send_receive == 3:
                    ipv6_unicast_add_path_send = True
                    ipv6_unicast_add_path_recv = True

        opt_params = opt_params[2 + param_len:]

        if found_cap_code_1 is False:
            # Enable IPV4 default.
            ipv4_unicast = True

    return {
        "version": version,
        "asn": peer_as,
        "hold_time": hold_time,
        "identifier": str(ipaddress.IPv4Address(identifier)),
        "capabilities": {
            "asn_4byte": asn_4byte,
            "ipv4_unicast": ipv4_unicast,
            "ipv6_unicast": ipv6_unicast,
            "ipv4_unicast_add_path_send": ipv4_unicast_add_path_send,
            "ipv4_unicast_add_path_recv": ipv4_unicast_add_path_recv,
            "ipv6_unicast_add_path_send": ipv6_unicast_add_path_send,
            "ipv6_unicast_add_path_recv": ipv6_unicast_add_path_recv
        }
    }


# BGP Keepalive Message
def create_keepalive_message():
    keepalive_message = struct.pack(
        '!16sHB',
        BGP_HEADER_MARKER,
        19,                  # Length of Keepalive message
        MESSAGE_TYPE.KEEPALIVE.value
    )
    return keepalive_message


# BGP Process Update
def parse_update_message(peer_id, peer_ip, peer_as, payload,
                         as4byte=False,
                         ipv4_unicast=True, ipv6_unicast=False,
                         ipv4_unicast_add_path=False,
                         ipv6_unicast_add_path=False) -> dict:
    nlri = []
    next_hop = None
    withdrawn_routes = []
    afi = 1  # default ipv4
    safi = 1  # default unicaast
    as_path = []
    communities = []
    ext_communities = []
    large_communities = []
    local_pref = None
    multi_exit_disc = None

    offset = 0

    # Parse IPV4 afi 1 withdrawn prefixes length
    if len(payload) < offset + 2:
        raise ValueError("Payload too short to contain"
                         " Withdrawn Routes Length")

    withdrawn_routes_len = struct.unpack('!H', payload[offset:offset + 2])[0]
    offset += 2

    # Parse IPV4 afi 1 withdrawn prefixes
    withdrawn_routes = []
    if len(payload) < offset + withdrawn_routes_len:
        raise ValueError("Payload too short to contain Withdrawn Routes")

    withdrawn_data = payload[offset:offset + withdrawn_routes_len]
    offset += withdrawn_routes_len

    while withdrawn_data:
        if ipv4_unicast_add_path:
            path_identifier = struct.unpack('!I', withdrawn_data[0:4])[0]
            prefix_len = withdrawn_data[4]
        else:
            path_identifier = None
            prefix_len = withdrawn_data[0]

        prefix_bytes = (prefix_len + 7) // 8

        if len(withdrawn_data) < 1 + prefix_bytes:
            raise ValueError("Invalid Withdrawn Route length")

        if ipv4_unicast_add_path:
            prefix = withdrawn_data[5:5 + prefix_bytes]
            withdrawn_data = withdrawn_data[5 + prefix_bytes:]
        else:
            prefix = withdrawn_data[1:1 + prefix_bytes]
            withdrawn_data = withdrawn_data[1 + prefix_bytes:]

        prefix = str(ipaddress.IPv4Address(
            int.from_bytes(prefix.ljust(4, b'\x00'), 'big')))
        withdrawn_routes.append(
            {
                "identifier": path_identifier,
                "prefix": prefix,
                "prefix_length": prefix_len
            })

    # Parse Total Path Attributes Length
    if len(payload) < offset + 2:
        raise ValueError("Payload too short to contain Path Attributes Length")
    total_path_attrs_len = struct.unpack('!H', payload[offset:offset + 2])[0]
    offset += 2

    # Parse Path Attributes
    path_attrs = {}
    if len(payload) < offset + total_path_attrs_len:
        raise ValueError("Payload too short to contain Path Attributes")
    path_data = payload[offset:offset + total_path_attrs_len]
    offset += total_path_attrs_len

    while path_data:
        if len(path_data) < 3:
            raise ValueError("Path attribute data too short")
        flags = path_data[0]
        attr_type = path_data[1]
        if flags & 0x10:  # Extended Length
            if len(path_data) < 4:
                raise ValueError("Path attribute data too short"
                                 " for Extended Length")
            attr_len = struct.unpack('!H', path_data[2:4])[0]
            if len(path_data) < 4 + attr_len:
                raise ValueError("Path attribute value too short"
                                 " for Extended Length")
            attr_value = path_data[4:4 + attr_len]
            path_data = path_data[4 + attr_len:]
        else:  # Standard Length
            attr_len = path_data[2]
            if len(path_data) < 3 + attr_len:
                raise ValueError("Path attribute value too short"
                                 " for Standard Length")
            attr_value = path_data[3:3 + attr_len]
            path_data = path_data[3 + attr_len:]

        if attr_type == 2:  # AS_PATH
            as_path = []
            while attr_value:
                if len(attr_value) < 2:
                    raise ValueError("Invalid AS_PATH segment")
                segment_type = attr_value[0]
                segment_length = attr_value[1]
                asns = []
                if segment_type == 1:  # AS_SEQUENCE
                    if as4byte:
                        if len(attr_value) < 2 + segment_length * 4:
                            raise ValueError("AS_PATH AS_SEQUENCE segment"
                                             " too short for 4-byte ASNs")
                        asns = [struct.unpack('!I', attr_value[i:i + 4])[0]
                                for i in range(2, 2 + segment_length * 4, 4)]
                    else:
                        if len(attr_value) < 2 + segment_length * 2:
                            raise ValueError("AS_PATH AS_SEQUENCE segment"
                                             " too short for 2-byte ASNs")
                        asns = [struct.unpack('!H', attr_value[i:i + 2])[0]
                                for i in range(2, 2 + segment_length * 2, 2)]
                elif segment_type == 2:  # AS_SEQUENCE
                    if as4byte:
                        if len(attr_value) < 2 + (segment_length * 4):
                            raise ValueError("AS_PATH AS_SET segment"
                                             " too short for 4-byte ASNs")
                        asns = [[struct.unpack('!I', attr_value[i:i + 4])[0]
                                 for i in range(2, 2 + segment_length * 4, 4)]]
                    else:
                        if len(attr_value) < 2 + segment_length * 2:
                            raise ValueError("AS_PATH AS_SET segment"
                                             " too short for 2-byte ASNs")
                        asns = [[struct.unpack('!H', attr_value[i:i + 2])[0]
                                 for i in range(2, 2 + segment_length * 2, 2)]]
                else:
                    # Segment Type 3 and 4 are both deprecated as per RFC5056.
                    asns = []

                as_path.extend(asns)

                if as4byte:
                    attr_value = attr_value[2 + segment_length * 4:]
                else:
                    attr_value = attr_value[2 + segment_length * 2:]

        elif attr_type == 3:  # NEXT_HOP
            next_hop = str(ipaddress.IPv4Address(attr_value))
        elif attr_type == 4:  # MULTI_EXIT_DISC (MED)
            if len(attr_value) != 4:
                raise ValueError("Invalid MED length")
            multi_exit_disc = struct.unpack('!I', attr_value)[0]
        elif attr_type == 5:  # LOCAL_PREF
            if len(attr_value) != 4:
                raise ValueError("Invalid LOCAL_PREF length")
            local_pref = struct.unpack('!I', attr_value)[0]
        elif attr_type == 8:  # COMMUNITIES
            communities = [struct.unpack('!H', attr_value[i:i + 2])[0]
                           for i in range(0, len(attr_value), 2)]
        elif attr_type == 14:  # MP_REACH_NRLI
            afi, safi = struct.unpack("!HB", attr_value[:3])
            next_hop_length = attr_value[3]
            next_hop_end = 4 + next_hop_length
            next_hop_raw = attr_value[4:next_hop_end]
            # Convert Next Hop to human-readable format
            if afi == 1:  # IPv4
                next_hop = socket.inet_ntoa(next_hop_raw)
            elif afi == 2:  # IPv6
                next_hop = socket.inet_ntop(socket.AF_INET6, next_hop_raw)
            else:
                next_hop = None

            path_attrs['NEXT_HOP'] = next_hop

            # Skip Reserved Byte (1 byte after Next Hop)
            nlri_start = next_hop_end + 1
            nlri_data = attr_value[nlri_start:]

            index = 0

            while index < len(nlri_data):
                # At least 1 byte for Prefix Length
                if len(nlri_data) - index < 1:
                    break

                if afi == 2 and safi == 1 and ipv6_unicast_add_path:
                    path_identifier = struct.unpack(
                        '!I', nlri_data[index:index + 4])[0]
                    index += 4
                else:
                    path_identifier = None

                # Read Prefix Length (in bits)
                prefix_length = nlri_data[index]
                index += 1

                # Calculate the size of the prefix in bytes
                # Round up to the nearest byte
                prefix_size = (prefix_length + 7) // 8

                # Check if enough bytes remain
                if len(nlri_data) - index < prefix_size:
                    break

                # Extract Prefix
                raw_prefix = nlri_data[index:index + prefix_size]
                index += prefix_size

                # Determine Prefix Type and Format
                if afi == 1:  # IPv4
                    # Pad to 4 bytes
                    prefix = socket.inet_ntoa(raw_prefix.ljust(4, b'\x00'))
                elif afi == 2:  # IPv6
                    # Pad to 16 bytes
                    prefix = socket.inet_ntop(socket.AF_INET6,
                                              raw_prefix.ljust(16, b'\x00'))
                else:
                    # Unknown prefix...
                    continue

                nlri.append({
                    "identifier": path_identifier,
                    "prefix": prefix,
                    "prefix_length": prefix_length
                })

        elif attr_type == 15:  # MP_UNREACH_NRLI
            afi, safi = struct.unpack("!HB", attr_value[:3])

            # Skip Reserved Byte (1 byte after Next Hop)
            nlri_data = attr_value[3:]

            index = 0

            while index < len(nlri_data):

                # At least 1 byte for Prefix Length
                if len(nlri_data) - index < 1:
                    break

                if afi == 2 and safi == 1 and ipv6_unicast_add_path:
                    path_identifier = struct.unpack(
                        '!I', nlri_data[index:index + 4])[0]
                    index += 4
                else:
                    path_identifier = None

                # Read Prefix Length (in bits)
                prefix_length = nlri_data[index]
                index += 1

                # Calculate the size of the prefix in bytes
                # Round up to the nearest byte
                prefix_size = (prefix_length + 7) // 8

                # Check if enough bytes remain
                if len(nlri_data) - index < prefix_size:
                    break

                # Extract Prefix
                raw_prefix = nlri_data[index:index + prefix_size]
                index += prefix_size

                # Determine Prefix Type and Format
                if afi == 1:  # IPv4
                    # Pad to 4 bytes
                    prefix = socket.inet_ntoa(raw_prefix.ljust(4, b'\x00'))
                elif afi == 2:  # IPv6
                    # Pad to 16 bytes
                    prefix = socket.inet_ntop(socket.AF_INET6,
                                              raw_prefix.ljust(16, b'\x00'))
                else:
                    prefix = None

                # Append to the list
                withdrawn_routes.append(
                    {
                        "identifier": path_identifier,
                        "prefix": prefix,
                        "prefix_length": prefix_length
                    })

        elif attr_type == 16:  # EXTENDED COMMUNITIES
            ext_communities = []
            while attr_value:
                if len(attr_value) < 8:
                    raise ValueError("Invalid Extended Community length")
                community_type = attr_value[0]
                community_subtype = attr_value[1]
                community_value = attr_value[2:8]
                ext_communities.append((community_type,
                                        community_subtype,
                                        community_value.hex()))
                attr_value = attr_value[8:]
        elif attr_type == 32:  # LARGE COMMUNITIES
            large_communities = []
            while attr_value:
                if len(attr_value) < 12:
                    raise ValueError("Invalid Large Community length")
                global_admin = struct.unpack('!I', attr_value[0:4])[0]
                local_data_1 = struct.unpack('!I', attr_value[4:8])[0]
                local_data_2 = struct.unpack('!I', attr_value[8:12])[0]
                large_communities.append((global_admin,
                                          local_data_1,
                                          local_data_2))
                attr_value = attr_value[12:]

    # Parse AFI 1 SAFI 1 only NLRI (Network Layer Reachability Information)
    nlri_data = payload[offset:]
    while nlri_data:
        if ipv4_unicast_add_path:
            path_identifier = struct.unpack('!I', nlri_data[0:4])[0]
            prefix_len = nlri_data[4]
        else:
            path_identifier = None
            prefix_len = nlri_data[0]

        prefix_bytes = (prefix_len + 7) // 8

        if len(nlri_data) < 1 + prefix_bytes:
            raise ValueError("Invalid NLRI length")

        if ipv4_unicast_add_path:
            prefix = nlri_data[5: 5 + prefix_bytes]
            nlri_data = nlri_data[5 + prefix_bytes:]
        else:
            prefix = nlri_data[1:1 + prefix_bytes]
            nlri_data = nlri_data[1 + prefix_bytes:]

        prefix = str(ipaddress.IPv4Address(
            int.from_bytes(prefix.ljust(4, b'\x00'), 'big')))
        nlri.append({
            "path_identifier": path_identifier,
            "prefix": prefix,
            "prefix_length": prefix_len
        })

    return {"peer_id": peer_id,
            "peer_as": peer_as,
            "peer_ip": peer_ip,
            "afi": afi,
            "afi_name": str(AFI(afi)),
            "safi": safi,
            "safi_name": str(SAFI(safi)),
            "withdrawn_routes": withdrawn_routes,
            "as_path": as_path,
            "next_hop": next_hop,
            "communities": communities,
            "ext_communities": ext_communities,
            "large_communities": large_communities,
            "multi_exit_disc": multi_exit_disc,
            "local_pref": local_pref,
            "nlri": nlri}
