from mail.types import Email
from mail.settings import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD
from mail.utils import create_smtp, create_body, create_attachment


async def sends(emails: list[Email]):
    smtp = create_smtp()
    with smtp(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        for email in emails:
            body = create_body(email.subject, email.message)
            for attachment in email.attachments:
                body.attach(create_attachment(attachment.filename, attachment.content, attachment.content_type,
                                              attachment.encoding))
            server.sendmail(SMTP_USER, email.to, body.as_string())
    return {"ok": True, "message": ""}