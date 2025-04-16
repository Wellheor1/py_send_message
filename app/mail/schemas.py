from pydantic import BaseModel, Field


class Attachment(BaseModel):
    encoding: str = Field(
        description="Кодировка вложения (например PDF в base64)", default=None
    )
    filename: str = Field(..., description="Наименование вложения, например file.pdf ")
    content: str = Field(..., description="Вложение")
    content_type: str = Field(
        ..., description="Тип вложения, по умолчанию octet-stream"
    )


class Email(BaseModel):
    to: str | list = Field(..., description="Адресат")
    subject: str = Field(..., description="Тема письма")
    message: str = Field(description="Тело письма", default=None)
    attachments: list[Attachment] = Field(
        description="Список вложений", default=None | list[Attachment]
    )
