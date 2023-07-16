import smtplib
from email.message import EmailMessage
from config import settings

from celery import Celery

celery_app = Celery('tasks', broker=settings.redis_broker_url)
celery_app.conf.broker_transport_options = {'visibility_timeout': 3600}  # 1 hour


@celery_app.task
def send_welcome_message_with_credentials(username: str, password: str, email: str) -> None:
    message = EmailMessage()
    message['From'] = settings.from_email
    message['To'] = email
    message['Subject'] = settings.welcome_subject

    with open('templates/welcome_message.html', 'r') as file:
        html_content = file.read()

    personalized_html = html_content.replace('[Username]', username).replace(
        '[Password]', password
    )

    message.add_alternative(personalized_html, subtype='html')

    try:
        with smtplib.SMTP_SSL(host=settings.smtp_host, port=settings.smtp_port) as smtp:
            smtp.login(settings.from_email, settings.from_email_password)
            smtp.send_message(message)

    except Exception as e:
        print(e)
