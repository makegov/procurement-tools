from .models.far_clause import Clause, Subpart
from bs4 import BeautifulSoup
from io import StringIO
import requests
import textwrap
from typing import List
import unicodedata

"""
Official source of FAR data comes from https://github.com/gsa/GSA-Acquisition-FAR/.
An alternative is to use the CFR, but for now, we're going to use the GSA Github.
"""


class FAR:
    def get_section(section_number: str):
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

    def get_subpart(subpart_number: str):
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
