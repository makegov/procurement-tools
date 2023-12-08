import json
from procurement_tools import FAR, USASpending, SBIR, get_entity
import typer
from typing_extensions import Annotated

app = typer.Typer()
sbir_app = typer.Typer()
app.add_typer(sbir_app, name="sbir")


@app.command()
def far(section_number: str):
    """Get a provision of the FAR"""
    res = FAR.get_section(section_number)
    text = res.title + "\n" + res.body + "\n\nURL: " + res.url
    print(text)


@app.command()
def sam(uei: str):
    """Get a SAM entity's JSON data by providing a UEI"""
    res = get_entity({"ueiSAM": uei})
    print(res.model_dump_json())


@sbir_app.command()
def awards(
    agency: str = None,
    company: str = None,
    year: int = None,
    research_institution: str = None,
):
    """Get SBIR awards"""
    res = SBIR.get_awards(
        agency=agency,
        company=company,
        year=year,
        research_institution=research_institution,
    )
    print(res.model_dump_json())


@sbir_app.command()
def solicitations(keyword: str = None, agency: str = None, open: int = 1):
    """Get SBIR solicitaitons"""
    res = SBIR.get_solicitations(keyword=keyword, agency=agency, open=open)
    print(res.model_dump_json())


@app.command()
def usaspending(
    uei: str,
    awards: Annotated[
        bool,
        typer.Option(
            help="Get the latest awards for entity. If false, then gets the entity's profile data"
        ),
    ] = False,
):
    """Get JSON data about an entity from USASpending by providing a UEI"""

    if awards:
        res = USASpending.get_latest_recipient_awards(uei)
        print(json.dumps(res, indent=2))
    else:
        res = USASpending.get_recipient_profile(uei)
        print(json.dumps(res, indent=2))


typer_click_object = typer.main.get_command(app)
