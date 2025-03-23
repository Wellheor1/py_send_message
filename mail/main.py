import base64
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from mail.types import Emails, Email
from mail.settings import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD
from mail.utils import create_smtp


async def send(emails: list[Email]):
    smtp = create_smtp()
    with smtp(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        for email in emails:
            body = MIMEMultipart()
            body["Subject"] = email.subject
            text_part = MIMEText(email.message, "plain")
            attachments = MIMEApplication(email.attachments, "pdf")
            attachments.add_header("Content-Disposition", "attachment", filename="file.pdf")
            body.attach(text_part)
            body.attach(attachments)
            server.sendmail(SMTP_USER, email.to, body.as_string())
    return {"ok": True, "message": ""}
