from fastapi.responses import JSONResponse
from fastapi import APIRouter, Query

from app.dao.base import find_all, find_one
from app.slog.models import Slog
from app.slog.query_params import QueryParamSlog, QueryParamSlogId
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


@router.get("/one", summary="Получить одну запись логов", response_model=ResultSSlog)
@logged
async def get_by_id(query_params: QueryParamSlogId = Query()):
    slog = await find_one(Slog, **query_params.to_dict())
    if slog:
        result = {"ok": True, "message": "", "result": slog}
    else:
        result = {"ok": False, "message": "Такой записи нет", "result": slog}
    return JSONResponse(result)
