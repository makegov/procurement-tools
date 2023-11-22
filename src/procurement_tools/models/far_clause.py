from pydantic import BaseModel, HttpUrl, computed_field
from typing import List


class Clause(BaseModel):
    number: str
    title: str
    body: str

    @computed_field
    @property
    def url(self) -> HttpUrl:
        return f"https://www.acquisition.gov/far/{self.number}"


class Subpart(BaseModel):
    number: str
    title: str
    clauses: List[Clause]

    @computed_field
    @property
    def url(self) -> HttpUrl:
        return f"https://www.acquisition.gov/far/{self.number}"
