from fastapi.responses import JSONResponse
from fastapi import APIRouter

from app.dao.base import find_all
from app.slog.models import Slog
from app.slog.schemas import SSlog

router = APIRouter(
    prefix="/slogs",
    tags=["slog"],
)


@router.get("/", summary="get all logs", response_model=list[SSlog])
async def get_all():
    result = await find_all(Slog)
    return JSONResponse(result)
