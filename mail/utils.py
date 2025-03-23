import logging
import os
import smtplib

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