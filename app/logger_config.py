import logging
import logging.config
import os

LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "standard",
        },
        "fastapi_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "standard",
            # "filename": "logs/fastapi.log",
            "filename": os.path.join(LOG_DIR, "fastapi.log"),
            "maxBytes": 10485760,  # 10MB
            "backupCount": 5,
        },
        "celery_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "standard",
            # "filename": "logs/celery.log",
            "filename": os.path.join(LOG_DIR, "celery.log"),
            "maxBytes": 10485760,  # 10MB
            "backupCount": 5,
        },
    },
    "loggers": {
        "fastapi": {
            "handlers": ["console", "fastapi_file"],
            "level": "INFO",
            "propagate": False,
        },
        "celery": {
            "handlers": ["console", "celery_file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}


def setup_logging():
    logging.config.dictConfig(logging_config)
