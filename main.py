from fastapi import FastAPI

from api.users import router as user_router
from db.db_setup import Base, engine
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