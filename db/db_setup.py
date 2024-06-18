
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:mojtaba7878@localhost/async"
SQLALCHEMY_ASYNC_DATABASE_URL = "postgresql+asyncpg://postgres:mojtaba7878@localhost/async"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True # type: ignore
)

async_engine = create_async_engine(SQLALCHEMY_ASYNC_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True
    )

AsyncSessionLocal = sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False # type: ignore
) # type: ignore

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_async_db():
    async with AsyncSessionLocal() as db: # type: ignore
        yield db
        await db.commit()
