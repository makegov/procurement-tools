from .models.far_clause import Clause, Subpart
from bs4 import BeautifulSoup
from io import StringIO
import requests
import textwrap
from typing import List
import unicodedata


class FAR:
    """Utilities for accessing the Federal Acquisition Regulation.

    Current functionality is limited to looking up a section or a subpart, but
    it may eventually do other things. One cool thing is that now you can
    programmatically access a FAR section as a dict/in json.

    Typical usage::

        from procurement_tools import FAR
        FAR.get_section("17.502-1")

    Note that the source of FAR data comes from https://github.com/gsa/GSA-Acquisition-FAR/.
    """

    @classmethod
    def get_section(cls, section_number: str) -> Clause:
        """Lookup a FAR section.

        Args:
            section_number: A FAR section number (e.g., "17.502-1")

        Returns:
            A FAR Clause.
        """
        URL = f"https://raw.githubusercontent.com/GSA/GSA-Acquisition-FAR/master/html/copypaste-AllTopic/{section_number}.html"
        res = requests.get(URL)
        if res.status_code == 200:
            soup = BeautifulSoup(
                StringIO(textwrap.shorten(res.text, len(res.text))), "html.parser"
            )
            text = "\n".join(
                [
                    para.get_text(strip=True, separator=" ")
                    for para in soup.find_all("p")
                    if para.get_text(strip=True)
                ]
            )
            return Clause(
                title=soup.title.text,
                number=soup.find("h1").span.text,
                body=text,
            )
        else:
            raise ValueError(
                f"Section '{section_number}' does not appear to be a valid FAR section"
            )

    @classmethod
    def get_subpart(cls, subpart_number: str) -> Subpart:
        """Lookup a FAR subpart.

        Args:
            subpart_number: A FAR subpart number (e.g. "17.5").

        Returns:
            A FAR Subpart.
        """

        def parse_clauses(soup: BeautifulSoup) -> List[Clause]:
            results = []
            sections = soup.find_all("article", class_="topic")
            for section in sections:
                if "nested2" in section.attrs["class"]:
                    continue
                if section:
                    clause = Clause(
                        number=section.find("h2").span.text,
                        title=section.find("h2").text.strip(),
                        body=unicodedata.normalize(
                            "NFKD", section.get_text(separator=" ", strip=True)
                        ),
                    )
                    results.append(clause)
            return results

        subpart_number = subpart_number.replace(".", "_")
        URL = f"https://raw.githubusercontent.com/GSA/GSA-Acquisition-FAR/master/html/copypaste-SubParts/FAR_Subpart_{subpart_number}.html"
        res = requests.get(URL)
        if res.status_code == 200:
            soup = BeautifulSoup(
                StringIO(textwrap.shorten(res.text, len(res.text))), "html.parser"
            )
            return Subpart(
                title=soup.title.text,
                number=soup.find("h1").span.text,
                clauses=parse_clauses(soup),
            )
        else:
            raise ValueError(
                f"Subpart '{subpart_number}' does not appear to be a valid FAR subpart"
            )
