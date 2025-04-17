from app.slog.models import LogType


# class SlogQueryParam(BaseModel):
#     slog_id: int | None = None
#     log_type: LogType | None = None
#     status: bool | None = None
#     outer_id: int | None = None


class QueryParamSlog:
    def __init__(
        self,
        slog_id: int | None = None,
        log_type: LogType | None = None,
        status: bool | None = None,
        outer_id: int | None = None,
    ):
        self.id = slog_id
        self.log_type = log_type
        self.status = status
        self.outer_id = outer_id

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "log_type": self.log_type,
            "status": self.status,
            "outer_id": self.outer_id,
        }
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
