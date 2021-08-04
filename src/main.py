from fastapi import FastAPI, Depends
from .schemas import CreateUser
from sqlalchemy.orm import Session
from .database import get_db
from .models import User


description = """
We are teachers and so Ellie is neither complicated nor simplistic.
Ellie is just right so you can focus on teaching and your students.
Discover Ellie a modern teaching and learning platform.
"""

app = FastAPI(title="Ellie Teaching and Learning Platform", description=description, version="0.0.1",
              terms_of_service="https://ellieplatform.org/terms-and-conditions/",
              contact={"name": "Ellie Platform", "url": "https://ellieplatform.org/contact"},
              license_info={"name": "MIT", "url": "https://github.com/open-apprentice/ellie/blob/main/LICENSE"})

@app.post("/user")
def create(details: CreateUser, db: Session = Depends(get_db)):
    to_create = User(
        first_name=details.first_name,
        last_name=details.last_name,
        is_admin=details.is_admin,
        user_email=details.user_email
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id": to_create.id
    }

@app.get("/user")
def get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == id).first()

@app.delete("/user")
def delete(id: int, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == id).delete()
    db.commit()
    return { "success": True}