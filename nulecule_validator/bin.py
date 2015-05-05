# Copyright (C) 2015 Tomas Radej <tradej@redhat.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -*- coding: utf-8 -*-

import sys

from argparse import ArgumentParser

from nulecule_validator import Validator
from nulecule_validator import exceptions, settings

def main():
    parser = ArgumentParser()
    parser.add_argument('filename', help='File to validate')
    parser.add_argument('-V', '--version',
                        help='Version of the spec to validate against. Latest by default.',
                        default=settings.DEFAULT_VERSION)
    args = parser.parse_args()

    try:
        validator = Validator(version=args.version)
        errors = validator.find_errors(args.filename)
    except exceptions.SchemaError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    if not errors:
        sys.exit(0)

    for error in errors:
        print('{path}: {msg}'.format(path=' > '.join(error.path), msg=error.message))
    sys.exit(1)
