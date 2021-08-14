from typing import Optional

from pydantic import BaseModel
from pydantic.networks import EmailStr
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from models.users import User
from models.courses import Course


class Author(BaseModel):
    created_courses: str # This is a placeholder for a list


class Student(BaseModel):
    enrolled_courses: str # This is a placeholder for a list


CreateUser = sqlalchemy_to_pydantic(User)
"""
class CreateUser(BaseModel):
    first_name: str
    last_name: str
    is_admin: bool
    user_email: EmailStr
    author: Optional[Author] = None
    student: Optional[Student] = None
    # Admin: Optional[Admin] = None
"""
