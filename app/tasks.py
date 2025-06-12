from app.celery_app import app as celery_app
import time


@celery_app.task
def example_task(x: int, y: int) -> int:
    time.sleep(2)  # Симуляция долгой задачи
    return x + y
