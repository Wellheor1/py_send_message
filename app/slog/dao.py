from sqlalchemy import select
from app.slog.models import Slog
from app.database import async_session_maker


class SlogDAO:
    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(Slog)
            students = await session.execute(query)
            return students.scalars().all()
