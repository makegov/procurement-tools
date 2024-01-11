from datetime import datetime, timedelta
import json
from procurement_tools import FAR, USASpending, SAM, SBIR
from procurement_tools.models.opportunities import OpportunitiesRequestParams
import typer
from typing import Optional
from typing_extensions import Annotated

app = typer.Typer()
sam_app = typer.Typer()
sbir_app = typer.Typer()
app.add_typer(sam_app, name="sam")
app.add_typer(sbir_app, name="sbir")


TODAY = datetime.now().strftime("%m/%d/%Y")


@app.command()
def far(section_number: str):
    """Get a provision of the FAR"""
    res = FAR.get_section(section_number)
    text = res.title + "\n" + res.body + "\n\nURL: " + res.url
    print(text)


@sam_app.command()
def entity(uei: str):
    """Get a SAM entity's JSON data by providing a UEI"""
    res = SAM.get_entity({"ueiSAM": uei})
    print(res.model_dump_json())


@sam_app.command()
def opportunities(
    *,
    q: str = "",
    postedFrom: Optional[
        str
    ] = None,  # (datetime.now() - timedelta(days=364)).strftime("%Y-%m-%d"),
    postedTo: Optional[str] = None,  # datetime.now().strftime("%Y-%m-%d"),
    active: str = "true",
    mode: str = "ALL",
):
    """Get SAM opportunities' JSON data"""
    params = {
        "q": q,
        "active": active,
        "mode": mode,
    }
    if postedFrom:
        params["modified_date.from"] = (postedFrom + "-06:00",)
    if postedTo:
        params["modified_date.to"] = (postedTo + "-06:00",)

    res = SAM.get_opportunities(params)
    print(json.dumps(res))


@sam_app.command()
def opportunity(notice_id: str):
    """Get SAM opportunity JSON data"""
    res = SAM.get_api_opportunity_by_id(notice_id)
    print(json.dumps(res))


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
    """Get SBIR solicitations"""
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
