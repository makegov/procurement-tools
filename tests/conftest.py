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
