import json
import re
from pathlib import Path
import sys

try:
    import jsonschema
except ImportError:
    print('jsonschema package not installed', file=sys.stderr)
    sys.exit(1)

def load_jsonc(path: Path):
    text = path.read_text()
    # remove // comments
    text = re.sub(r"//.*", "", text)
    # remove /* */ comments
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    return json.loads(text)

schema = load_jsonc(Path('schemas/hef-schema.jsonc'))
instance = load_jsonc(Path('example.hef.json'))

jsonschema.validate(instance=instance, schema=schema)
print('Validation succeeded')
