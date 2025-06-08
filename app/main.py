from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from app.auth.main import verify_bearer_token_v2
from app.redis_client import init_redis, close_redis
from app.router.mail import router as mail_router
from app.router.slog import router as slog_router
from app.settings import MODULES
from app.mail.utils import check_settings as mail_check_settings
from app.utils import check_settings as main_check_settings

app = FastAPI(dependencies=[Depends(verify_bearer_token_v2)])

main_check_settings()


@asynccontextmanager
async def lifespan():
    await init_redis()
    yield
    await close_redis()


@app.get("/", tags=["Приложение"])
async def root():
    result = []
    return JSONResponse({"ok": True, "message": "Hello World Well", "result": result})


app.include_router(slog_router)

if MODULES.get("mail"):
    app.include_router(mail_router)
    mail_check_settings()
