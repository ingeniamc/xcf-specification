import sys
import glob
import os
import xmlschema

SCHEMA_FILE = "config.xsd"
EXAMPLES_DIR = "example_files"

schema = xmlschema.XMLSchema(SCHEMA_FILE)

errors = []
files = glob.glob(os.path.join(EXAMPLES_DIR, "*.xcf"))

if not files:
    print(f"No .xcf files found in the '{EXAMPLES_DIR}' directory.")
    sys.exit(2)

for xcf_file in files:
    try:
        schema.validate(xcf_file)
        print(f"{xcf_file}: valid")
    except xmlschema.XMLSchemaValidationError as e:
        print(f"{xcf_file}: INVALID\n{e}")
        errors.append(xcf_file)

if errors:
    print(f"\nValidation failed for {len(errors)} file(s): {', '.join(errors)}")
    sys.exit(1)
else:
    print("\nAll XCF files are valid.")
