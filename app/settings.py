# Адрес и порт сервера
ADDRESS = "127.0.0.1"
PORT = 8000
# Токены доступа к серверу
BEARER_TOKEN = "some token"

# Модули
MODULES = {"mail": False}

# Настройка подключения к БД
DB_HOST = "127.0.0.1"
DB_PORT = 5432
DB_NAME = "py_send_message"
DB_USER = "postgres"
DB_PASSWORD = "1234562"


try:
    from app.local_settings import *  # noqa: F403
except ImportError:
    pass
