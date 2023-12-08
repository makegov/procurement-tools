from pydantic import BaseModel
from typing import List


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
