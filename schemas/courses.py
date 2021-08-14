from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from models.courses import Course, CourseSection

PydanticCourse = sqlalchemy_to_pydantic(Course, exclude=["id"])
PydanticCourseSection = sqlalchemy_to_pydantic(CourseSection, exclude=["id"])
