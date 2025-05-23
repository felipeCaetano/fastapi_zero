from typing import List

from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr


class UserDB(UserPublic):
    id: int


class UserList(BaseModel):
    users: List[UserPublic]
