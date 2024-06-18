from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from api.courses_route import router as courses_router
from api.users_route import router as user_router
from api.utils.courses_util import get_course
from db.db_setup import Base, engine, get_db
from db.models import course, user

course.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)



app = FastAPI(
    title="Fast API MLS",
    description="MLS for managing studants and courses",
    version="0.0.1",
    license_info={
        "name": "MIT"
    },
)

app.include_router(user_router)
app.include_router(courses_router)
