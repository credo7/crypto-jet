from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    email: EmailStr


class GetUser(BaseModel):
    id: str
    username: str
    email: EmailStr
    created_at: str
    updated_at: str


class TokenData(BaseModel):
    id: str
    email: EmailStr
    username: str
