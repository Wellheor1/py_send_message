from app.mail.schemas import Email
from app.mail.settings import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD
from app.mail.utils import (
    create_smtp,
    create_body_with_attachments,
    create_result_send,
)


async def send(email: Email, session=None):
    if session:
        body = create_body_with_attachments(email)
        result_send = session.sendmail(SMTP_USER, email.to, body.as_string())
    else:
        smtp = create_smtp()
        with smtp(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASSWORD)
            body = create_body_with_attachments(email)
            result_send = server.sendmail(SMTP_USER, email.to, body.as_string())
    return result_send


async def sends(emails: list[Email]):
    smtp = create_smtp()
    success = []
    errors = []
    with smtp(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        for email in emails:
            result_send = await send(email, server)
            if result_send:
                errors.append(create_result_send(email.to, result_send))
            else:
                success.append(create_result_send(email.to, result_send))
    result = {"success": success, "errors": errors}
    return {"ok": True, "message": "", "result": result}
