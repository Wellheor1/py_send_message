import pytest
from fastapi.testclient import TestClient


@pytest.mark.asyncio
async def test_non_token(client: TestClient):
    response = client.get("/")
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_invalid_token(client: TestClient):
    headers = {"authorization": "Bearer 434324"}
    response = client.get("/", headers=headers)
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_valid_token(client: TestClient, test_settings):
    headers = {"authorization": f"Bearer {test_settings.BEARER_TOKEN}"}
    response = client.get("/", headers=headers)
    assert response.status_code == 200
