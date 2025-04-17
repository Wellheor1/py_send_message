from sqlalchemy.future import select
from app.database import async_session_maker


async def find_all(model, **filter_by):
    async with async_session_maker() as session:
        query = select(model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalars().all()


async def find_by_id(model, entity_id: int):
    async with async_session_maker() as session:
        query = select(model).filter_by(id=entity_id)
        result = await session.execute(query)
        return result.scalars_one_or_none()
