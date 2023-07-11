import json
import pika
import smtplib
from email.message import EmailMessage

from config import settings


def callback(channel, method, properties, body):
    message = json.loads(body)

    if not isinstance(message, dict):
        return

    username = message['username']
    email = message['email']
    password = message['password']

    if not all([username, email, password]):
        return

    send_email_welcome(recipient_email=email, username=username, password=password)


def send_email_welcome(recipient_email: str, username: str, password: str):
    message = EmailMessage()
    message['From'] = settings.from_email
    message['To'] = recipient_email
    message['Subject'] = settings.welcome_subject

    with open(settings.message_html_path, 'r') as file:
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


def listen_welcome_messages():
    connection = pika.BlockingConnection(pika.URLParameters(settings.rabbitmq_url))
    channel = connection.channel()

    channel.queue_declare(queue=settings.welcome_queue_name)
    channel.basic_consume(
        queue=settings.welcome_queue_name, on_message_callback=callback, auto_ack=True
    )

    channel.start_consuming()
