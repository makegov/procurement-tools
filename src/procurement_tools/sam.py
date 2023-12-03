from .models.entity import Entity
from .uei import UEI
import keyring
import os
from pydantic import BaseModel, Field, field_validator, ValidationError
import requests
from urllib.parse import urlencode

API_KEY = os.environ.get("SAM_API_KEY")
if not API_KEY:
    API_KEY = keyring.get_password("system", "sam_api_key")
BASE_URL = f"https://api.sam.gov/entity-information/v3/entities?api_key={API_KEY}"


class EntityRequestParams(BaseModel):
    """Query Parameters for a SAM API Request"""

    ueiSAM: str = None
    naicsCode: str = None
    includeSections: str = Field(default="All")

    @field_validator("ueiSAM")
    @classmethod
    def uei_is_valid(cls, uei: str) -> str:
        if UEI.is_valid(uei):
            return uei
        raise ValueError("UEI is not valid!")


def get_entity(params: dict) -> Entity:
    """Get a pydantic model of an Entity from the `SAM API <https://open.gsa.gov/api/entity-api/>`_.

    Typical usage::

        from procurement_tools import get_entity
        res = get_entity({ueiSAM:"XRVFU3YRA2U5"})

    Args:
        params: A dict for the request parameters to the SAM API. As currently implemented, we use \
        EntityRequestParams to check whether the parameters are valid. This is limited to `ueiSAM` and \
        `includeSections`

    Returns:
        A pydantic Entity modle
    """
    try:
        request_params = EntityRequestParams(**params).model_dump(exclude_none=True)
    except ValidationError:
        raise

    param_str = urlencode(request_params)
    url = f"{BASE_URL}&{param_str}"
    res = requests.get(url)
    data = res.json()
    return Entity(**data["entityData"][0])
