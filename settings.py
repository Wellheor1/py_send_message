# Адрес и порт сервера
ADDRESS = "127.0.0.1"
PORT = 3000
# Токены доступа к серверу
BEARER_TOKEN = "some token"

MODULES = {
    "mail": False
}

try:
    from settings.local_settings.local_server import *
except ImportError:
    pass
