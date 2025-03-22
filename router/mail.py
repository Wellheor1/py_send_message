from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends
from mail.main import send
from mail.types import Emails
from mail.utils import check_settings

router = APIRouter(
    prefix="/mail",
    tags=["mail"],
    dependencies=[Depends(check_settings)]
)


@router.post("/send")
async def send_mail(emails: Emails):
    result = send(emails)
    return JSONResponse(result)
