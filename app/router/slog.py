from fastapi.responses import JSONResponse
from fastapi import APIRouter

from app.slog.dao import SlogDao
from app.slog.schemas import SSlog

router = APIRouter(
    prefix="/slogs",
    tags=["slog"],
)


@router.get("/", summary="get all logs", response_model=list[SSlog])
async def get_all():
    result = await SlogDao.find_all()
    return JSONResponse(result)
