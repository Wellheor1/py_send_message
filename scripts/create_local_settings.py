import logging
import os
import shutil
import sys

sys.path.append("../py_send_message")
from app.settings import MODULES

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger("create_settings_file")


def create_local_settings_path(directory):
    local_settings_file_path = os.path.join(directory, "local_settings.py")
    return local_settings_file_path


def copy_settings_file(directory):
    shutil.copy(
        os.path.join(directory, "settings.py"),
        os.path.join(directory, "local_settings.py"),
    )


def find_project_dir():
    scripts_directory = os.path.dirname(__file__)
    project_directory = os.path.dirname(scripts_directory)
    return project_directory


project_dir = find_project_dir()
local_settings_file = create_local_settings_path(project_dir)
project_settings_exists = os.path.isfile(local_settings_file)
if not project_settings_exists:
    copy_settings_file(project_dir)
    logger.info(
        "The project settings file has been copied, do not forget to change the settings."
    )

modules = {module for module in MODULES if MODULES[module]}
for module in modules:
    module_dir = os.path.join(project_dir, module)
    local_settings_file = create_local_settings_path(module_dir)
    module_settings_exists = os.path.isfile(local_settings_file)
    if not module_settings_exists:
        copy_settings_file(module_dir)
        logger.info(
            f"The {module} module settings file has been copied, do not forget to change the settings."
        )
