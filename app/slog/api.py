import datetime
import functools
import logging
from sqlalchemy import delete
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker
from app.slog.models import Slog

logger = logging.getLogger("uvicorn.error")


def logged(function):
    @functools.wraps(function)
    async def wrapper(*args, **kwargs):
        logger.info("до функции")
        result = await function(*args, **kwargs)
        logger.info("после функции")
        return result

    return wrapper


async def delete_slog(count_days: int = 180):
    current_day = datetime.date.today()
    prev_day = current_day - datetime.timedelta(days=count_days)
    async with async_session_maker() as session:
        async with session.begin():
            query = delete(Slog).filter_by(created_at__lte=prev_day)
            result = await session.execute(query)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return result.rowcount
