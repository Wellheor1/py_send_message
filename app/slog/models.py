from sqlalchemy import ForeignKey, text, Text,  Column, Integer, String, Enum, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, str_uniq, int_pk, str_null_true
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

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"sender={self.sender!r},"
                f"recipient={self.recipient!r})"
                f"log_type={self.log_type!r})"
                f"status={self.status!r})")

    def __repr__(self):
        return str(self)
