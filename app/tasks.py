from celery.utils.log import get_task_logger

from app.celery_app import app as celery_app
import time

logger = get_task_logger("celery_tasks")


@celery_app.task
def example_task(x: int, y: int) -> int:
    logger.info("task starter")
    time.sleep(2)
    logger.info("task finished")
    return x + y
