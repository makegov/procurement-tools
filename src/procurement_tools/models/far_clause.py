from datetime import datetime
from pydantic import BaseModel, HttpUrl, computed_field


class Clause(BaseModel):
    number: str
    title: str
    body: str

    @computed_field
    @property
    def url(self) -> HttpUrl:
        return f"https://www.acquisition.gov/far/{self.number}"
