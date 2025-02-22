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
from enum import Enum, auto

BGP_HEADER_MARKER = b'\xff' * 16


class BGP_STATE(Enum):
    """
    Enum representing BGP FSM States.
    """
    IDLE = auto()
    CONNECT = auto()
    ACTIVE = auto()
    OPENSENT = auto()
    OPENCONFIRM = auto()
    ESTABLISHED = auto()


class BGP_EVENT(Enum):
    """
    Enum representing BGP FSM Events.
    """
    START = auto()
    TCP_SUCCESS = auto()
    TCP_FAIL = auto()
    RETRY = auto()
    RECEIVE_OPEN = auto()
    OPEN_RECEIVED = auto()
    OPEN_FAIL = auto()
    SEND_KEEPALIVE = auto()
    RECEIVE_KEEPALIVE = auto()
    KEEPALIVE_RECEIVED = auto()
    KEEPALIVE_FAIL = auto()
    ERROR = auto()
    RECEIVE_NOTIFICATION = auto()
    UPDATE_RECEIVED = auto()
    MANUAL_SHUTDOWN = auto()


class MESSAGE_TYPE(Enum):
    """
    Enum representing BGP Message Types.
    """
    OPEN = 1                      # Open message
    UPDATE = 2                    # Update message
    NOTIFICATION = 3              # Notification message
    KEEPALIVE = 4                 # Keepalive message
    ROUTE_REFRESH = 5             # Route Refresh message (RFC 2918)
    CAPABILITY = 6                # Capability Advertisement (RFC 5492)
    ROUTE_REFRESH_ENHANCED = 128  # Enhanced Route Refresh (RFC 7313, Optional)


class AFI(Enum):
    """
    Enum representing BGP Address Family Identifiers (AFI).
    """
    IPV4 = 1              # IPv4 Address Family
    IPV6 = 2              # IPv6 Address Family


class SAFI(Enum):
    """
    Enum representing BGP Subsequent Address Family Identifiers (SAFI).
    """
    UNICAST = 1           # Unicast SAFI
    MULTICAST = 2         # Multicast SAFI


class ADD_PATH(Enum):
    """
    Enum representing ADD_PATH modes for BGP.

    Constants:
        SEND_ONLY (1): Advertises multiple paths but does not receive them.
        RECEIVE_ONLY (2): Receives multiple paths but does not advertise them.
        SEND_AND_RECEIVE (3): Both advertises and receives multiple paths.
    """
    RECEIVE_ONLY = 1
    SEND_ONLY = 2
    SEND_AND_RECEIVE = 3
