from pydantic import BaseModel


class Attachment(BaseModel):
    encoding: str
    filename: str
    content: str
    contentType: str


class Email(BaseModel):
    to: str | list
    subject: str
    message: str | None
    attachments: list[Attachment] | None


class Emails(BaseModel):
    emails: list[Email]
