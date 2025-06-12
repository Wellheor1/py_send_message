from uuid import UUID

from pydantic import BaseModel, Field


class Attachment(BaseModel):
    """
    Структура вложения письма
    """

    encoding: str = Field(
        description="Кодировка вложения (например PDF в base64)", default=None
    )
    filename: str = Field(..., description="Наименование вложения, например file.pdf ")
    content: str = Field(..., description="Вложение")
    content_type: str = Field(
        ..., description="Тип вложения, по умолчанию octet-stream"
    )


class Email(BaseModel):
    """
    Структура письма для отправки
    """

    to: str | list = Field(..., description="Адресат")
    subject: str = Field(..., description="Тема письма")
    message: str = Field(description="Тело письма", default=None)
    attachments: list[Attachment] = Field(description="Список вложений", default=None)


class SendingError(BaseModel):
    """
    Ошибка отправки
    """

    code: int = Field(default=..., description="Код ошибки")
    title: str = Field(default=..., description="Наименование ошибки")


class SendingErrorWithAddress(BaseModel):
    """
    Ошибка отправки с адресом получателя
    """

    recipient: str = Field(default=..., description="Адрес получателя")
    errors: SendingError = Field(..., description="Ошибка")


class ResultSend(BaseModel):
    """
    Результат запроса на отправку email
    """

    ok: bool = Field(default="", description="Результат запроса")
    message: str = Field(default="", description="Сообщение")
    result: list[SendingErrorWithAddress] = Field(
        default=[], description="Результат, список ошибок"
    )


class ResultCelery(BaseModel):
    task_id: UUID = Field(default="", description="id задачи")
    status: str = Field(default="", description="Статус задачи")


class ResultSendViaCelery(BaseModel):
    ok: bool = Field(default="", description="Результат запроса")
    message: str = Field(default="", description="Сообщение")
    result: dict = Field(description="Ответ celery")
