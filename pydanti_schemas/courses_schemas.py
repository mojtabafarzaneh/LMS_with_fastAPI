from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    user_id : int


class CourseCreate(CourseBase):
    ...


class Course(CourseBase):
    id: int


    class Config:
        from_attributes = True