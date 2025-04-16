from pydantic import BaseModel


class Result(BaseModel):
    ok: bool
    message: str
    result: dict | list


class Attachment(BaseModel):
    encoding: str | None = None
    filename: str
    content: str
    content_type: str


class Attachments(BaseModel):
    attachments: list[Attachment]


class Email(BaseModel):
    to: str | list
    subject: str
    message: str | None = None
    attachments: Attachments | None = None


class Emails(BaseModel):
    emails: list[Email]
