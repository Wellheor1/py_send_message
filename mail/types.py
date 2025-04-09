from pydantic import BaseModel


class Attachment(BaseModel):
    encoding: str | None = None
    filename: str
    content: str
    content_type: str


class Email(BaseModel):
    to: str | list
    subject: str
    message: str | None = None
    attachments: list[Attachment] | None = None


class Emails(BaseModel):
    emails: list[Email]
