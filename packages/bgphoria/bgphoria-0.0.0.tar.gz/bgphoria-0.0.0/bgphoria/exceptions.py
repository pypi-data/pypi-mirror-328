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

class Error(Exception):
    """BGPPhoria Base Exception"""


class BGPConnectionError(Error):
    """BGP Session Connection Closed"""


class BGPConnectionClosed(BGPConnectionError):
    """BGP Session Connection Closed"""


class BGPConnectionTimeout(BGPConnectionError):
    """BGP Session Connection Closed"""


class BGPInvalidMessage(Error):
    """BGP Session Invalid Message"""
