from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType
from sqlalchemy.sql.schema import Column, ForeignKey

from sqlalchemy.ext.declarative import declarative_base

# from database.db import Base
Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    created_courses = Column(String, nullable=True)  # This is a placeholder for a list
    ## Is this correct?
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="authors")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    enrolled_courses = Column(String, nullable=True)  # This is a placeholder for a list
    ## Is this correct?
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="students")


# What about this?
# class Admin(Base):
#     __tablename__ = 'admins'
#     id = Column(Integer, primary_key=True)
#     permission_level = Column(Integer, default=1)
## Is this correct?
# user_id = Column(Integer, ForeignKey("users.id"))
# user = relationship("User", back_populates="admins")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    user_email = Column(EmailType, nullable=False)

    # Is this correct?
    authors = relationship("Author", back_populates="user")
    students = relationship("Student", back_populates="user")
    # admins = relationship("Admin", back_populates="users")
