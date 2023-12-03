from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from typing import List, Optional


class Company(BaseModel):
    """A model of a company, for use in FAR responses"""

    model_config = ConfigDict(alias_generator=to_camel)

    company_id: Optional[str] = Field(alias="id")
    name: Optional[str]
    tin: Optional[str]
    unique_entity_id: Optional[str]
    year_established: Optional[str]


class CAGE(BaseModel):
    """CAGE information about the entity's owner"""

    model_config = ConfigDict(alias_generator=to_camel)

    cage_code: Optional[str]
    ncage_code: Optional[str]
    legal_business_name: Optional[str]
    has_owner: Optional[str]
    cage_id: Optional[str] = Field(alias="id")


class Person(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    first_name: Optional[str]
    middle_initial: Optional[str]
    last_name: Optional[str]
    title: Optional[str]


class PointOfContact(Person):
    model_config = ConfigDict(alias_generator=to_camel)

    poc_id: str = Field(alias="id")
    telephone_number: Optional[str]
    extension: Optional[str]
    international_number: Optional[str]


class ArchitectExperience(BaseModel):
    ae_id: Optional[str] = Field(alias="id")
    experience_code: Optional[str]
    experience_description: Optional[str]
    annual_avg_revenue_code: Optional[str]
    annual_avg_revenue_description: Optional[str]


class DisciplineInfo(BaseModel):
    discipline_info_id: str = Field(alias="id")
    disciplineID: str
    firmNumOfEmployees: str
    branchNumOfEmployees: str
    disciplineDescription: str


class FARAnswer(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    section: Optional[str]
    question_text: Optional[str]
    answer_id: Optional[str]
    answer_text: Optional[str]
    country: Optional[str]
    company: Optional[Company]
    highest_level_owner_cage: Optional[CAGE]
    immediate_owner_cage: Optional[CAGE]
    person_details: Optional[Person]
    point_of_contact: Optional[PointOfContact]
    architect_experiences_list: List[ArchitectExperience] = Field(
        default=[], alias="architectExperiencesList"
    )
    discipline_info_list: List = Field(default=[])
    end_products_list: List = Field(default=[])
    foreign_govt_entities_list: List = Field(default=[])
    former_firms_list: List = Field(default=[])
    fsc_info_list: List = Field(default=[])
    joint_venture_companies_list: List = Field(default=[])
    labor_surplus_concerns_list: List = Field(default=[])
    naics_list: List = Field(default=[])
    predecessors_list: List = Field(default=[])
    sam_facilities_list: List = Field(default=[])
    sam_points_of_contact_list: List = Field(default=[])
    services_revenues_list: List = Field(default=[])
    software_list: List = Field(default=[])
    url_list: List = Field(default=[])
