import logging

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from auth.main import verify_bearer_token
from router.mail import router as mail_router
from settings import MODULES
from mail.utils import check_settings as mail_check_settings
from utils import check_settings as main_check_settings

app = FastAPI(dependencies=[Depends(verify_bearer_token)])
main_check_settings()
if MODULES.get("mail"):
    app.include_router(mail_router)
    mail_check_settings()


@app.get("/", tags=["main"])
async def root():
    return JSONResponse({"message": "Hello World Well"})


