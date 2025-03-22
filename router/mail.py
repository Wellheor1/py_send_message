import smtplib
from fastapi.responses import JSONResponse
from fastapi import APIRouter
from settings.mail import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD

# Создаём роутер
router = APIRouter(
    prefix="/mail",
    tags=["mail"]
)


@router.post("/send")
async def send_mail():
    smtp = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    return JSONResponse({"ok": True, "message": ""})
