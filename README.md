# procurement-tools

![PyPI version](https://img.shields.io/pypi/v/procurement-tools.svg)

A handy collection of python utilities and tools to navigate federal contracting.

## Usage

```py
from procurement_tools import USASpending, UEI
print(USASpending.get_usaspending_URL("J7M9HPTGJ1S9"))
# 'https://www.usaspending.gov/recipient/bf1220c1-2373-042a-e8e1-33d5a29639d0-P/latest'

print(UEI.is_valid("J7M9HPTGJ1S9"))
# True
```

## Installation

```sh
pip install procurement-tools
```

## License

Apache 2.0
