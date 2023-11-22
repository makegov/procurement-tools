# procurement-tools

[![PyPI version](https://img.shields.io/pypi/v/procurement-tools.svg)](https://pypi.org/project/procurement-tools/)

A handy collection of python utilities and tools to navigate federal contracting.

## Usage

```py
from procurement_tools import FAR, UEI, USASpending
print(UEI.is_valid("J7M9HPTGJ1S9"))
# True

print(USASpending.get_usaspending_URL("J7M9HPTGJ1S9"))
# 'https://www.usaspending.gov/recipient/bf1220c1-2373-042a-e8e1-33d5a29639d0-P/latest'

print(FAR.get_section("17.502-2"))
# Returns a pydantic model with the title, section number, url, and text of the section
```

## Installation

```sh
pip install procurement-tools
```

## License

Apache 2.0
