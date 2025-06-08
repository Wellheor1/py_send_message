from celery_app import app
import time


@app.task
def example_task(x: int, y: int) -> int:
    time.sleep(2)  # Симуляция долгой задачи
    return x + y
