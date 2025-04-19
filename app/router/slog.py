from fastapi.responses import JSONResponse
from fastapi import APIRouter, Query, Path

from app.dao.base import find_all, find_by_id
from app.slog.models import Slog
from app.slog.query_params import QueryParamSlog
from app.slog.schemas import ResultSSlog, ResultSSlogs
from app.slog.main import logged

router = APIRouter(
    prefix="/slogs",
    tags=["Системные логи"],
)


@router.get("/", summary="Получить все записи логов", response_model=ResultSSlogs)
@logged
async def get_all(query_params: QueryParamSlog = Query()):
    slogs = await find_all(Slog, **query_params.to_dict())
    result = {"ok": True, "message": "", "result": slogs}
    return JSONResponse(result)


@router.get("/{slog_id}", summary="Получить логи по id", response_model=ResultSSlog)
@logged
async def get_by_id(slog_id: int = Path()):
    slog = await find_by_id(Slog, slog_id)
    if slog:
        result = {"ok": True, "message": "", "result": slog}
    else:
        result = {"ok": False, "message": "Лога с таким id нет", "result": slog}
    return JSONResponse(result)
