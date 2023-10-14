import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
host = os.getenv('POSTGRES_HOST')
db_name = os.getenv('POSTGRES_DB')


DATABASE_URL = f'postgresql+asyncpg://{user}:{password}@{host}/{db_name}'
engine = create_async_engine(DATABASE_URL, future=True)


async_session: AsyncSession = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    future=True,
)

Base = declarative_base()


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
