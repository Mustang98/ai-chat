"""
DB engine and session management
"""
from dotenv import dotenv_values
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

# Database URL
database_url = dotenv_values(".env").get("DATABASE_URL")

# Creating the async SQLAlchemy engine
engine = create_async_engine(database_url, echo=True, future=True)

# Creating the async session maker
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncSession:
    """
    Function to provide a database session
    :return: AsyncSession
    """
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise