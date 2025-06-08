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

# Настройка подключения к Redis
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None


try:
    from app.local_settings import *  # noqa: F403
except ImportError:
    pass
