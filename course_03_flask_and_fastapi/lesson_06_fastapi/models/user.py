"""
Создайте модель User со следующими полями:
    ○ id: int (идентификатор пользователя, генерируется автоматически)
    ○ username: str (имя пользователя)
    ○ email: str (электронная почта пользователя)
    ○ password: str (пароль пользователя)
"""

from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    username: str = Field(max_length=40)
    email: EmailStr = Field(max_length=128)
    password: str = Field(min_length=6)

class UserOut(BaseModel):
    id: int
    username: str = Field(max_length=40)
    email: EmailStr = Field(max_length=128)