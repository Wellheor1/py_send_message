from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.auth.main import verify_bearer_token
from app.database import async_session_maker
from app.router.mail import router as mail_router
from app.settings import MODULES
from app.mail.utils import check_settings as mail_check_settings
from app.slog.models import Slog
from app.utils import check_settings as main_check_settings

app = FastAPI(dependencies=[Depends(verify_bearer_token)])


main_check_settings()
if MODULES.get("mail"):
    app.include_router(mail_router)
    mail_check_settings()


@app.get("/", tags=["main"])
async def root():
    result = await Slog.find_all()
    return JSONResponse({"ok": True, "message": "Hello World Well", "result": result})
