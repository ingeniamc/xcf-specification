def create_tables_xcf(tables=None):
    """Helper to create an XCF with one or more tables.

    Args:
        tables (list of dict): List of tables to include. Each dict should have 'id', 'subnode', and 'elements' keys.
    """
    if tables is None:
        tables = [
            {
                "id": "COGGIG_COMP",
                "subnode": "1",
                "elements": [
                    {"address": 0, "data": "1234"},
                    {"address": 1, "data": "4321"},
                    {"address": 2, "data": "7531"},
                ],
            }
        ]
    tables_xml = "\n".join([
        f'<Table id="{tbl["id"]}" subnode="{tbl["subnode"]}">\n' +
        "\n".join(f'<Element address="{el["address"]}" data="{el["data"]}"/>' for el in tbl["elements"]) +
        '\n</Table>' for tbl in tables
    ])
    return f"""<?xml version="1.0" ?>
<IngeniaDictionary>
    <Header>
        <Version>2.2</Version>
    </Header>
    <Body>
        <Device Interface="CAN" firmwareVersion="0.1.0" ProductCode="741289" PartNumber="EVS-NET-C" RevisionNumber="" NodeID="64">
            <Registers>
                <Register access="rw" dtype="u32" id="MOT_BRAKE_FREQ" subnode="1" storage="10000"/>
            </Registers>
            <Tables>
                {tables_xml}
            </Tables>
        </Device>
    </Body>
</IngeniaDictionary>"""


def test_valid_table_structure(schema):
    """Test a valid Tables/Table/Element structure."""
    xcf = create_tables_xcf()
    assert schema.is_valid(xcf)


def test_element_missing_data(schema):
    """Test Element missing required data attribute (should fail)."""
    xcf = create_tables_xcf()
    # Remove data from first element
    xcf = xcf.replace('data="1234"', '')
    assert not schema.is_valid(xcf)


def test_element_invalid_data(schema):
    """Test Element with invalid hex data (should fail)."""
    tables = [
        {
            "id": "COGGIG_COMP",
            "subnode": "1",
            "elements": [
                {"address": 0, "data": "nothex"},
                {"address": 1, "data": "4321"},
            ],
        }
    ]
    xcf = create_tables_xcf(tables)
    assert not schema.is_valid(xcf)

def test_multiple_tables(schema):
    """Test multiple Table elements inside Tables."""
    tables = [
        {
            "id": "T1",
            "subnode": "1",
            "elements": [
                {"address": 0, "data": "1234"},
                {"address": 1, "data": "4321"},
            ],
        },
        {
            "id": "T2",
            "subnode": "2",
            "elements": [
                {"address": 0, "data": "abcd"},
                {"address": 1, "data": "dcba"},
            ],
        },
    ]
    xcf = create_tables_xcf(tables)
    assert schema.is_valid(xcf)

def test_negative_address_not_allowed(schema):
    """Test that negative addresses are not allowed in Table Element."""
    tables = [
        {
            "id": "COGGIG_COMP",
            "subnode": "1",
            "elements": [
                {"address": -1, "data": "1234"},
                {"address": 0, "data": "4321"},
            ],
        }
    ]
    xcf = create_tables_xcf(tables)
    assert not schema.is_valid(xcf)