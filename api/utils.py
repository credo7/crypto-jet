import random
import string

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from fastapi import HTTPException, status, Response
from passlib.context import CryptContext

from oauth2 import create_access_token
from models import Username, User
from config import settings


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_available_username(session: Session) -> str:
    username = (
        session.query(Username).filter(Username.taken == False).order_by(func.random()).first()
    )

    if not username:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Didn't expect so many users.. All funny usernames are currently taken",
        )

    username.taken = True

    return username.username


def set_jwt_cookie(response: Response, user: User):
    token_data = {'id': str(user.id), 'email': user.email, 'username': user.username}
    access_token = create_access_token(token_data)
    response.set_cookie(
        key='access_token',
        value=access_token,
        max_age=settings.access_token_expire_minutes * 60,
        httponly=True,
        # secure=True,
    )


def generate_password(length=8) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def hash(password: str) -> str:
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_response_with_jwt_cookie(user: User) -> Response:
    token_data = {'id': str(user.id), 'email': user.email, 'username': user.username}
    access_token = create_access_token(token_data)
    response = Response().set_cookie(
        key='access_token',
        value=access_token,
        max_age=settings.access_token_expire_minutes * 60,
    )

    return response
