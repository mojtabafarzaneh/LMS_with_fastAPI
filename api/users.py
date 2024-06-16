import typing
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.utils.user_util import (create_user, get_user, get_user_by_email,
                                 get_users)
from db.db_setup import get_db
from pydanti_schemas.user import User, UserCreate

router = APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(skip : int = 0, limit: int =100, db: Session = Depends(get_db)): # type: ignore
    users = get_users(db, skip=skip, limit=limit )
    return users


#@router.post("/users")
#async def create_new_user(user: User):
 #   users.append(user)
  #  return "success"

#@router.get("/users/{id}")
#async def read_user(id:int):
  ##  return {"user": users[id]}

