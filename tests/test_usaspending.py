import pytest
from procurement_tools import USASpending


@pytest.fixture
def uei():
    return "J7M9HPTGJ1S9"


def test_convert_UEI_default(uei):
    assert (
        USASpending.convert_uei_to_hash(uei) == "bf1220c1-2373-042a-e8e1-33d5a29639d0-P"
    )


def test_convert_UEI_parent(uei):
    assert (
        USASpending.convert_uei_to_hash(uei, level="P")
        == "bf1220c1-2373-042a-e8e1-33d5a29639d0-P"
    )


def test_convert_UEI_child(uei):
    assert (
        USASpending.convert_uei_to_hash(uei, level="C")
        == "bf1220c1-2373-042a-e8e1-33d5a29639d0-C"
    )


def test_get_usaspending_URL(uei):
    """"""
    uei_hash = USASpending.convert_uei_to_hash(uei)
    assert (
        USASpending.get_usaspending_URL(uei)
        == f"https://www.usaspending.gov/recipient/{uei_hash}/latest"
    )


def test_get_recipient_profile(usas_recipient_api_results):
    res = USASpending.get_recipient_profile("J7M9HPTGJ1S9")
    assert res["name"] == "TRIWEST HEALTHCARE ALLIANCE CORP"


def test_get_latest_recipient_awards(usas_awards_api_results):
    res = USASpending.get_latest_recipient_awards("J7M9HPTGJ1S9")
    assert len(res["results"]) == 8
    assert (
        res["results"][0]["generated_internal_id"]
        == "CONT_AWD_36C10G24F0004_3600_36C10G21D0001_3600"
    )
