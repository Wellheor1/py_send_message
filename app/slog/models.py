from sqlalchemy import ForeignKey, text, Text, Column, Integer, String, Enum, Boolean, select
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, str_uniq, int_pk, str_null_true, async_session_maker
from datetime import date
from enum import Enum as PyEnum


class LogType(PyEnum):
    MAIL = 'mail'


class Slog(Base):
    id: Mapped[int_pk]
    log_type = Column(Enum(LogType))
    sender = Column(String(255))
    recipient = Column(String(255))
    status = Column(Boolean)
    outer_id = Column(String(255))

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"sender={self.sender!r},"
                f"recipient={self.recipient!r})"
                f"log_type={self.log_type!r})"
                f"status={self.status!r})")

    def __repr__(self):
        return str(self)

    @staticmethod
    async def find_all():
        async with async_session_maker() as session:
            query = select(Slog)
            result = await session.execute(query)
            return result.all()
