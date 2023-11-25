from .models.entity import Entity
from .uei import UEI
import keyring
from pydantic import BaseModel, Field, field_validator
import requests
from urllib.parse import urlencode


API_KEY = keyring.get_password("system", "sam_api_key")
BASE_URL = f"https://api.sam.gov/entity-information/v3/entities?api_key={API_KEY}"


class EntityRequestParams(BaseModel):
    """Query Parameters for a SAM API Request"""

    ueiSAM: str = None
    naicsCode: str = None
    includeSections: str = Field(default="entityRegistration")

    @field_validator("ueiSAM")
    @classmethod
    def uei_is_valid(cls, uei: str) -> str:
        if UEI.is_valid(uei):
            return uei
        raise ValueError("UEI is not valid!")


def get_entity(params: EntityRequestParams) -> Entity:
    """Get a pydantic model of an Entity from the `SAM API <https://open.gsa.gov/api/entity-api/>`_.

    Args:
        params: An EntityRequestParams object

    Returns:
        A pydantic Entity modle
    """

    param_str = urlencode(params.model_dump(exclude_none=True))
    url = f"{BASE_URL}&{param_str}"
    res = requests.get(url)
    data = res.json()
    return Entity(**data["entityData"][0])
