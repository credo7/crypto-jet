from typing import List
import functools

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import UUID4

import schemas
import database
import models
from oauth2 import get_user_or_raise_exception


router = APIRouter(tags=['Users'], prefix='/users')


@router.get('', status_code=status.HTTP_200_OK, response_model=List[schemas.GetUser])
def get_users(
    _admin_user: models.User = Depends(
        functools.partial(get_user_or_raise_exception, require_admin=True)
    ),
    db: Session = Depends(database.get_db),
):
    users = db.query(models.User).all()
    return models.User.to_json_list(users)


@router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=schemas.GetUser)
def get_user(
    user_id: UUID4,
    _user: models.User = Depends(get_user_or_raise_exception),
    db: Session = Depends(database.get_db),
):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    return user.to_json()
