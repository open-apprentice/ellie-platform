from sqlalchemy import Integer, String, Boolean
from sqlalchemy_utils import EmailType
from sqlalchemy.sql.schema import Column

from sqlalchemy.ext.declarative import declarative_base

# from database.db import Base
Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    created_courses = Column(String, nullable=True)  # This is a placeholder for a list


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    enrolled_courses = Column(String, nullable=True)  # This is a placeholder for a list


# class Admin(Base):
#     __tablename__ = 'admins'
#     id = Column(Integer, primary_key=True)
#     permission_level = Column(Integer, default=1)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    user_email = Column(EmailType, nullable=False)
