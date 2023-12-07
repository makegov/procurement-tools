from datetime import date, timedelta
from hashlib import md5
import httpx
import uuid


class USASpending:
    """Utilities for working with USASpending.gov.

    Current functionality is limited to converting a UEI to a USASpending.gov
    recipient profile hash and getting an entity's URL from a URL.

    Typical usage::

        from procurement_tools import USASpending
        USASpending.convert_uei_to_hash("J7M9HPTGJ1S9")
    """

    @classmethod
    def convert_uei_to_hash(cls, uei: str, level: str = "P") -> str:
        """Convert a UEI into a Hash for USASpending.gov

        Args:
            uei: A UEI for conversion
            level: The entity level (i.e., a Parent "P" or a Child "C"). Defaults to Parent.

        Returns:
            The USASpending recipient hash
        """
        uei_string = ("uei-" + uei).upper()
        m = md5(bytes(uei_string.encode()))
        return f"{str(uuid.UUID(m.hexdigest()))}-{level}"

    @classmethod
    def get_usaspending_URL(cls, uei: str, level: str = "P") -> str:
        """Gets a USASpending.gov URL for an entity

        Args:
            uei: The entity's UEI
            level: The entity level (i.e., a Parent "P" or a Child "C"). Defaults to Parent.

        Returns:
            The USASpending.gov URL
        """
        uei_hash = cls.convert_uei_to_hash(uei, level)
        return f"https://www.usaspending.gov/recipient/{uei_hash}/latest"

    @classmethod
    def get_recipient_profile(
        cls, uei: str, level: str = "P", year: int = None
    ) -> dict:
        """Gets a recipient profile from USASpending's `recipient API endpoint <https://github.com/fedspendingtransparency/usaspending-api/blob/master/usaspending_api/api_contracts/contracts/v2/recipient/recipient_id.md>`_.

        Args:
            uei: The entity's UEI
            level: The entity level (i.e., a Parent "P" or a Child "C"). Defaults to Parent.

        Returns:
            The USASpending.gov recipient profile page data
        """
        recipient_hash = cls.convert_uei_to_hash(uei, level)
        url = f"https://api.usaspending.gov/api/v2/recipient/{recipient_hash}/"
        if year:
            url += "?year={year}"
        res = httpx.get(url)
        return res.json()

    @classmethod
    def get_latest_recipient_awards(cls, uei: str) -> dict:
        """Gets the most recent 10 awards within the last 90 days from USASpending's `spending by award API endpoint <https://github.com/fedspendingtransparency/usaspending-api/blob/master/usaspending_api/api_contracts/contracts/v2/search/spending_by_award.md>`_.

        Args:
            uei: The entity's UEI

        Returns:
            The USASpending.gov awards data
        """
        end_date = date.today()
        start_date = end_date - timedelta(days=90)
        data = dict(
            filters={
                "time_period": [
                    {
                        "start_date": start_date.strftime("%Y-%m-%d"),
                        "end_date": end_date.strftime("%Y-%m-%d"),
                        "date_type": "new_awards_only",
                    },
                ],
                "recipient_search_text": [uei],
                "award_type_codes": [
                    "A",
                    "B",
                    "C",
                    "D",
                ],
            },
            fields=[
                "Award ID",
                "Recipient Name",
                "Start Date",
                "End Date",
                "Award Amount",
                "Description",
                "Awarding Agency",
                "Awarding Sub Agency",
                "Funding Agency",
                "Funding Sub Agency",
                "Contract Award Type",
            ],
            limit=10,
        )
        url = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
        res = httpx.post(url, json=data).json()
        return res
