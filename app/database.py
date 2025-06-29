import os
from datetime import datetime
from typing import Annotated
from sqlalchemy import func
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

from app.settings import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT


def get_db_url():
    db_user = os.getenv("POSTGRES_USER", DB_USER)
    db_password = os.getenv("POSTGRES_PASSWORD", DB_PASSWORD)
    db_host = os.getenv("POSTGRES_HOST", DB_HOST)
    db_port = os.getenv("POSTGRES_PORT", DB_PORT)
    db_name = os.getenv("POSTGRES_DB", DB_NAME)
    return (
        f"postgresql+asyncpg://{db_user}:{db_password}@"
        f"{db_host}:{db_port}/{db_name}"
    )


DATABASE_URL = get_db_url()

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# настройка аннотаций
int_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[
    datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)
]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
str_null_true = Annotated[str, mapped_column(nullable=True)]


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
