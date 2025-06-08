import json
import logging

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse

from app.auth.main import verify_bearer_token_v2
from app.redis_client import init_redis, close_redis, get_redis
from app.celery_app import (
    app as celery_app,
    start_worker as start_celery_worker,
    stop_worker as stop_celery_worker,
)
from app.tasks import example_task
from app.router.mail import router as mail_router
from app.router.slog import router as slog_router
from app.settings import MODULES
from app.mail.utils import check_settings as mail_check_settings
from app.utils import check_settings as main_check_settings

logger = logging.getLogger("uvicorn.error")

app = FastAPI(dependencies=[Depends(verify_bearer_token_v2)])

main_check_settings()

celery_worker_process = None


@app.on_event("startup")
def startup_event():
    init_redis()
    start_celery_worker()


@app.on_event("shutdown")
def shutdown_event():
    close_redis()
    stop_celery_worker()


@app.get("/", tags=["Приложение"], summary="Проверка работоспособности приложения")
async def root():
    result = []
    return JSONResponse({"ok": True, "message": "Hello World Well", "result": result})


@app.post(
    "/cache/store",
    tags=["Приложение"],
    summary="Проверка работоспособности redis",
)
def store_in_cache(key: str, value: dict, ttl: int = 60):
    try:
        r = get_redis()
        serialized_value = json.dumps(value)
        r.setex(key, ttl, serialized_value)
        return {"message": f"Data stored in cache with key {key} for {ttl} seconds"}
    except Exception as e:
        return HTTPException(
            status_code=500, detail=f"Failed to store in cache: {str(e)}"
        )


@app.get(
    "/cache/retrieve", tags=["Приложение"], summary="Проверка работоспособности redis"
)
def retrieve_from_cache(key: str):
    try:
        r = get_redis()
        cached_value = r.get(key)
        print(cached_value)
        if not cached_value:
            return HTTPException(status_code=404, detail="Key not found in cache")
        return json.loads(cached_value)
    except Exception as e:
        return HTTPException(
            status_code=500, detail=f"Failed to retrieve from cache: {str(e)}"
        )


@app.post(
    "/celery/add-task", tags=["Приложение"], summary="Проверка работоспособности celery"
)
def start_task(x: int, y: int):
    try:
        task = example_task.delay(x, y)
        return {"task_id": task.id, "status": "Task started"}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Failed to start task: {str(e)}")


@app.get(
    "/celery/task-status",
    tags=["Приложение"],
    summary="Проверка работоспособности celery",
)
def get_task_status(task_id: str):
    try:
        task = celery_app.AsyncResult(task_id)
        if task.state == "PENDING":
            return {"task_id": task_id, "status": "Pending"}
        elif task.state == "SUCCESS":
            return {"task_id": task_id, "status": "Success", "result": task.result}
        else:
            return {"task_id": task_id, "status": task.state}
    except Exception as e:
        return HTTPException(
            status_code=500, detail=f"Failed to get task status: {str(e)}"
        )


app.include_router(slog_router)

if MODULES.get("mail"):
    app.include_router(mail_router)
    mail_check_settings()
