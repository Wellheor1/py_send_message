from pydantic import BaseModel, Field


class Result(BaseModel):
    ok: bool = Field(..., description="Статус запроса")
    message: str = Field(..., description="Сообщение")
    result: dict | list = Field(..., description="Результата запроса")
