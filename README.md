# procurement-tools

[![PyPI version](https://img.shields.io/pypi/v/procurement-tools.svg)](https://pypi.org/project/procurement-tools/)

A handy collection of python utilities and tools to navigate federal contracting.

## Features

- [x] UEI validation
- [x] Get a URL for an entity from USASpending
- [x] Get recent award data for an entity from USASpending
- [x] Lookup a FAR provision by citation
- [x] Get entity information from the SAM entity
- [x] Access innovations from the Periodic Table of Acquisition Innovations

## Usage

For full documentation, head to [the docs](https://procurement-tools.readthedocs.io/en/latest/).

```py
from procurement_tools import FAR, UEI, USASpending, PeriodicTable
print(UEI.is_valid("J7M9HPTGJ1S9"))
# True

print(USASpending.get_usaspending_URL("J7M9HPTGJ1S9"))
# 'https://www.usaspending.gov/recipient/bf1220c1-2373-042a-e8e1-33d5a29639d0-P/latest'

print(FAR.get_section("17.502-2"))
# Returns a pydantic model with the title, section number, url, and text of the section

print(PeriodicTable.get_random_innovation())
# Returns a dict with an innovation from the FAI Periodic Table of Acquisition Innovations
```

Additionally, we have the beginning of a SAM API client:

```python
from procurement_tools import get_entity
res = get_entity({"ueiSAM":"XRVFU3YRA2U5"})
print(res)
# Returns a pydantic model with the latest SAM data for a given Entity
```

## CLI Usage

# `fargo`

**Usage**:

```console
$ fargo [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--install-completion`: Install completion for the current shell.
- `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
- `--help`: Show this message and exit.

**Commands**:

- `far`: Get a provision of the FAR
- `sam`: Get a SAM entity's JSON data by providing...
- `usaspending`: Get JSON data about an entity from...

## `fargo far`

Get a provision of the FAR

**Usage**:

```console
$ fargo far [OPTIONS] SECTION_NUMBER
```

**Arguments**:

- `SECTION_NUMBER`: [required]

**Options**:

- `--help`: Show this message and exit.

## `fargo sam`

Get a SAM entity's JSON data by providing a UEI

**Usage**:

```console
$ fargo sam [OPTIONS] UEI
```

**Arguments**:

- `UEI`: [required]

**Options**:

- `--help`: Show this message and exit.

## `fargo usaspending`

Get JSON data about an entity from USASpending by providing a UEI

**Usage**:

```console
$ fargo usaspending [OPTIONS] UEI
```

**Arguments**:

- `UEI`: [required]

**Options**:

- `--awards / --no-awards`: [default: no-awards]
- `--help`: Show this message and exit.

## Installation

```sh
pip install procurement-tools
```

## License

Apache 2.0
