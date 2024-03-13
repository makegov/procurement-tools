import pytest
from procurement_tools.sba import (
    SizeStandardsTable,
    _extract_sector,
    _extract_subsector,
)
from procurement_tools.models.naics_size_standards import (
    Sector,
    Subsector,
    NaicsSizeStandard,
)


@pytest.fixture
def sector_row():
    return ["", "Sector 11 – Agriculture, Forestry, Fishing and Hunting", "", "", ""]


@pytest.fixture
def sector():
    return Sector(id=11, description="Agriculture, Forestry, Fishing and Hunting")


@pytest.fixture
def sector_45():
    return Sector(id=457, description="Retail Trade")


@pytest.fixture
def subsector_row():
    return ["Subsector 111 – Crop Production", "", "", "", ""]


@pytest.fixture
def subsector_sector_45_row():
    return ["Subsector 457 – Gasoline Stations and Fuel Dealers", "", "", "", ""]


def test_sector_row_extract(sector_row):
    expected = Sector(id=11, description="Agriculture, Forestry, Fishing and Hunting")
    result = _extract_sector(sector_row)
    assert result == expected


def test_subsector_row_extract(subsector_row, sector):
    expected = Subsector(id=111, description="Crop Production")
    result = _extract_subsector(
        sector,
        subsector_row,
    )
    assert result == (sector, expected)


def test_subsector_row_extract_sector45(sector_45, subsector_sector_45_row):
    expected = Subsector(id=457, description="Gasoline Stations and Fuel Dealers")
    result = _extract_subsector(sector_45, subsector_sector_45_row)
    assert result == (sector_45, expected)


def test_size_standards_table():
    result = SizeStandardsTable.create_json_from_file()
    assert result[100] == NaicsSizeStandard(
        code=236115,
        description="New Single-family Housing Construction (Except For-Sale Builders)",
        sector=Sector(id=23, description="Construction"),
        subsector=Subsector(id=236, description="Construction of Buildings"),
        revenue_limit=45.0,
        employee_limit=None,
        footnote=None,
        parent=None,
        asset_limit=None,
    )

    assert result[96].code == 221210
    assert result[96].employee_limit == 1150

    assert result[112] == NaicsSizeStandard(
        code="237990_exception",
        description="Dredging and Surface Cleanup Activities2",
        sector=Sector(id=23, description="Construction"),
        subsector=Subsector(
            id=237, description="Heavy and Civil Engineering Construction"
        ),
        revenue_limit=37.0,
        employee_limit=None,
        footnote="2",
        parent=237990,
        asset_limit=None,
    )
