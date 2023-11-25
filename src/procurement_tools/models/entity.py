from pydantic import BaseModel, ConfigDict, Field, HttpUrl
from pydantic.alias_generators import to_camel
from typing import Literal, List, Optional


class BusinessType(BaseModel):
    """Business Types (e.g., WOSB)"""

    model_config = ConfigDict(alias_generator=to_camel)

    business_type_code: str
    business_type_description: str = Field(alias="businessTypeDesc")


class SBABusinessType(BaseModel):
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
    zip_code_plus4: str
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


class Entity(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    registration: Registration = Field(default=None, alias="entityRegistration")
    core_data: Optional[EntityData] = Field(default=None, alias="coreData")
