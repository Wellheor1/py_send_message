from celery import Celery
from app.redis_client import create_redis_url

redis_url = create_redis_url()
app = Celery("myapp", broker=redis_url, backend=redis_url, include=["tasks"])

# Настройки Celery
app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
