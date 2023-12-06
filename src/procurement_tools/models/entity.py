from pydantic import BaseModel, ConfigDict, Field, HttpUrl
from pydantic.alias_generators import to_camel
from typing import Literal, List, Optional, Union
from .sam_entity.far_answer import FARAnswer


class BusinessType(BaseModel):
    """Business Types (e.g., WOSB)"""

    model_config = ConfigDict(alias_generator=to_camel)

    business_type_code: str
    business_type_description: str = Field(alias="businessTypeDesc")


class SBABusinessType(BaseModel):
    """SBA certifications (e.g., 8(a))"""

    model_config = ConfigDict(alias_generator=to_camel)

    sba_business_type_code: Optional[str]
    sba_business_type_description: Optional[str] = Field(alias="sbaBusinessTypeDesc")
    certification_entry_date: Optional[str]
    certification_exit_date: Optional[str]


class Registration(BaseModel):
    """Basic registration information for an entity"""

    model_config = ConfigDict(populate_by_name=True)

    registered: Literal["Yes", "No"] = Field(alias="samRegistered")
    uei: str = Field(alias="ueiSAM")
    eft: Optional[str] = Field(alias="entityEFTIndicator")
    cage: Optional[str] = Field(alias="cageCode")
    dodaac: Optional[str]
    legal_name: str = Field(alias="legalBusinessName")
    dba_name: Optional[str] = Field(alias="dbaName")
    purpose_code: str = Field(alias="purposeOfRegistrationCode")
    purpose_description: str = Field(alias="purposeOfRegistrationDesc")
    status: str = Field(alias="registrationStatus")
    evs_source: str = Field(alias="evsSource")
    registration_date: str = Field(alias="registrationDate")
    last_update_date: str = Field(alias="lastUpdateDate")
    expiration_date: str = Field(alias="registrationExpirationDate")
    activation_date: str = Field(alias="activationDate")
    uei_status: str = Field(alias="ueiStatus")
    uei_expiration_date: Optional[str] = Field(alias="ueiExpirationDate")
    uei_creation_date: str = Field(alias="ueiCreationDate")
    public_display_flag: str = Field(alias="publicDisplayFlag")
    exclusion_status_flag: str = Field(alias="exclusionStatusFlag")
    exclusion_url: Optional[HttpUrl] = Field(alias="exclusionURL")
    dun_bradstreet_open_data: Optional[str] = Field(alias="dnbOpenData")


class Address(BaseModel):
    """Generic address object, used in multiple places"""

    model_config = ConfigDict(alias_generator=to_camel)

    address_line1: str
    address_line2: Optional[str]
    city: str
    state_or_province_code: str
    zip_code: str
    zip_code_plus4: Optional[str]
    country_code: str


