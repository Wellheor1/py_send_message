from fastapi.responses import JSONResponse
from fastapi import APIRouter, Query

from app.dao.base import find_all
from app.slog.models import Slog
from app.slog.query_params import QueryParamSlog
from app.slog.schemas import SSlog

router = APIRouter(
    prefix="/slogs",
    tags=["slog"],
)


@router.get("/", summary="get all logs", response_model=list[SSlog])
async def get_all(query_params: QueryParamSlog = Query()):
    result = await find_all(Slog, **query_params.to_dict())
    return JSONResponse(result)
