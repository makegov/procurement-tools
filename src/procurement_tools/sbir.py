from .models.sbir import AwardList, Firm, Solicitation, SolicitationList
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

    @classmethod
    def get_awards(
        cls,
        agency: str = None,
        company: str = None,
        year: int = None,
        research_institution: str = None,
    ) -> AwardList:
        """Get awards from the SBIR API

        Args:
            agency: the department/agency of record (e.g., "HHS")
            company: the company name to look up
            year: the year of the award (e.g., 2023)
            research_institution: the Research Institution (if any). E.g., ("California Institute of Technology)

        Returns:
            A list of Firm pydantic models

        """
        url = f"https://www.sbir.gov/api/awards.json?rows=1000"
        if agency:
            url += f"&agency={agency}"
        if company:
            url += f"&firm={company}"
        if year:
            url += f"&year={year}"
        if research_institution:
            url += f"&ri={research_institution}"
        res = httpx.get(url)
        awards = []
        if not res.json() == {"ERROR": "No record found."}:
            for obj in res.json():
                awards.append(Firm(**obj))
        return AwardList(results=awards)
