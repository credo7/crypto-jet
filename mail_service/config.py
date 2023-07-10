from pydantic import EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    rabbitmq_host: str
    rabbitmq_port: int
    welcome_queue_name: str
    from_email: EmailStr
    from_email_password: str
    welcome_subject: str
    smtp_host: str
    smtp_port: int
    message_html_path: str

    @property
    def rabbitmq_url(self):
        return f'amqp://guest:guest@{settings.rabbitmq_host}:{settings.rabbitmq_port}/'

    class Config:
        env_file = '.env'


settings = Settings()
