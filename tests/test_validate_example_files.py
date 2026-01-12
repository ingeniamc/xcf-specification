from pathlib import Path
import pytest
import xmlschema

EXAMPLES_DIR = "example_files"


def get_example_files():
    """Get all .xcf files from the examples directory."""
    examples_path = Path(__file__).parent.parent / EXAMPLES_DIR
    return list(examples_path.glob("*.xcf"))


@pytest.mark.parametrize("xcf_file", get_example_files())
def test_validate_xcf_file(schema, xcf_file):
    """Test that each .xcf file is valid against the schema."""
    try:
        schema.validate(xcf_file)
    except xmlschema.XMLSchemaValidationError as e:
        pytest.fail(f"{xcf_file.name} is invalid: {e}")
