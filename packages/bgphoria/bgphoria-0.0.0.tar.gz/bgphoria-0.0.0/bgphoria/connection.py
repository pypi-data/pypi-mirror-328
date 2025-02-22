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
import asyncio

from bgphoria.exceptions import (BGPConnectionTimeout,
                                 BGPConnectionClosed,
                                 BGPConnectionError)


class TCPClient(object):
    __slots__ = ("__reader", "__writer", "__timeout")

    def __init__(self):
        self.__reader = None
        self.__writer = None
        self.__timeout = None

    def timeout(self, value):
        self.__timeout = value

    @property
    def connected(self):
        if self.__reader and self.__writer:
            return True
        else:
            return False

    async def connect(self, host, port, timeout=None):
        if timeout is None:
            timeout = self.__timeout

        try:
            self.__reader, self.__writer = await asyncio.wait_for(
                asyncio.open_connection(host, port),
                timeout=timeout
            )
        except asyncio.TimeoutError:
            raise BGPConnectionTimeout("Connection timed out")
        except Exception as e:
            raise BGPConnectionError(f"Failed to connect: {e}")

    async def read(self, n):
        if self.__reader is None:
            raise BGPConnectionClosed("Socket is not connected")

        try:
            data = await asyncio.wait_for(self.__reader.readexactly(n),
                                          timeout=self.__timeout)
            return data
        except asyncio.TimeoutError:
            raise BGPConnectionTimeout("Read operation timed out")
        except Exception:
            self.close()
            raise BGPConnectionError("Connection closed")

    async def send(self, data):
        if self.__writer is None:
            raise BGPConnectionClosed("Socket is not connected")

        try:
            self.__writer.write(data)
            await self.__writer.drain()  # Ensure data is sent
        except Exception:
            self.close()
            raise BGPConnectionError("Connection closed")

    def settimeout(self, timeout):
        self.__timeout = timeout

    async def close(self):
        if self.__writer:
            try:
                self.__writer.close()
                await self.__writer.wait_closed()
            except Exception:
                pass
            self.__reader = None
            self.__writer = None
