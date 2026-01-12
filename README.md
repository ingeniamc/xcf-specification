# xcf-specification

This repository contains the XSD (XML Schema Definition) specification for Ingenia XCF (XML Configuration File)
dictionaries.

## Overview

The XSD files in this repository define the structure and validation rules for XCF files used with Ingenia/Novanta
Motion drives. These schemas ensure that XCF files are consistent, valid, and compatible with drive firmware and
software tools.

## Testing

The repository includes automated tests to validate example XCF files against the schema.

### Running Tests

Install Poetry (if not already installed):
```bash
pip install poetry
```

Install dependencies:
```bash
poetry install
```

Run all tests:
```bash
poetry run pytest
```

Run with verbose output:
```bash
poetry run pytest -v
```

Run specific test file:
```bash
poetry run pytest tests/test_validate_example_files.py
```
