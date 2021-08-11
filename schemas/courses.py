from typing import List

from datetime import date
from pydantic import BaseModel


class CreateCourseSection(BaseModel):
    course_section_name: str
    date_published: date = None
    last_updated: date = None
    course_section_is_draft: bool
    course_section_is_complete: bool
    course_section_purpose: str
    course_section_order: int
    # This needs a way to assign to a specific course
    # QUESTION: How to create a many to one relationship that syncs with the sqlalchemy engine?


class CreateCourse(BaseModel):
    course_name: str
    is_draft: bool
    is_published: bool
    date_published: date = None
    last_updated: date = None
    author: str
    course_sections: List[CreateCourseSection] = []
