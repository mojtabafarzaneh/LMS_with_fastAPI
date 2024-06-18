from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.utils.user_util import (create_user, get_user, get_user_by_email,
                                 get_users)
from db.db_setup import get_db
from pydanti_schemas.user_schemas import User, UserCreate

router = APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(skip : int = 0, limit: int =100, db: Session = Depends(get_db)): # type: ignore
    users = get_users(db, skip=skip, limit=limit )
    return users


@router.post("/users", response_model=User)
async def create_new_user(user: UserCreate, db: Session=Depends(get_db)):
  db_user = get_user_by_email(db=db, email=user.email)
  if db_user:
    raise HTTPException(status_code=400, detail="user already exists")
  return create_user(db=db, user=user)


@router.get("/users/{user_id}")
async def read_user(id: int, db: Session=Depends(get_db)):
  db_user =get_user(db=db, user_id=id)
  if db_user is None:
    raise HTTPException(status_code=404, detail="user not found")
  return db_user



