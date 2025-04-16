from fastapi.responses import JSONResponse
from fastapi import APIRouter

from app.slog.dao import SlogDAO

router = APIRouter(
    prefix="/slogs",
    tags=["slog"],
)


@router.get("/", summary="get all logs")
async def get_all():
    result = await SlogDAO.find_all()
    print(result)
    return JSONResponse(result)
