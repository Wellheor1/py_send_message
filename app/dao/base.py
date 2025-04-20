from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import delete as sqlalchemy_delete
from app.database import async_session_maker


async def find_all(model, **filter_by):
    async with async_session_maker() as session:
        query = select(model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalars().all()


async def find_one(model, **filter_by):
    async with async_session_maker() as session:
        query = select(model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def add(model, **values):
    async with async_session_maker() as session:
        async with session.begin():
            new_instance = model(**values)
            session.add(new_instance)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return new_instance


async def delete(model, **filter_by):
    async with async_session_maker() as session:
        async with session.begin():
            query = sqlalchemy_delete(model).filter_by(**filter_by)
            result = await session.execute(query)
            try:
                await session.commit()
            except SQLAlchemyError as e:
                await session.rollback()
                raise e
            return result.rowcount
