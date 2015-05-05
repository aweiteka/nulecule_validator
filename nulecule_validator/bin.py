
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
