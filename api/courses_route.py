from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.utils.courses_util import create_course, get_course, get_courses
from db.db_setup import get_db
from pydanti_schemas.courses_schemas import Course, CourseCreate

router = APIRouter()


@router.get("/courses", response_model=List[Course])
async def read_users(skip : int = 0, limit: int =100, db: Session = Depends(get_db)): # type: ignore
    courses = get_courses(db, skip=skip, limit=limit )
    return courses


@router.post("/courses", response_model=Course)
async def create_new_course(course: CourseCreate, db: Session=Depends(get_db)):
    return create_course(db=db, course=course)


@router.get("/courses/{course_id}")
async def read_course(id: int, db: Session = Depends(get_db)):
    db_course = get_course(db=db, course_id=id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

