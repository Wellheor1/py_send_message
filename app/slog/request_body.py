from pydantic import BaseModel, Field

from app.slog.models import LogType


class SSlogAdd(BaseModel):
    log_type: LogType = Field(
        ..., description="Тип события, [email, telegram, whatsapp]"
    )
    sender: str = Field(..., description="Отправитель, от 1 до 255 символов")
    recipient: str = Field(..., description="Получатель, от 1 до 255 символов")
    status: bool = Field(..., description="Статус отправки")
    outer_id: str = Field(
        ..., description="id в отправившей системе, от 1 до 255 символов"
    )

    def to_dict(self) -> dict:
        data = {
            "log_type": self.log_type,
            "sender": self.sender,
            "recipient": self.recipient,
            "status": self.status,
            "outer_id": self.outer_id,
        }
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
