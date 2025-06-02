import jsonschema
import json5
import pathlib
import sys

SCHEMA_FILE = pathlib.Path('schemas/hef-schema.jsonc')


def load_schema():
    with SCHEMA_FILE.open('r', encoding='utf-8') as f:
        return json5.load(f)


def validate_file(path, schema):
    with open(path, 'r', encoding='utf-8') as f:
        data = json5.load(f)
    jsonschema.validate(data, schema)


def main():
    schema = load_schema()
    files = list(pathlib.Path('.').rglob('*.hef.jsonc'))
    if not files:
        print('No .hef.jsonc files found')
        return
    success = True
    for fp in files:
        try:
            validate_file(fp, schema)
            print(f"Validated {fp}")
        except jsonschema.ValidationError as e:
            print(f"Validation failed for {fp}: {e}")
            success = False
        except Exception as e:
            print(f"Error validating {fp}: {e}")
            success = False
    if not success:
        sys.exit(1)


if __name__ == '__main__':
    main()
