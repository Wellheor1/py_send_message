import logging
import os
import smtplib
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from app.mail.schemas import Email
from app.mail.settings import SMTP_SECURE

logger = logging.getLogger("uvicorn.error")


def check_settings():
    mail_dir = os.path.dirname(os.path.abspath(__file__))
    local_settings_path = os.path.join(mail_dir, "local_settings.py")
    local_settings_exists = os.path.exists(local_settings_path)
    if not local_settings_exists:
        logger.warning(
            "The mail module is enabled, but there is no local settings file."
        )


def create_smtp():
    if SMTP_SECURE:
        smtp = smtplib.SMTP_SSL
    else:
        smtp = smtplib.SMTP
    return smtp


def get_encoder(encoding: str):
    encodings = {
        "base64": encoders.encode_base64,
    }
    result = encodings.get(encoding)
    return result


def create_attachment(
    filename, content, content_type, encoding=None
) -> MIMEApplication:
    if encoding:
        encoder = get_encoder(encoding)
        current_attachment = MIMEApplication(content, content_type, encoder)
    else:
        current_attachment = MIMEApplication(content, content_type)
    current_attachment.add_header(
        "Content-Disposition", "attachment", filename=filename
    )
    return current_attachment


def create_body(subject: str, message: str) -> MIMEMultipart:
    body = MIMEMultipart()
    body["Subject"] = subject
    text_part = MIMEText(message, "plain")
    body.attach(text_part)
    return body


def create_errors_body(errors: dict[str, tuple[int, str]]) -> list:
    result = []
    for recipient, error in errors.items():
        code, title = error
        result.append({"recipient": recipient, "error": {"code": code, "title": title}})
    return result


def create_body_with_attachments(email: Email):
    body = create_body(email.subject, email.message)
    for attachment in email.attachments:
        body.attach(
            create_attachment(
                attachment.filename,
                attachment.content,
                attachment.content_type,
                attachment.encoding,
            )
        )
    return body
