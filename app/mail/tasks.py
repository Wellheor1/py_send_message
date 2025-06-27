from celery.utils.log import get_task_logger

from app.celery_app import app as celery_app
from app.mail.settings import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD
from app.mail.schemas import Email
from app.mail.utils import create_smtp, create_body_with_attachments

logger = get_task_logger("celery_tasks")


@celery_app.task
def send_email(email_data: dict):
    email = Email(
        to=email_data.get("to"),
        subject=email_data.get("subject"),
        message=email_data.get("message"),
        attachments=email_data.get("attachments"),
    )
    smtp = create_smtp()
    with smtp(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        body = create_body_with_attachments(email)
        result_send = server.sendmail(SMTP_USER, email.to, body.as_string())
        return result_send
