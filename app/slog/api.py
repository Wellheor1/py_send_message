import datetime
import logging
from sqlalchemy import delete
from sqlalchemy.exc import SQLAlchemyError

from app.dao.base import add
from app.database import async_session_maker
from app.mail.settings import SMTP_USER
from app.slog.models import Slog

logger = logging.getLogger("uvicorn.error")


async def email_logged(result_send: dict[str, list]) -> None:
    for value in result_send.values():
        for email in value:
            recipients = email.get("recipient")
            status = email.get("status")
            logged_info = {
                "log_type": "mail",
                "sender": SMTP_USER,
                "recipient": recipients,
                "status": status,
                "outer_id": "",
            }
            await add(Slog, **logged_info)


async def delete_slog_older(count_days: int = 180):
    current_day = datetime.date.today()
    prev_day = current_day - datetime.timedelta(days=count_days)
    async with async_session_maker() as session:
        async with session.begin():
            query = delete(Slog).filter(Slog.created_at <= prev_day)
            result = await session.execute(query)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return result.rowcount
