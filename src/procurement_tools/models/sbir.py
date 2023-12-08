from pydantic import BaseModel
from typing import List, Optional


class Firm(BaseModel):
    """The firm that won a SBIR award"""

    firm: Optional[str]
    award_title: str
    agency: str
    branch: str
    phase: str
    program: str
    agency_tracking_number: str
    contract: str
    proposal_award_date: str
    contract_end_date: str
    solicitation_number: str
    solicitation_year: str
    topic_code: str
    award_year: str
    award_amount: str
    duns: str
    hubzone_owned: str
    socially_economically_disadvantaged: str
    women_owned: str
    number_employees: str
    company_url: str
    address1: str
    address2: str
    city: str
    state: str
    zip: str
    poc_name: str
    poc_title: str
    poc_phone: str
    poc_email: str
    pi_name: str
    pi_title: str
    pi_phone: str
    pi_email: str
    ri_name: Optional[str]
    ri_poc_name: Optional[str]
    ri_poc_phone: Optional[str]
    abstract: str
    award_link: str


class AwardList(BaseModel):
    results: List[Firm]


class Subtopic(BaseModel):
    """A SBIR subtopic"""

    subtopic_title: str
    branch: str
    subtopic_number: str
    subtopic_description: str
    sbir_subtopic_link: str


class Topic(BaseModel):
    """A SBIR topic"""

    topic_title: str
    branch: str
    topic_number: str
    topic_description: str
    sbir_topic_link: str
    subtopics: List[Subtopic]


class Solicitation(BaseModel):
    """A SBIR solicitation"""

    solicitation_title: str
    solicitation_number: str
    program: str
    phase: str
    agency: str
    branch: str
    solicitation_year: str
    release_date: str
    open_date: str
    close_date: str
    application_due_date: List[str]
    sbir_solicitation_link: str
    solicitation_agency_url: str
    current_status: str
    solicitation_topics: List[Topic]


class SolicitationList(BaseModel):
    """A list of SBIR solicitations"""

    results: List[Solicitation]
