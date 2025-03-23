from pydantic import BaseModel


class Email(BaseModel):
    to: str | list
    subject: str
    message: str
    attachments: str | list


class Emails(BaseModel):
    emails: list[Email]
