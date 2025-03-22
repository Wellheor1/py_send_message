from fastapi.responses import JSONResponse
from fastapi import APIRouter
from pydantic import BaseModel

from mail.main import send
from mail.types import Emails

# Создаём роутер
router = APIRouter(
    prefix="/mail",
    tags=["mail"]
)


@router.post("/send")
async def send_mail(emails: Emails):
    result = send(emails)
    return JSONResponse(result)
