import smtplib

from settings.mail import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, SMTP_SECURE
from mail.utils import create_body


def send(to_address: str, subject, message, mail_body=None):
    smtp = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    if SMTP_SECURE:
        smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    if not mail_body:
        mail_body = create_body(subject, message)
    smtp.sendmail(SMTP_USER, to_address, mail_body)
    smtp.quit()
    return {"ok": True, "message": ""}
