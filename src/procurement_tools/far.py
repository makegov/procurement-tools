from .models.far_clause import Clause
from io import StringIO
import requests
import textwrap
import unicodedata
from lxml import html
from lxml import etree
from lxml.html.clean import clean_html

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
            tree = html.parse(StringIO(textwrap.dedent(res.text)), parser)
            body = "".join(tree.xpath("//div[contains(@class,'body')]//text()")).strip()
            return Clause(
                title=tree.xpath("//title")[0].text,
                number=tree.xpath("//h1")[0].cssselect("span")[0].text,
                body=unicodedata.normalize("NFKD", body),
            )
