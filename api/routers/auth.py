from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import APIRouter, status, Depends, Response, HTTPException
from sqlalchemy.orm import Session

from utils import (
    get_available_username,
    generate_password,
    hash,
    verify,
    set_jwt_cookie,
)
from background_tasks import send_welcome_message_with_credentials
import database
import schemas
import models
from config import settings


router = APIRouter(tags=['Authorization'], prefix='/auth')


@router.post('/register', status_code=status.HTTP_201_CREATED, response_model=None)
def register(
    response: Response,
    user_create_dto: schemas.UserCreate,
    db: Session = Depends(database.get_db),
):
    username = get_available_username(session=db)
    password = generate_password()
    hashed_password = hash(password)

    new_user = models.User(
        username=username, email=user_create_dto.email, password=hashed_password
    )
    db.add(new_user)
    db.commit()

    set_jwt_cookie(response=response, user=new_user)

    send_welcome_message_with_credentials.delay(
        username=username, password=password, email=user_create_dto.email
    )


@router.post('/login', status_code=status.HTTP_200_OK, response_model=None)
def login(
    response: Response,
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    user = (
        db.query(models.User).filter(models.User.username == user_credentials.username).first()
    )

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    if not verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail='Invalid Credentials'
        )

    set_jwt_cookie(response=response, user=user)
