from app.celery_app import app as celery_app


@celery_app.task
def send_email(recipient, subject, body):
    # Логика отправки email
    print(f"Отправка email: {subject} to {recipient}")
    return f"Email sent to {recipient}"
