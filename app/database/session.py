from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator

from app.config import settings

# Creating async engine
async_engine = create_async_engine(
    url=settings.GET_DATABASE_URL
)

# Creating async sessionmaker
async_session = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Session dependency for database queries
async def get_session() -> AsyncGenerator:
    try:
        session: AsyncSession = async_session()
        yield session
    finally:
        await session.close()