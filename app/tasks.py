import logging

from app.celery_app import app as celery_app
import time

logger = logging.getLogger("celery")


@celery_app.task
def example_task(x: int, y: int) -> int:
    logger.info("task starter")
    time.sleep(2)
    logger.info("task finished")
    return x + y
