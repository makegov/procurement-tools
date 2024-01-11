from .models.entity import Entity
from .models.opportunities import OpportunitiesRequestParams
from .uei import UEI
from datetime import date, timedelta
import httpx
from getpass import getpass
import keyring
from random import choice
from string import digits
import os
from pydantic import BaseModel, Field, field_validator, ValidationError
import requests
from urllib.parse import urlencode

API_KEY = os.environ.get("SAM_API_KEY")
if not API_KEY:
    try:
        API_KEY = keyring.get_password("system", "sam_api_key")
    except keyring.errors.NoKeyringError:
        API_KEY = getpass(prompt="Please enter your SAM API KEY")
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


class SAM:
    """A class representing SAM.gov's entity and search capabilities

    Typical usage::

            from procurement_tools import SAM
            res = SAM.get_opportunities({"q":"Agile"})
            opportunity = res.get_api_opportunity_by_id(res["opportunitiesData"][0]["noticeId"])

    """

    def get_entity(params: dict) -> Entity:
        """Get a pydantic model of an Entity from the `SAM API <https://open.gsa.gov/api/entity-api/>`_.

        Typical usage::

            from procurement_tools import SAM
            res = SAM.get_entity({ueiSAM:"XRVFU3YRA2U5"})

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

        BASE_URL = (
            f"https://api.sam.gov/entity-information/v3/entities?api_key={API_KEY}"
        )

        param_str = urlencode(request_params)
        url = f"{BASE_URL}&{param_str}"
        res = requests.get(url)
        data = res.json()
        return Entity(**data["entityData"][0])

    def get_opportunities(params: dict) -> dict:
        """
        Get a list of opportunities from SAM.gov using keyword search.

        Typical usage::

            from procurement_tools import SAM
            res = SAM.get_opportunities({"q":"Agile"})

        Args:
            params: A dict that includes a query (e.g., {"q":"Agile"}) and optionally other search parameters.

        Returns:
            A dict of the search results
        """
        seed = "".join(choice(digits) for i in range(13))
        mode = params.get("mode", "ALL")
        active = params.get("active", "true")
        BASE_URL = f"https://sam.gov/api/prod/sgs/v1/search/?random={seed}&index=opp&page=0&sort=-modifiedDate&size=1000&mode=search&responseType=json&qMode={mode}&is_active={active}"

        param_str = urlencode(params)
        url = f"{BASE_URL}&{param_str}"
        res = httpx.get(url)
        data = res.json()
        return data

    def get_api_opportunities(params: dict) -> dict:
        """Get a JSON of an opportunity from the `SAM API <https://open.gsa.gov/api/get-opportunities-public-api>`_.

        Typical usage::

            from procurement_tools import SAM
            res = SAM.get_api_opportunities({"postedFrom":"12/14/2023", "postedTo": "12/14/2023", "limit": 1000})

        Args:
            params: A dict for the request parameters to the SAM API. As currently implemented, we use \
            OpportunitiesRequestParams to check whether the parameters are valid.

        Returns:
            A dict
        """

        try:
            request_params = OpportunitiesRequestParams(**params).model_dump(
                exclude_none=True
            )
        except ValidationError:
            raise

        BASE_URL = f"https://api.sam.gov/opportunities/v2/search?api_key={API_KEY}"

        param_str = urlencode(request_params)
        url = f"{BASE_URL}&{param_str}"
        res = httpx.get(url)
        data = res.json()
        return data

    def get_api_opportunity_by_id(notice_id: str) -> dict:
        """Get a JSON of a specific opportunity from the `SAM API <https://open.gsa.gov/api/get-opportunities-public-api>`_.

        Typical usage::

            from procurement_tools import SAM
            res = SAM.get_api_opportunity_by_id("f2483be142e64eeabcc5fba2f8992251")

        Args:
            notice_id: The SAM notice unique identifier.

        Returns:
            A dict
        """

        TODAY = date.today()
        YEAR_AGO = TODAY - timedelta(days=364)
        url = f"https://api.sam.gov/opportunities/v2/search?api_key={API_KEY}&postedFrom={YEAR_AGO.strftime('%m/%d/%Y')}&postedTo={TODAY.strftime('%m/%d/%Y')}&noticeid={notice_id}&limit=1"
        res = httpx.get(url)
        data = res.json()
        return data
