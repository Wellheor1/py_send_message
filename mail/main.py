import smtplib
from mail.types import Emails
from settings.mail import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, SMTP_SECURE


def send(emails: Emails):
    smtp = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    if SMTP_SECURE:
        smtp.starttls()
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    for email in emails:
        print(email)
        # smtp.sendmail(SMTP_USER, email.to, mail_body)
    smtp.quit()
    return {"ok": True, "message": ""}
