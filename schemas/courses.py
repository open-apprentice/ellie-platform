from typing import List

from datetime import date
from pydantic import BaseModel


class Course(BaseModel):
    course_name: str
    is_draft: bool
    is_published: bool
    date_published: date = None
    last_updated: date = None
    author: str


class CreateCourseSectionBase(BaseModel):
    course_section_name: str
    date_published: date = None
    last_updated: date = None
    course_section_is_draft: bool
    course_section_is_complete: bool
    course_section_purpose: str
    course_section_order: int


class CreateCourseSectionPayload(CreateCourseSectionBase):
    """How we call the FastAPI endpoint"""
    course_ids: List[int]


class CreateCourseSectionObject(CreateCourseSectionBase):
    """How we create the SA object"""
    courses: List[Course]


class CreateCourse(Course):
    course_sections: List[CreateCourseSectionBase] = []
