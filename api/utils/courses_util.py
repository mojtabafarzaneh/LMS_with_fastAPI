from turtle import title

from sqlalchemy.orm import Session

from db.models.course import Course
from pydanti_schemas.courses_schemas import CourseCreate


def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()



def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Course).offset(skip).limit(limit).all()


def create_course(db: Session, course: CourseCreate):
    db_course = Course(
        title = course.title,
        description = course.description,
        user_id = course.user_id
        ) # type: ignore
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course