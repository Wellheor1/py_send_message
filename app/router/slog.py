from fastapi import APIRouter, Query, Body

from app.dao.base import find_all, find_one, add
from app.slog.models import Slog
from app.slog.query_params import QueryParamSlog, QueryParamSlogId
from app.slog.request_body import SSlogAdd
from app.slog.schemas import ResultSSlog, ResultSSlogs
from app.slog.main import logged

router = APIRouter(
    prefix="/slogs",
    tags=["Системные логи"],
)


@router.get("/", summary="Получить все записи логов")
@logged
async def get_all_slogs(query_params: QueryParamSlog = Query()) -> ResultSSlogs:
    slogs = await find_all(Slog, **query_params.to_dict())
    result = ResultSSlogs(ok=True, message="", result=slogs)
    return result


@router.get("/one", summary="Получить одну запись логов")
@logged
async def get_slog_by_id(query_params: QueryParamSlogId = Query()) -> ResultSSlog:
    slog = await find_one(Slog, **query_params.to_dict())
    if slog:
        ok = True
        message = ""
    else:
        ok = False
        message = "Такой записи нет"
    result = ResultSSlog(ok=ok, message=message, result=slog)
    return result


@router.post("/add", summary="Создать новый лог")
@logged
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
