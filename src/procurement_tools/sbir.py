from .models.sbir import Solicitation, SolicitationList
import httpx
from typing import List


class SBIR:
    """Utilities for accessing information about SBIRs.

    Typical usage::

        from procurement_tools import SBIR
        SBIR.get_solicitations(keyword="water")
    """

    @classmethod
    def get_solicitations(
        cls, keyword: str = None, agency: str = None, open: int = 1
    ) -> SolicitationList:
        """Get solicitations from the SBIR API

        Args:
            keyword: a keyword to look up in the solicitation
            agency: the department/agency of record
            open: 1 or 0 (defaults to open)
        Returns:
            A list of Solicitation pydantic models

        """
        url = f"https://www.sbir.gov/api/solicitations.json?open={open}"
        res = httpx.get(url)
        solicitations = []
        if not res.json() == {"ERROR": "No record found."}:
            for obj in res.json():
                solicitation = Solicitation(**obj)
                if agency and agency not in solicitation.agency:
                    continue
                if not keyword:
                    solicitations.append(solicitation)
                elif keyword in solicitation.model_dump_json():
                    solicitations.append(solicitation)
                else:
                    continue
        return SolicitationList(results=solicitations)
