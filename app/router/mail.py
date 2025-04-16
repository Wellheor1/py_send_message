from fastapi.responses import JSONResponse
from fastapi import APIRouter

from app.mail.main import sends
from app.mail.schemas import Emails, Result

router = APIRouter(
    prefix="/mail",
    tags=["mail"],
)


@router.post("/sends", summary="Send email", response_model=Result)
async def send_mails(body: Emails):
    result = await sends(body.emails)
    return JSONResponse(result)
