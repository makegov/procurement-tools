from bs4 import BeautifulSoup
import httpx
import json
import os
import random
import re

with open(
    os.path.join(
        os.path.dirname(__file__),
        "data/periodic_table.json",
    ),
    "r",
) as fp:
    INNOVATIONS = json.load(fp)


class PeriodicTable:
    """
    Utilities using the `FAI Periodic Table of Acquisition
    Innovation <https://www.fai.gov/periodic-table>`_.


    Typical usage::

        from procurement_tools import PeriodicTable
        PeriodicTable.get_random_innovation()

    """

    innovations = INNOVATIONS

    @classmethod
    def get_random_innovation(cls) -> dict:
        """Gets a random innovation from the Table.

        Returns:
            A dict with an innovation.
        """
        idx = random.randint(0, len(cls.innovations) - 1)
        return cls.innovations[idx]

    @staticmethod
    def create_data() -> dict:
        """Create a dict with the FAI Periodic Table of Acquisition Innovation elements

        :meta private:
        """
        req = httpx.get("https://www.fai.gov/periodic-table")
        soup = BeautifulSoup(req, "html.parser")

        results = []

        columns = soup.find_all(class_="pt-card")
        for column in columns:
            res = re.split(r"\n\s+\n", column.find(class_="cardTitle").get_text())
            column_title = res[0]
            # column_subtitle = res[1]
            tiles = column.find_all(class_="tile")
            for tile in tiles:
                title = tile.find(class_="views-field-title").get_text().strip()
                sections = [
                    elem.get_text() for elem in tile.find_all(class_="popup-subtitle")
                ]
                description = sections[0]
                problems_solved = sections[1]
                benefits = sections[2]
                results.append(
                    dict(
                        column_title=column_title,
                        title=title,
                        description=description,
                        problems_solved=problems_solved,
                        benefits=benefits,
                    )
                )
        return results
