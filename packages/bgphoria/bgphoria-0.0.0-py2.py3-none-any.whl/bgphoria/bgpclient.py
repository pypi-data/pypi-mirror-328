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
import json
import asyncio
import logging
import traceback

from bgphoria.exceptions import BGPConnectionError
from bgphoria.constants import (BGP_STATE,
                                MESSAGE_TYPE,
                                ADD_PATH)
from bgphoria.connection import TCPClient
from bgphoria.messages import (read_message,
                               parse_notification,
                               create_open_message,
                               parse_open_message,
                               create_keepalive_message,
                               parse_update_message)

log = logging.getLogger(__name__)


class BGPClient(object):
    # BGP FSM based on IETF RFC4271
    # Under-construction / Planning Phase
    def __init__(self, peer_id,
                 peer_ip, peer_as, local_as, local_bgp_id,
                 update_callback=None, ipv4_unicast=True, ipv6_unicast=False,
                 ipv4_unicast_add_path=None, ipv6_unicast_add_path=None):
        self.__conn = TCPClient()
        self.__state = BGP_STATE.IDLE
        self.__active_keepalive_loop = None
        self.__active_state_task = None

        self.__hold_time = 90
        self.__peer_id = peer_id
        self.__peer_ip = peer_ip
        self.__peer_as = peer_as
        self.__local_as = local_as
        self.__local_bgp_id = local_bgp_id
        self.__update_callback = update_callback
        self.__ipv4_unicast = ipv4_unicast
        self.__ipv6_unicast = ipv6_unicast
        self.__ipv4_unicast_add_path = ipv4_unicast_add_path
        self.__ipv6_unicast_add_path = ipv6_unicast_add_path

        self.__session = {"ipv4_unicast": True,
                          "ipv4_unicast_add_path_recv": False,
                          "ipv6_unicast": False,
                          "ipv6_unicast_add_path_recv": False}

    async def connect(self):
        asyncio.create_task(self.__start_event())

    async def stop(self):
        if self.__active_state_task:
            self.__active_state_task.cancel()
            try:
                await self.__active_state_task
            except asyncio.CancelledError:
                pass

        self.__state == BGP_STATE.IDLE

        if self.__active_keepalive_loop:
            self.__active_keepalive_loop.cancel()
            try:
                await self.__active_keepalive_loop
            except asyncio.CancelledError:
                pass

        self._conn.close()

    @property
    def state(self):
        match self.__state:
            case BGP_STATE.IDLE:
                return "idle"
            case BGP_STATE.CONNECT:
                return "connect"
            case BGP_STATE.ACTIVE:
                return "active"
            case BGP_STATE.OPENSENT:
                return "opensent"
            case BGP_STATE.OPENCONFIRM:
                return "openconfirm"
            case BGP_STATE.ESTABLISHED:
                return "established"
            case _:
                return "unknown_state"

    def __log(self, level, message):
        """Logs messages with neighbor-specific context."""
        full_message = (
            f"BGP Neigbour: {self.__peer_ip} PEER-AS: {self.__peer_as}"
            f" ({self.__peer_id}): {message}"
        )
        log.log(level, full_message)

    async def __start_event(self):
        if self.__state == BGP_STATE.IDLE:
            asyncio.create_task(self.__connect_state())
        else:
            self.__log(logging.CRITICAL, "Start Event failed,"
                                         " not in idle state")

    async def __fail_event(self, msg):
        self.__log(logging.ERROR, msg)
        await self.__conn.close()
        if self.__active_keepalive_loop:
            self.__active_keepalive_loop.cancel()
            try:
                await self.__active_keepalive_loop
            except asyncio.CancelledError:
                pass
        asyncio.create_task(self.__active_state())

    async def __keepalive_loop(self, holdtime):
        keep_alive_interval = int(holdtime / 3)
        while 1:
            try:
                await asyncio.sleep(keep_alive_interval)
            except asyncio.CancelledError:
                break

            if (self.__conn.connected
                    and self.__state == BGP_STATE.ESTABLISHED):
                # Send Keepalive message
                await self.__conn.send(create_keepalive_message())
                self.__log(logging.INFO, "Sent KEEPALIVE")
            else:
                break

    async def __process_notification(self, payload):
        error_code, error_subcode, msg = parse_notification(payload)
        await self.__fail_event(f"Received Notification message:"
                                f" Error Code {error_code},"
                                f" Subcode {error_subcode}, Message: {msg}")

    async def __connect_state(self):
        self.__log(logging.INFO, f"Transitioning from {self.state} to Connect")
        self.__state = BGP_STATE.CONNECT
        for i in range(3):
            try:
                await self.__conn.connect(self.__peer_ip, 179, timeout=5)
                self.__conn.timeout(self.__hold_time)
                asyncio.create_task(self.__open_sent_state())
                break
            except BGPConnectionError as e:
                self.__log(logging.ERROR, str(e))
                if i == 2:
                    self.__log(logging.INFO, "Transitioning from"
                                             " Connect to Active")
                    asyncio.create_task(self.__active_state())
                    break

    async def __active_state(self):
        self.__log(logging.INFO, f"Transitioning from {self.state} to Active")
        self.__state = BGP_STATE.ACTIVE
        # Sleep 5 seconds.
        await asyncio.sleep(5)
        asyncio.create_task(self.__connect_state())

    async def __open_sent_state(self):
        self.__log(logging.INFO, f"Transitioning from {self.state}"
                                 "to OpenSent")
        self.__state = BGP_STATE.OPENSENT

        # Send Open Message
        msg = create_open_message(
            self.__local_as,
            self.__hold_time,
            self.__local_bgp_id,
            ipv4_unicast=self.__ipv4_unicast,
            ipv6_unicast=self.__ipv6_unicast,
            ipv4_unicast_add_path=self.__ipv4_unicast_add_path,
            ipv6_unicast_add_path=self.__ipv6_unicast_add_path)
        try:
            await self.__conn.send(msg)
        except BGPConnectionError as e:
            await self.__fail_event(str(e))
            return  # short circuit

        # Receive Open Message
        try:
            length, message_type, payload = await read_message(self.__conn)
        except BGPConnectionError as e:
            await self.__fail_event(str(e))
            return  # short circuit

        if message_type == MESSAGE_TYPE.OPEN.value:
            self.__peer = parse_open_message(payload)
            # Set Socket Timeout to Hold-Time from peer in open message.
            self.__conn.settimeout(self.__peer['hold_time'])

            if (self.__ipv4_unicast
                    and self.__peer['capabilities']['ipv4_unicast']):
                self.__session['ipv4_unicast'] = True
                if (self.__ipv4_unicast_add_path in (ADD_PATH.RECEIVE_ONLY,
                                                     ADD_PATH.SEND_AND_RECEIVE)
                    and (self.__peer['capabilities']
                         ['ipv4_unicast_add_path_send'])):
                    self.__session['ipv4_unicast_add_path_recv'] = True
                else:
                    self.__session['ipv4_unicast_add_path_recv'] = False
            else:
                self.__session['ipv4_unicast'] = False

            if (self.__ipv6_unicast
                    and self.__peer['capabilities']['ipv6_unicast']):
                self.__session['ipv6_unicast'] = True
                if (self.__ipv6_unicast_add_path in (ADD_PATH.RECEIVE_ONLY,
                                                     ADD_PATH.SEND_AND_RECEIVE)
                    and (self.__peer['capabilities']
                         ['ipv6_unicast_add_path_send'])):
                    self.__session['ipv6_unicast_add_path_recv'] = True
                else:
                    self.__session['ipv6_unicast_add_path_recv'] = False
            else:
                self.__session['ipv6_unicast'] = False

            asyncio.create_task(self.__open_confirm_state())
        elif message_type == MESSAGE_TYPE.NOTIFICATION.value:
            await self.__process_notification(payload)
        else:
            await self.__fail_event("Unexpected message type"
                                    " during session setup")

    async def __open_confirm_state(self):
        self.__log(logging.INFO, f"Transitioning from {self.state}"
                                 " to OpenConfirm")
        self.__state = BGP_STATE.OPENCONFIRM

        # Send Keepalive.
        try:
            await self.__conn.send(create_keepalive_message())
        except BGPConnectionError as e:
            await self.__fail_event(f"Sending Keepalive {str(e)}")
            return  # short circuit

        # Receive Keepalive.
        try:
            length, message_type, payload = await read_message(self.__conn)
        except BGPConnectionError as e:
            await self.__fail_event(f"Receive Keepalive {str(e)}")
            return  # short circuit

        if message_type == MESSAGE_TYPE.KEEPALIVE.value:
            asyncio.create_task(self.__established_state())
        elif message_type == MESSAGE_TYPE.NOTIFICATION.value:
            await self.__process_notification(payload)
        else:
            await self.__fail_event(f"Unexpected message type {message_type}"
                                    " during OpenConfirm received")

    async def __process_update(self, payload):
        try:
            update = parse_update_message(
                self.__peer_id,
                self.__peer_ip,
                self.__peer_as,
                payload,
                as4byte=self.__peer['capabilities']['asn_4byte'],
                ipv4_unicast=self.__session['ipv4_unicast'],
                ipv6_unicast=self.__session['ipv6_unicast'],
                ipv4_unicast_add_path=(self.__session
                                       ['ipv4_unicast_add_path_recv']),
                ipv6_unicast_add_path=(self.__session
                                       ['ipv6_unicast_add_path_recv']))
            if self.__update_callback:
                self.__update_callback(update)
            else:
                self.__log(
                    logging.INFO,
                    "\n" + json.dumps(
                        {"afi": update["afi"],
                         "afi_name": update["afi_name"],
                         "safi": update["safi"],
                         "safi_name": update["safi_name"],
                         "widthdrawn_routes": update["withdrawn_routes"],
                         "as_path": update["as_path"],
                         "next_hop": update["next_hop"],
                         "communities": update["communities"],
                         "ext_communities": update["ext_communities"],
                         "large_communities": update["large_communities"],
                         "multi_exit_disc": update["multi_exit_disc"],
                         "local_pref": update["local_pref"],
                         "nlri": update["nlri"]}, indent=4))
        except Exception as e:
            trace = str(traceback.format_exc())
            self.__log(logging.ERROR, f"Error: {e}\n{trace}")

    async def __established_state(self):
        self.__log(logging.INFO, f"Transitioning from {self.state}"
                                 " to Established")
        self.__state = BGP_STATE.ESTABLISHED

        self.__active_keepalive_loop = \
            asyncio.create_task(
                self.__keepalive_loop(self.__peer['hold_time']))

        # Receive and process messages
        while (self.__conn.connected
                and self.__state == BGP_STATE.ESTABLISHED):
            try:
                length, message_type, payload = await read_message(self.__conn)
            except BGPConnectionError as e:
                await self.__fail_event(f"{str(e)}")

            if message_type == MESSAGE_TYPE.UPDATE.value:
                # Process update...
                await self.__process_update(payload)
                continue
            elif message_type == MESSAGE_TYPE.NOTIFICATION.value:
                await self.__process_notification(payload)
                break
            elif message_type == MESSAGE_TYPE.KEEPALIVE.value:
                self.__log(logging.INFO,
                           "Received keep-alive")
            else:
                self.__log(logging.ERROR,
                           f"Received unhandled message type: {message_type}")
