from pathlib import Path
import pytest
import xmlschema


def get_schema_path():
    """Get the path to the schema file."""
    return Path(__file__).parent.parent / "config.xsd"


@pytest.fixture(scope="session")
def schema():
    """Load the XSD schema once for all tests."""
    return xmlschema.XMLSchema(get_schema_path())
