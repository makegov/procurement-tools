import re


class UEI:
    """Utilities for working with Unique Entity Identifiers (UEIs).

    Current functionality is limited to validating a UEI.

    Typical usage::

        from procurement_tools import UEI
        UEI.is_valid("J7M9HPTGJ1S9")
    """

    @classmethod
    def is_valid(cls, uei: str) -> bool:
        """Checks validity of a UEI

        This implements the UEI standard described here: https://www.gsa.gov/about-us/organization/federal-acquisition-service/technology-transformation-services/integrated-award-environment-iae/iae-systems-information-kit/uei-technical-specifications-and-api-information
        Credit to GSA TTS's original implementation here: https://github.com/GSA-TTS/uei-js

        Args:
            uei: A UEI (e.g., "J7M9HPTGJ1S9")

        Returns:
            True or False.
        """

        def _check_digit(uei: str) -> bool:
            """Checksum"""

            def _reducer_step(m):
                return sum((i * (j + 1)) % 10 for j, i in enumerate(m))

            # Convert the first 11 digits of the UEI into an
            # array of ASCII codes for each character
            s0 = [ord(i) for i in uei[:-1]]
            res = _reducer_step(s0)

            # Run the same process again until a single digit is obtained
            while res > 9:
                res = _reducer_step([int(i) for i in str(res)])

            # Check if the computed digit is the same as the provided check digit
            return res == int(uei[-1])

        if len(uei) != 12:
            return False
        elif uei[0] == "0":
            return False
        elif "O" in uei.upper():
            return False
        elif "I" in uei.upper():
            return False
        elif re.search(r"\d{9}", uei):
            return False
        elif _check_digit(uei):
            return True
        else:
            return False
