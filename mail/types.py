from pydantic import BaseModel


class Email(BaseModel):
    to: str
    subject: str
    message: str
    attachments: str


class Emails(BaseModel):
    emails: list[Email]
