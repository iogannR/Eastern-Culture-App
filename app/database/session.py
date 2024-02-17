import sqlalchemy.ext.asyncio as sa_ext_asyncio
import sqlalchemy.orm as sa_orm
import typing

from app.config import settings

# Creating async engine
async_engine = sa_ext_asyncio.create_async_engine(
    url=settings.GET_DATABASE_URL
)

# Creating async sessionmaker
async_session = sa_orm.sessionmaker(
    bind=async_engine,
    class_=sa_ext_asyncio.AsyncSession,
    expire_on_commit=False
)

# Session dependency for database queries
async def get_session() -> typing.AsyncGenerator:
    try:
        session: sa_ext_asyncio.AsyncSession = async_session()
        yield session
    finally:
        await session.close()