from fastapi import APIRouter, Query, Body

from app.dao.base import find_all, find_one, add
from app.slog.models import Slog
from app.slog.query_params import (
    QueryParamGetSlog,
    QueryParamGetSlogWithId,
    QueryParamDeleteSlog,
)
from app.slog.request_body import SSlogAdd
from app.slog.schemas import ResultSSlog, ResultSSlogs, ResultDeleteSSlog
from app.slog.api import delete_slog_older

router = APIRouter(
    prefix="/slogs",
    tags=["Системные логи"],
)


@router.get("/", summary="Получить все записи логов", response_model=ResultSSlogs)
async def get_all_slogs(query_params: QueryParamGetSlog = Query()):
    slogs = await find_all(Slog, **query_params.to_dict())
    result = {"ok": True, "message": "", "result": slogs}
    return result


@router.get("/one", summary="Получить одну запись логов", response_model=ResultSSlog)
async def get_slog_by_id(
    query_params: QueryParamGetSlogWithId = Query(),
):
    slog = await find_one(Slog, **query_params.to_dict())
    if slog:
        ok = True
        message = ""
    else:
        ok = False
        message = "Такой записи нет"
    result = {"ok": ok, "message": message, "result": slog}
    return result


@router.post("/add", summary="Создать новый лог")
async def add_slog(request_body: SSlogAdd = Body()) -> ResultSSlog:
    slog = await add(Slog, **request_body.to_dict())
    if slog:
        ok = True
        message = ""
    else:
        ok = False
        message = "Не удалось создать лог"
    result = ResultSSlog(ok=ok, message=message, result=slog)
    return result


@router.delete("/", summary="Удалить логи")
async def delete_slog(
    query_params: QueryParamDeleteSlog = Query(),
) -> ResultDeleteSSlog:
    slog = await delete_slog_older(query_params.count_days)
    result = ResultDeleteSSlog(ok=True, message="", result=slog)
    return result
