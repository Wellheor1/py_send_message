from pydantic import BaseModel, Field, ConfigDict


class SSlog(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    log_type: str = Field(..., description="Тип события, [email, telegram, whatsapp]")
    sender: str = Field(..., description="Отправитель, от 1 до 255 символов")
    recipient: str = Field(..., description="Получатель, от 1 до 255 символов")
    status: str = Field(..., description="Статус отправки")
    outer_id: str = Field(
        ..., description="id в отправившей системе, от 1 до 255 символов"
    )
