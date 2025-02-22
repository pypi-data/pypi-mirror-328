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
from datetime import datetime

# The package name, which is also the "UNIX name" for the project.
package = 'bgphoria'
project = 'BGPHoria'
project_no_spaces = project.replace(' ', '')

# Please follow https://www.python.org/dev/peps/pep-0440/
version = '0.0.0'
description = project
author = 'Interstellio IO (PTY) LTD'
email = 'opensource@interstellio.io'
license = 'LGPLv3'
copyright = '2025-%s %s' % (datetime.now().year, author,)
url = 'https://github.com/interstellio/bgphoria'
identity = project + ' v' + version

# Classifiers
# <http://pypi.python.org/pypi?%3Aaction=list_classifiers>
classifiers = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Intended Audience :: Information Technology',
    'Intended Audience :: Telecommunications Industry',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3.10',
    'Topic :: System :: Monitoring',
    'Topic :: System :: Networking']
