# Адрес и порт сервера
ADDRESS = "127.0.0.1"
PORT = 8000
# Токены доступа к серверу
BEARER_TOKEN = "some token"

MODULES = {
    "mail": False
}

DB_HOST = '127.0.0.1'
DB_PORT = 5432
DB_NAME = 'py_send_message'
DB_USER = 'postgres'
DB_PASSWORD = '1234562'


def get_db_url():
    return (f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@"
            f"{DB_HOST}:{DB_PORT}/{DB_NAME}")


try:
    from app.local_settings import *
except ImportError:
    pass
