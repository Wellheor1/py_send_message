from pydantic import BaseModel


class Result(BaseModel):
    ok: bool
    message: str
    result: dict | list
