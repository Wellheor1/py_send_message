import logging
import os
import subprocess

from celery import Celery
from app.redis_client import create_redis_url

logger = logging.getLogger("uvicorn.error")

redis_url = create_redis_url()
app = Celery(
    "py_send_message", broker=redis_url, backend=redis_url, include=["app.tasks"]
)

# Настройки Celery
app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

celery_worker_process = None


def start_worker():
    global celery_worker_process
    celery_worker_process = subprocess.Popen(
        ["celery", "-A", "app.celery_app", "worker", "--loglevel=info"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=os.environ.copy(),
    )
    logger.info("Worker celery started")


def stop_worker():
    global celery_worker_process
    if celery_worker_process:
        celery_worker_process.terminate()
        logger.info("Worker celery stopped")
