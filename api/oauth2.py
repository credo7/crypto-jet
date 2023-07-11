from datetime import datetime, timedelta

from fastapi import Depends, status, HTTPException, Cookie
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
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


def verify_access_token(token: str) -> schemas.TokenData or None:
    try:
        payload = jwt.decode(
            token, settings.access_token_secret_key, algorithms=[settings.algorithm]
        )

        id: str = payload.get('id')
        username: str = payload.get('username')
        email: str = payload.get('email')

        token_data = schemas.TokenData(id=id, email=email, username=username)

        return token_data

    except:
        return None


def get_user_or_raise_exception(
    access_token: str = Cookie(None),
    db: Session = Depends(get_db),
    require_admin: bool = False,
) -> models.User:
    if not access_token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized')

    token_data = verify_access_token(access_token)
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate credentials'
        )

    user = db.query(models.User).filter(models.User.id == token_data.id).first()

    if require_admin and not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='User is not authorized to access this data',
        )

    return user
