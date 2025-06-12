from app.celery_app import app as celery_app
from app.mail.api import send
from app.mail.schemas import Email


@celery_app.task
def send_email(email_data: dict):
    email = Email(
        to=email_data.get("to"),
        subject=email_data.get("subject"),
        message=email_data.get("message"),
        attachments=email_data.get("attachments"),
    )
    result_send = send(email)
    return result_send
