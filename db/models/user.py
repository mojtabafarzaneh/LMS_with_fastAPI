import enum

from sqlalchemy import Boolean, Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from db.db_setup import Base
from db.models.mixins import Timestamp


class Role(enum.Enum):
    Teacher = 1
    Student = 2


class User(Base, Timestamp):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Integer, Enum(Role), default= Role.Student)
    is_avtive = Column(Boolean, default=False)


    profile = relationship("Profile",back_populates="owner", uselist=False)


class Profile(Base, Timestamp):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False )
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("user", back_populates="profile")