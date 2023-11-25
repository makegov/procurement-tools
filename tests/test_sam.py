import json
import pytest
import requests
from procurement_tools.models.entity import Entity
from procurement_tools.sam import EntityRequestParams, get_entity


@pytest.fixture()
def sam_results():
    with open("./tests/data/sam_results.json", "r") as fp:
        data = json.load(fp)
    return data


def test_entity_model(sam_results):
    ent = Entity(**sam_results["entityData"][0])
    assert ent.registration.uei == "XRVFU3YRA2U5"


class MockSAMEntityResponse:
    def json():
        with open("./tests/data/sam_entity_results.json", "r") as fp:
            data = json.load(fp)
        return data


class MockSAMExpandedEntityResponse:
    def json():
        with open("./tests/data/sam_results_expanded.json", "r") as fp:
            data = json.load(fp)
        return data


def test_get_entity(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockSAMEntityResponse

    monkeypatch.setattr(requests, "get", mock_get)
    res = get_entity(EntityRequestParams(ueiSAM="XRVFU3YRA2U5"))
    assert res.registration.dba_name == "JAMES & ENYART"

    # Test check for invalid UEI
    with pytest.raises(ValueError) as error:
        get_entity(EntityRequestParams(ueiSAM="XRVFU3YRA2U5#$"))
    assert "UEI is not valid!" in str(error.value)


def test_get_entity_expanded(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockSAMExpandedEntityResponse

    monkeypatch.setattr(requests, "get", mock_get)
    res = get_entity(EntityRequestParams(ueiSAM="XRVFU3YRA2U5"))
    assert res.registration.dba_name == "JAMES & ENYART"
    assert res.core_data.business_types.businessTypeList[0].business_type_code == "2X"
