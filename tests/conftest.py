import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app
from tests.test_settings import BEARER_TOKEN


@pytest.fixture
def test_settings():
    class TestSettings:
        BEARER_TOKEN = BEARER_TOKEN

    return TestSettings()


@pytest.fixture
def client(test_settings):
    with patch("app.settings", test_settings):
        yield TestClient(app)
