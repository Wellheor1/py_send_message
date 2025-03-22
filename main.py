import smtplib
from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from auth.main import verify_bearer_token
from settings.mail import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD

app = FastAPI(dependencies=[Depends(verify_bearer_token)])


@app.get("/")
async def root():
    return JSONResponse({"message": "Hello World Well"})


@app.get("/send-mail")
async def send_mail():
    smtp = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    return JSONResponse({"ok": True, "message": ""})
