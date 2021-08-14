from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from database.db import get_db

from models.users import User
from models.courses import Course, CourseSection
from schemas.users import PydanticUser
from schemas.courses import (PydanticCourse,
                             PydanticCourseSection)

from docs_config import docsettings as docs

app = FastAPI(
    title=docs.title,
    description=docs.description,
    openapi_tags=docs.openapi_tags,
    version=docs.version,
    terms_of_service=docs.terms_of_service,
    contact=docs.contact,
    license_info=docs.license_info,
)


@app.get("/", tags=["index"], response_class=HTMLResponse)
def index():
    return """
    <html>
        <head>
            <title>Ellie - Learning and Teaching Platform</title>
        </head>
        <body>
            <h1>Ellie - Learning and Teaching Platform</h1>
            <ul>
                <li><a href="http://localhost:8000/docs">API Documentation</a></li>
            </ul>
        </body>

    </html>
    """  # noqa E501


@app.post("/user", status_code=201, tags=["create-user"])
def create_user(details: PydanticUser, db: Session = Depends(get_db)):
    user = User(
        first_name=details.first_name,
        last_name=details.last_name,
        is_admin=details.is_admin,
        user_email=details.user_email,
    )
    db.add(user)
    db.commit()
    return {"success": True, "created_id": user.id}


@app.get("/user", tags=["get-user"])
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == id).first()


@app.delete("/user", tags=["delete-user"])
def delete_user(id: int, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == id).delete()
    db.commit()
    return {"success": True}


@app.post("/course", status_code=201, tags=["create-course"])
def create_course(details: PydanticCourse, db: Session = Depends(get_db)):
    course = Course(
        course_name=details.course_name,
        is_draft=details.is_draft,
        is_published=details.is_published,
        date_published=details.date_published,
        last_updated=details.last_updated,
        author=details.author,
        course_sections=details.course_sections,
    )
    db.add(course)
    db.commit()
    return {"success": True, "created_id": course.id}


@app.get("/course", tags=["get-course"])
def get_course_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Course).filter(Course.id == id).first()


@app.delete("/course", tags=["delete-course"])
def delete_course(id: int, db: Session = Depends(get_db)):
    db.query(Course).filter(Course.id == id).delete()
    db.commit()
    return {"success": True}


@app.post("/course-section", status_code=201, tags=["create-course-section"])
def create_course_section(details: PydanticCourseSection,
                          db: Session = Depends(get_db)):
    course_ids = details.course_ids
    courses = db.query(Course).filter(
        Course.id.in_(course_ids)
    ).all()
    if not courses:
        error = f"No courses found for course ids {course_ids}"
        raise HTTPException(status_code=400, detail=error)

    course = CourseSection(
        course_section_name=details.course_section_name,
        date_published=details.date_published,
        last_updated=details.last_updated,
        course_section_is_draft=details.course_section_is_draft,
        course_section_is_complete=details.course_section_is_complete,
        course_section_purpose=details.course_section_purpose,
        course_section_order=details.course_section_order,
        courses=courses
    )
    db.add(course)
    db.commit()
    return {"success": True, "created_id": course.id}


@app.get("/course-section", tags=["get-course-section"])
def get_course_section_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(CourseSection).filter(CourseSection.id == id).first()


@app.delete("/course-section", tags=["delete-course-section"])
def delete_course_section(id: int, db: Session = Depends(get_db)):
    db.query(CourseSection).filter(CourseSection.id == id).delete()
    db.commit()
    return {"success": True}
