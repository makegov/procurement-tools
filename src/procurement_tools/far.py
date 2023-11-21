from .models.far_clause import Clause
from bs4 import BeautifulSoup
from io import StringIO
import requests
import textwrap
import unicodedata
from lxml import etree, html
from lxml.html.soupparser import fromstring

"""

https://www.acquisition.gov/content/developers-page
https://github.com/gsa/GSA-Acquisition-FAR/
"""


class FAR:
    def get_section(section_number: str):
        URL = f"https://raw.githubusercontent.com/GSA/GSA-Acquisition-FAR/master/html/copypaste-AllTopic/{section_number}.html"
        res = requests.get(URL)
        if res.status_code == 200:
            parser = etree.HTMLParser(remove_blank_text=True)
            tree = html.parse(
                StringIO(textwrap.shorten(res.text, len(res.text))), parser
            )
            body = tree.xpath("//div[contains(@class,'body')]")[0]
            soup = BeautifulSoup(etree.tostring(body), "html.parser")
            text = "\n".join(
                [
                    para.get_text(strip=True, separator=" ")
                    for para in soup.find_all("p")
                    if para.get_text(strip=True)
                ]
            )
            return Clause(
                title=tree.xpath("//title")[0].text,
                number=tree.xpath("//h1")[0].cssselect("span")[0].text,
                body=text,
            )
