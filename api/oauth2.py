from datetime import datetime, timedelta

from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from database import get_db
import models
import schemas
from config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def create_access_token(user_data: dict):
    to_encode = user_data.copy()

    expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({'exp': expire})

    encoded_jwt = jwt.encode(
        to_encode, settings.access_token_secret_key, algorithm=settings.algorithm
    )

    return encoded_jwt


def verify_access_token(token: str, credentials_exception, raise_on_error=True):
    try:
        payload = jwt.decode(
            token, settings.access_token_secret_key, algorithms=[settings.algorithm]
        )

        id: str = payload.get('user_id')

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id=id)

    except JWTError:
        if raise_on_error:
            raise credentials_exception

        token_data = None

    return token_data


def get_current_user(
    token: str = Depends(oauth2_scheme), raise_on_error=True, db: Session = Depends(get_db)
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f'Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    token = verify_access_token(token, credentials_exception, raise_on_error=raise_on_error)

    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user