from fastapi.responses import JSONResponse
from fastapi import APIRouter

from app.mail.main import sends
from app.mail.schemas import Email
from app.router.schemas import Result

router = APIRouter(
    prefix="/mail",
    tags=["mail"],
)


@router.post("/sends", summary="Send email", response_model=Result)
async def send_mails(body: list[Email]):
    result = await sends(body)
    return JSONResponse(result)
