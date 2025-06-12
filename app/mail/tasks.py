from app.celery_app import app as celery_app
from app.mail.api import send


@celery_app.task
def send_email(email):
    result_send = send(email)
    return result_send
