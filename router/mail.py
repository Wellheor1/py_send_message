import smtplib
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from mail.main import send

# Создаём роутер
router = APIRouter(
    prefix="/mail",
    tags=["mail"]
)


@router.post("/send")
async def send_mail():
    result = send()
    return JSONResponse(result)
