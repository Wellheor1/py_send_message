from fastapi.responses import JSONResponse
from fastapi import APIRouter, Query, Path

from app.dao.base import find_all, find_by_id
from app.slog.models import Slog
from app.slog.query_params import QueryParamSlog
from app.slog.schemas import SSlog

router = APIRouter(
    prefix="/slogs",
    tags=["slog"],
)


@router.get("/", summary="Получить все записи логов", response_model=list[SSlog])
async def get_all(query_params: QueryParamSlog = Query()):
    result = await find_all(Slog, **query_params.to_dict())
    return JSONResponse(result)


@router.get("/{slog_id}", summary="Получить логи по id", response_model=SSlog)
async def get_by_id(slog_id: int = Path()):
    result = await find_by_id(Slog, slog_id)
    return JSONResponse(result)
