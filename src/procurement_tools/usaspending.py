from hashlib import md5
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
