from procurement_tools import get_entity
from typing import Optional
import typer
import json

app = typer.Typer()


@app.command()
def sam(uei: str):
    """Get a SAM entity's JSON data by providing a UEI"""
    res = get_entity({"ueiSAM": uei})
    print(res.model_dump_json())


@app.callback()
def callback():
    pass


typer_click_object = typer.main.get_command(app)
