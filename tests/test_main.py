import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.settings import BEARER_TOKEN

client = TestClient(app)


@pytest.mark.asyncio
async def test_non_token():
    response = client.get("/")
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_invalid_token():
    headers = {"authorization": "Bearer 434324"}
    response = client.get("/", headers=headers)
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_valid_token():
    headers = {"authorization": f"Bearer {BEARER_TOKEN}"}
    response = client.get("/", headers=headers)
    assert response.status_code == 200
