from fastapi.responses import JSONResponse
from fastapi import APIRouter

from app.mail.main import sends
from app.mail.types import Emails

router = APIRouter(
    prefix="/mail",
    tags=["mail"],
)


@router.post("/sends")
async def send_mail(body: Emails):
    result = await sends(body.emails)
    return JSONResponse(result)
