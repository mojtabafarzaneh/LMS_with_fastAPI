import typing
from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

users : list[typing.Any] = []

class User(BaseModel):
    email : str
    is_active : bool
    bio : Optional[str]


@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def post_user(user: User):
    users.append(user)
    return "success"

@router.get("/users/{id}")
async def get_user(id:int):
    return {"user": users[id]}

