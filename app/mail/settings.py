# Настройка почтовых серверов
SMTP_HOST = "smtp.mail.ru"
SMTP_PORT = 465
SMTP_SECURE = True
SMTP_USER = "account@mail.ru"
SMTP_PASSWORD = "passwordFromApplication"
SMTP_SUBJECT = "Subject"
SMTP_TEXT = "message"

try:
    from app.mail.local_settings import *  # noqa: F403
except ImportError:
    pass