class EntityInformation(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    entity_url: Optional[str] = Field(alias="entityURL")
    entity_division_name: Optional[str]
    entity_division_number: Optional[str]
    entity_start_date: str
    fiscal_year_end_close_date: str
    submission_date: str


class EntityGeneralInformation(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    entity_structure_code: str
    entity_structure_description: str = Field(alias="entityStructureDesc")
    entity_type_code: str
    entity_type_description: str = Field(alias="entityTypeDesc")
    profit_structure_code: str
    profit_structure_description: str = Field(alias="entityTypeDesc")
    organization_structure_code: Optional[str]
    organization_structure_description: Optional[str] = Field(
        alias="organizationStructureDesc"
    )
    state_of_incorporation_code: str
    state_of_incorporation_description: str = Field(alias="stateOfIncorporationDesc")
    country_of_incorporation_code: str
    country_of_incorporation_description: str = Field(
        alias="countryOfIncorporationDesc"
    )


class FinancialInformation(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    credit_card_usage: str
    debt_subject_to_offset: str


class BusinessTypes(BaseModel):
    businessTypeList: List[BusinessType]
    sbaBusinessTypeList: List[SBABusinessType]


class EntityData(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    entity_information: EntityInformation
    physical_address: Address
    mailing_address: Address
    congressional_district: str
    general_information: EntityGeneralInformation
    business_types: BusinessTypes
    financial_information: FinancialInformation


class Naics(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    naics_code: str
    naics_description: str
    sba_small_business: Optional[str]
    naics_exception: Optional[str]


class ProductServiceCode(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    psc_code: Optional[str]
    psc_description: Optional[str]


class GoodsAndServices(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    primary_naics: Optional[str]
    naics_list: List[Naics]
    psc_list: List[ProductServiceCode]


class GeographicalAreaServed(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    geographical_area_served_state_code: Optional[str]
    geographical_area_served_state_name: Optional[str]
    geographical_area_served_county_code: Optional[str]
    geographical_area_served_county_name: Optional[str]
    geographical_area_servedmetropolitan_statistical_area_code: Optional[str]
    geographical_area_servedmetropolitan_statistical_area_name: Optional[str]


class DisasterReliefData(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    disaster_registry_flag: str
    bonding_flag: str
    geographical_area_served: List[GeographicalAreaServed]


class EdiInformation(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    edi_information_flag: str


class AssertionData(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    goods_and_services: GoodsAndServices
    disaster_relief_data: DisasterReliefData
    edi_information: EdiInformation


class FARResponse(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    provision_id: str
    list_of_answers: List[FARAnswer]


class Certifications(BaseModel):
    fARResponses: List[FARResponse]
    dFARResponses: List[FARResponse]


class FinancialAssistanceCertifications(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    grants_certification_status: Optional[str]
    grants_certifying_response: Optional[str]
    certifier_first_name: Optional[str]
    certifier_last_name: Optional[str]
    certifier_middle_initial: Optional[str]


class PDFLinks(BaseModel):
    far_pdf: str = Field(alias="farPDF")
    far_and_dfars_pdf: str = Field(alias="farAndDfarsPDF")
    architect_engineering_pdf: Optional[str] = Field(alias="architectEngineeringPDF")
    financial_assistance_certifications_pdf: Optional[str] = Field(
        alias="financialAssistanceCertificationsPDF"
    )


class Qualifications(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    architect_engineer_responses: Optional[FARResponse]


class RepsAndCerts(BaseModel):
    certifications: Certifications
    qualifications: Qualifications
    financial_assistance_certifications: FinancialAssistanceCertifications = Field(
        alias="financialAssistanceCertifications"
    )
    pdf_links: PDFLinks = Field(alias="pdfLinks")


class EntitySummary(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    uei: str = Field(default=None, alias="ueiSAM")
    cage_code: str
    legal_business_name: str
    physical_address: Address


class Proceeding(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    proceeding_date: Optional[str]
    instrument_number: Optional[str]
    instrument: Optional[str]
    proceeding_state_code: Optional[str]
    proceeding_type: Optional[str]
    disposition: Optional[str]
    proceeding_description: Optional[str]


class POC(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    first_name: Optional[str]
    middle_initial: Optional[str]
    last_name: Optional[str]
    title: Optional[str]
    address_line1: Optional[str]
    address_line2: Optional[str]
    city: Optional[str]
    state_or_province_code: Optional[str]
    zip_code: Optional[str]
    zip_code_plus4: Optional[str]
    country_code: Optional[str]


class ProceedingsPointsOfContact(BaseModel):
    proceedingsPOC: Optional[POC]
    proceedingsAlternatePOC: Optional[POC]


class ProceedingsData(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    proceedings_question1: Optional[str]
    proceedings_question2: Optional[str]
    proceedings_question3: Optional[str]
    proceedings_record_count: Optional[Union[str, int]]
    list_of_proceedings: List[Proceeding]
    proceedings_points_of_contact: Optional[ProceedingsPointsOfContact]


class ResponsibilityInformation(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    record_type: Optional[str]
    record_type_desc: Optional[str]
    record_date: Optional[str]
    procurement_id_or_federal_assistance_id: Optional[str]
    reference_idv_piid: Optional[str]
    attachment: Optional[str]


class CorporateIntegrity(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    legal_business_name: Optional[str]
    cage_code: Optional[str]
    integrity_records: Optional[str]


class CorporateRelationships(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    highest_owner: Optional[CorporateIntegrity]
    immediate_owner: Optional[CorporateIntegrity]
    predecessors_list: Optional[List[CorporateIntegrity]]


class IntegrityInformation(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    entity_summary: Optional[EntitySummary]
    proceedings_data: Optional[ProceedingsData]
    responsibility_information_count: Union[str, int]
    responsibility_information_list: Optional[List[ResponsibilityInformation]]
    corporate_relationships: Optional[CorporateRelationships]


class POCData(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    government_business_POC: Optional[POC] = Field(alias="governmentBusinessPOC")
    electronic_business_POC: Optional[POC] = Field(alias="electronicBusinessPOC")
    government_business_alternate_POC: Optional[POC] = Field(
        alias="governmentBusinessAlternatePOC"
    )
    electronic_business_alternate_POC: Optional[POC] = Field(
        alias="electronicBusinessAlternatePOC"
    )
    past_performance_POC: Optional[POC] = Field(alias="pastPerformancePOC")
    past_performance_alternate_POC: Optional[POC] = Field(
        alias="pastPerformanceAlternatePOC"
    )


class Entity(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    registration: Registration = Field(default=None, alias="entityRegistration")
    core_data: Optional[EntityData] = Field(default=None, alias="coreData")
    integrity_information: Optional[IntegrityInformation] = Field(
        default=None, alias="integrityInformation"
    )
    assertions: Optional[AssertionData] = Field(default=None, alias="assertions")
    reps_and_certs: Optional[RepsAndCerts] = Field(default=None, alias="repsAndCerts")
    points_of_contact: Optional[POCData] = Field(default=None, alias="pointsOfContact")
