from fastapi import APIRouter

from app.mail.api import sends
from app.mail.schemas import Email, ResultSend
from app.slog.api import email_logged

router = APIRouter(
    prefix="/mail",
    tags=["Электронная почта"],
)


@router.post("/sends", summary="Отправка писем", response_model=ResultSend)
async def send_mails(body: list[Email]):
    result_send = await sends(body)
    await email_logged(result_send.get("result"))
    result = ResultSend(
        ok=True, message="", result=result_send.get("result").get("errors")
    )
    return result
