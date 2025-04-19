from fastapi.responses import JSONResponse
from fastapi import APIRouter

from app.mail.main import sends
from app.mail.schemas import Email, ResultSend
from app.slog.main import logged

router = APIRouter(
    prefix="/mail",
    tags=["Электронная почта"],
)


@router.post("/sends", summary="Отправка писем", response_model=ResultSend)
@logged
async def send_mails(body: list[Email]):
    result = await sends(body)
    # todo Логировать
    return JSONResponse(result)
