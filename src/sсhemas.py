from datetime import date, datetime
from pydantic import BaseModel, EmailStr, Field


class ContactBase(BaseModel):
    firstname: str = "John"
    lastname: str = "Dou"
    email: EmailStr = "test@test.com"
    phone: str = "1234567890"
    birthday: date = date(year=2023, month=1, day=1)


class ContactCreate(ContactBase):
    pass


class ContactResponse(BaseModel):
    id: int = 1
    firstname: str
    lastname: str
    email: EmailStr
    phone: str
    birthday: date

    class Config:
        orm_mode = True


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=10)


class UserDb(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RequestEmail(BaseModel):
    email: EmailStr
