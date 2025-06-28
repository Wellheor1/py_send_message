import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_send_message():
    response = client.get("/")
    assert response.status_code == 200


# @pytest.mark.asyncio
# async def test_send_message_empty():
#     response = client.get("/3rkjjk")
#     assert response.status_code == 422  # Ожидаем ошибку валидации
