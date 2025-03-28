from email import encoders
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from mail.types import Email
from mail.settings import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD
from mail.utils import create_smtp, get_encoder


async def send(emails: list[Email]):
    smtp = create_smtp()
    with smtp(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        for email in emails:
            body = MIMEMultipart()
            body["Subject"] = email.subject
            text_part = MIMEText(email.message, "plain")
            body.attach(text_part)
            for attachment in email.attachments:
                if attachment.encoding:
                    encoder = get_encoder(attachment.encoding)
                    current_attachment = MIMEApplication(attachment.content, attachment.contentType, encoder)
                else:
                    current_attachment = MIMEApplication(attachment.content, attachment.contentType)
                current_attachment.add_header("Content-Disposition", "attachment",
                                              filename=attachment.filename)
                body.attach(attachment)
            server.sendmail(SMTP_USER, email.to, body.as_string())
    return {"ok": True, "message": ""}
