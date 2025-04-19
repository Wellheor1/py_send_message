from app.mail.schemas import Email
from app.mail.settings import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD
from app.mail.utils import (
    create_smtp,
    create_body,
    create_attachment,
    create_errors_body,
)


async def sends(emails: list[Email]):
    smtp = create_smtp()
    errors = []
    with smtp(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        for email in emails:
            body = create_body(email.subject, email.message)
            for attachment in email.attachments:
                body.attach(
                    create_attachment(
                        attachment.filename,
                        attachment.content,
                        attachment.content_type,
                        attachment.encoding,
                    )
                )
            result_send = server.sendmail(SMTP_USER, email.to, body.as_string())
            if result_send:
                errors.extend(create_errors_body(result_send))
    return {"ok": True, "message": "", "result": errors}
