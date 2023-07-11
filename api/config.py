from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_port: int
    database_hostname: str
    database_port: int
    database_password: str
    database_name: str
    database_username: str
    algorithm: str
    access_token_secret_key: str
    access_token_expire_minutes: int
    rabbitmq_host: str
    rabbitmq_port: int
    welcome_queue_name: str

    @property
    def database_url(self):
        return f'postgresql://{self.database_username}:{self.database_password}@{self.database_hostname}:{self.database_port}/{self.database_name}'

    @property
    def rabbitmq_url(self):
        return f'amqp://guest:guest@{settings.rabbitmq_host}:{settings.rabbitmq_port}/'

    class Config:
        env_file = '.env'


settings = Settings()
