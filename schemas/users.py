from typing import Optional

from pydantic import BaseModel
from pydantic.networks import EmailStr

class Author(BaseModel):
    created_courses: str

class Student(BaseModel):
    enrolled_courses: str

class Admin(BaseModel):
    permission_level: int

class CreateUser(BaseModel):
    first_name: str
    last_name: str
    is_admin: bool
    user_email: EmailStr
    author: Optional[Author] = None
    student: Optional[Student] = None
    Admin: Optional[Admin] = None
