from pydantic_settings import BaseSettings
from pydantic import EmailStr


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
    from_email: EmailStr
    from_email_password: str
    welcome_subject: str
    smtp_host: str
    smtp_port: int
    redis_password: str
    redis_host: str
    redis_port: int

    @property
    def database_url(self):
        return f'postgresql://{self.database_username}:{self.database_password}@{self.database_hostname}:{self.database_port}/{self.database_name}'

    @property
    def redis_broker_url(self):
        # return f'redis://default:{self.redis_password}@{self.redis_host}:{self.redis_port}/0'
        return f'redis://{self.redis_host}:{self.redis_port}/0'

    class Config:
        env_file = '.env'


settings = Settings()
