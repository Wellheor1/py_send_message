import logging
import os
import smtplib
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from mail.settings import SMTP_SECURE

logger = logging.getLogger("uvicorn.error")


def check_settings():
    mail_dir = os.path.dirname(os.path.abspath(__file__))
    local_settings_path = os.path.join(mail_dir, "local_settings.py")
    local_settings_exists = os.path.exists(local_settings_path)
    if not local_settings_exists:
        logger.warning("The mail module is enabled, but there is no local settings file.")


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


def create_attachment(filename, content, content_type, encoding=None):
    if encoding:
        encoder = get_encoder(encoding)
        current_attachment = MIMEApplication(content, content_type, encoder)
    else:
        current_attachment = MIMEApplication(content, content_type)
    current_attachment.add_header("Content-Disposition", "attachment",
                                  filename=filename)
    return current_attachment


def create_body(subject: str, message: str) -> MIMEMultipart:
    body = MIMEMultipart()
    body["Subject"] = subject
    text_part = MIMEText(message, "plain")
    body.attach(text_part)
    return body
