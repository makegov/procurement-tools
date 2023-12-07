import httpx
import json
import pytest
import requests


class MockSAMEntityResponse:
    def json():
        with open("./tests/data/sam_entity_results.json", "r") as fp:
            data = json.load(fp)
        return data


@pytest.fixture
def sam_api_results(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockSAMEntityResponse

    monkeypatch.setattr(requests, "get", mock_get)


class MockUSASRecipientResponse:
    def json():
        with open("./tests/data/usaspending_recipient_profile_results.json", "r") as fp:
            data = json.load(fp)
        return data


@pytest.fixture
def usas_recipient_api_results(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockUSASRecipientResponse

    monkeypatch.setattr(httpx, "get", mock_get)


class MockUSASAwardsResponse:
    def json():
        with open("./tests/data/usaspending_awards_data.json", "r") as fp:
            data = json.load(fp)
        return data


@pytest.fixture
def usas_awards_api_results(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockUSASAwardsResponse

    monkeypatch.setattr(httpx, "post", mock_get)