import logging
import os

logger = logging.getLogger("uvicorn.error")


def check_settings():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    local_settings_path = os.path.join(project_dir, "local_settings.py")
    local_settings_exists = os.path.exists(local_settings_path)
    if not local_settings_exists:
        logger.error("fdfsd")
        logger.error("There is no local settings file for the main module")
