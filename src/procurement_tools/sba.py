from .models.naics_size_standards import Sector, Subsector, NaicsSizeStandard
from pathlib import Path
from python_calamine import CalamineWorkbook


class SizeStandardsTable:

    @staticmethod
    def create_json_from_file():
        workbook = CalamineWorkbook.from_path(
            Path(__file__).parent / "data/size_standards_table.xlsx"
        )
        table = workbook.get_sheet_by_name("table_of_size_standards-all").to_python()
        footnotes = _extract_footnotes(
            workbook.get_sheet_by_name("footnotes").to_python()
        )

        sector = None
        subsector = None
        results = []

        for row in table[1:]:
            if row[1].startswith("Sector"):  # This is a sector
                sector = _extract_sector(row)
            elif row[0] == "":
                continue
            elif str(row[0]).startswith("Subsector"):  # This is a subsector
                sector, subsector = _extract_subsector(sector, row)
            else:
                results.append(_extract_naics(sector, subsector, row, footnotes))
        return results


def _extract_sector(row):
    data = row[1].split(" – ")
    if data[0] == "Sector 44 - 45":
        sector_id = 44
    elif data[0] == "Sector 48 - 49":
        sector_id = 48
    else:
        sector_id = data[0].replace("Sector ", "")
    description = data[1]
    return Sector(id=sector_id, description=description)


def _extract_subsector(sector: Sector, row: dict) -> (Sector, Subsector):
    data = row[0].replace("-", "–").split("–")
    subsector_id = data[0].replace("Subsector ", "").strip()
    if int(subsector_id[:2]) != sector.id:
        sector.id = int(subsector_id[:2])
    description = data[1].strip()
    return (sector, Subsector(id=subsector_id, description=description))


def _extract_footnotes(table):
    rows = [row for row in table if type(row[0]) == float]
    return {int(row[0]): row[1] for row in rows if row[1]}


def _extract_naics(
    sector: Sector, subsector: Subsector, row: dict, footnotes: dict
) -> NaicsSizeStandard:

    # Coerce NAICS code
    try:
        code = int(row[0])
        footnote = None
        parent = None
    except ValueError:
        code = row[0].replace(" ", "_").replace("(", "").replace(")", "").lower()
        footnote = row[4].replace("See footnote ", "")
        parent = int(row[0].split(" ")[0])

    # Coerce revenue limit / asset limit
    try:
        revenue_limit = float(row[2]) if row[2] else None
        asset_limit = None
    except ValueError:
        revenue_limit = None
        asset_limit = float(row[2].split(" ")[0].replace("$", ""))

    return NaicsSizeStandard(
        code=code,
        description=row[1],
        sector=sector,
        subsector=subsector,
        revenue_limit=revenue_limit,
        employee_limit=row[3] if row[3] else None,
        asset_limit=asset_limit,
        footnote=footnote,
        parent=parent,
    )
