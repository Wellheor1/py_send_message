import os
from pydantic_settings import BaseSettings, SettingsConfigDict

# Адрес и порт сервера
ADDRESS = "127.0.0.1"
PORT = 8000
# Токены доступа к серверу
BEARER_TOKEN = "some token"

MODULES = {
    "mail": False
}


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env")
    )


settings = Settings()


def get_db_url():
    return (f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@"
            f"{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")


try:
    from app.local_settings import *
except ImportError:
    pass
