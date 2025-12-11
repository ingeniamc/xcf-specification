
import pytest


def create_test_xcf(data_value=None):
    """Helper to create a minimal XCF with optional data attribute."""
    data_attr = f' data="{data_value}"' if data_value is not None else ''
    return f"""<?xml version="1.0" ?>
<IngeniaDictionary>
    <Header>
        <Version>2.2</Version>
    </Header>
    <Body>
        <Device Interface="CAN" firmwareVersion="0.1.0" ProductCode="741289" PartNumber="EVS-NET-C" RevisionNumber="" NodeID="64">
            <Registers>
                <Register access="rw" dtype="u32" id="TEST_REG" subnode="1" storage="10000"{data_attr}/>
            </Registers>
        </Device>
    </Body>
</IngeniaDictionary>"""



def test_data_attribute_is_optional(schema):
    """Test that data attribute is optional."""
    xcf = create_test_xcf()
    assert schema.is_valid(xcf)


def test_valid_hex_data(schema):
    """Test a few valid lowercase hex values for data attribute."""
    for hex_val in ["01", "deadbeef", "00aa11bb"]:
        xcf = create_test_xcf(hex_val)
        assert schema.is_valid(xcf)


def test_invalid_hex_data(schema):
    """Test a few invalid values for data attribute."""
    for hex_val in ["0", "FF", "hello", "0x01", "123"]:
        xcf = create_test_xcf(hex_val)
        assert not schema.is_valid(xcf)


def test_minimum_valid_length(schema):
    """Test minimum valid length (2 hex chars = 1 byte)."""
    xcf = create_test_xcf("00")
    assert schema.is_valid(xcf)

def test_various_byte_patterns(schema):
    """Test various valid byte patterns."""
    patterns = [
        "00",  # All zeros
        "ff",  # All ones
        "01",  # Single bit
        "0f",  # Lower nibble
        "f0",  # Upper nibble
        "5a",  # Mixed
    ]
    for pattern in patterns:
        xcf = create_test_xcf(pattern)
        assert schema.is_valid(xcf), f"Failed for pattern: {pattern}"

def test_multi_byte_sequences(schema):
    """Test multi-byte sequences."""
    sequences = [
        "0001",  # 2 bytes
        "000102",  # 3 bytes
        "00010203",  # 4 bytes
        "0123456789abcdef",  # 8 bytes
    ]
    for seq in sequences:
        xcf = create_test_xcf(seq)
        assert schema.is_valid(xcf), f"Failed for sequence: {seq}"
