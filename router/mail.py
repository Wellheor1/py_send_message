from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends
from mail.main import send
from mail.types import Emails
from mail.utils import check_settings

router = APIRouter(
    prefix="/mail",
    tags=["mail"],
)


@router.post("/send")
async def send_mail(body: Emails):
    result = await send(body.emails)
    return JSONResponse(result)
