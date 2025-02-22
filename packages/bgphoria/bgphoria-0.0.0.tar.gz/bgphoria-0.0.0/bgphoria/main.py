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
import sys
# import argparse

from bgphoria import metadata


def main(argv):
    print(metadata.description + ' ' + metadata.version)

    # parser = argparse.ArgumentParser(description=metadata.description)
    # args = parser.parse_args()


def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    raise SystemExit(main(sys.argv))


if __name__ == '__main__':
    entry_point()
