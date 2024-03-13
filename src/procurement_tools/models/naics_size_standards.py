from pydantic import BaseModel, Field
from typing import Optional


class Sector(BaseModel):
    id: int
    description: str


class Subsector(BaseModel):
    id: int
    description: str


class NaicsSizeStandard(BaseModel):
    code: int | str
    description: str
    sector: Sector
    subsector: Subsector
    revenue_limit: Optional[float] = None
    employee_limit: Optional[int] = None
    footnote: Optional[str] = None
    parent: Optional[int | str] = None
    asset_limit: Optional[int] = None
