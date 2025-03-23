import logging
import os

logger = logging.getLogger("mail")


def check_settings():
    mail_dir = os.path.dirname(os.path.abspath(__file__))
    local_settings_path = os.path.join(mail_dir, "local_settings.py")
    local_settings_exists = os.path.exists(local_settings_path)
    if not local_settings_exists:
        logger.error("The mail module is enabled, but there is no local settings file.")
