from fastapi import APIRouter

from app.mail.api import sends
from app.mail.schemas import Email, ResultSend
from app.mail.task import send_email
from app.slog.api import email_logged

router = APIRouter(
    prefix="/mail",
    tags=["Электронная почта"],
)


@router.post("/sends", summary="Отправка писем", response_model=ResultSend)
async def send_emails(body: list[Email]):
    result_send = await sends(body)
    await email_logged(result_send.get("result"))
    result = ResultSend(
        ok=True, message="", result=result_send.get("result").get("errors")
    )
    return result


@router.post("/sends-deferred", summary="Отправка писем", response_model=ResultSend)
async def send_via_celery(body: Email):
    task = send_email.delay(body)
    result = ResultSend(
        ok=True, message="", result={"task_id": task.id, "status": "Task started"}
    )
    return result
