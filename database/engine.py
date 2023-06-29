"""
DB engine and session management
"""
import os

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

# Database URL
database_url = os.environ.get("DATABASE_URL")

# Creating the async SQLAlchemy engine
engine = create_async_engine(database_url, echo=True, future=True)

# Creating the async session maker
session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    """
    Function to provide a database session
    :return: AsyncSession
    """
    async with session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise