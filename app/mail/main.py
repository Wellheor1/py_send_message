from app.mail.schemas import Email
from app.mail.settings import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD
from app.mail.utils import create_smtp, create_body, create_attachment


async def sends(emails: list[Email]):
    smtp = create_smtp()
    result = []
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
            # todo Продумать структуру ответа, возвращаются только ошибки в виде { 'some@mail.ru', (550,
            #  'User Unknown') }
            if result_send:
                result.append({"ok": False, "errors": result_send})
            else:
                result.append({"ok": True, "errors": None})
    return {"ok": True, "message": "", "result": result}
