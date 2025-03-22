import smtplib

from settings.mail import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD
from mail.utils import create_body


def send():
    smtp = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    subject = "Тестовый заголовок"
    message = "Тело письма"
    mail_body = create_body(subject, message)
    smtp.sendmail(SMTP_USER, "well.heor@yandex.ru", mail_body)
    smtp.quit()
    return {"ok": True, "message": ""}
