#!/usr/bin/env python3

import argparse
import jsonschema
import logging
import sys
import yaml

SCHEMA = 'data/schema.yaml'

logger = logging.getLogger('nulecule')
logger.setLevel(logging.WARNING)

parser = argparse.ArgumentParser()
parser.add_argument('spec', help='Nulecule specfile in YAML format to be validated')
args = parser.parse_args()

try:
    with open(args.spec) as fh:
        data = yaml.load(fh.read())
except FileNotFoundError as e:
    logger.warning(str(e))
    sys.exit(1)

try:
    with open(SCHEMA) as fh:
        schema = yaml.load(fh.read())
except FileNotFoundError as e:
    logger.warning('Schema not found: {e}'.format(e=str(e)))
    sys.exit(1)

validator = jsonschema.Draft4Validator(schema)
errors = sorted(validator.iter_errors(data), key=lambda e: e.path)

if not errors:
    sys.exit(0)

for error in errors:
    print('{path}: {msg}'.format(path=' > '.join(error.path), msg=error.message))

