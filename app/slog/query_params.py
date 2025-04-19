from pydantic import BaseModel, Field

from app.slog.models import LogType


class QueryParamSlog(BaseModel):
    log_type: LogType | None = Field(None, description="Тип события")
    status: bool | None = Field(None, description="Статус события")
    outer_id: int | None = Field(None, description="id внешней системы")

    def to_dict(self) -> dict:
        data = {
            "log_type": self.log_type,
            "status": self.status,
            "outer_id": self.outer_id,
        }
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
