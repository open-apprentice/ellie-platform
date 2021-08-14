from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from models.users import User, Author, Student

PydanticUser = sqlalchemy_to_pydantic(User, exclude=["id"])
PydanticAuthor = sqlalchemy_to_pydantic(Author, exclude=["id"])
PydanticStudent = sqlalchemy_to_pydantic(Student, exclude=["id"])
