"""
Endpoints for user related operations.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from database.engine import get_session
from structures.user import UserRead
from database.orm_models import User

router = APIRouter()


@router.post("/users", response_model=UserRead, status_code=200, summary="Create a new user")
async def create_user(session: AsyncSession = Depends(get_session)) -> UserRead:
    """
    Create a new user with the provided user data.

    :param session: the database session.

    :return: UserRead - the newly created user with the ID.
    """
    try:
        user = User()
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return UserRead(id=user.id)
    except SQLAlchemyError:
        await session.rollback()
        raise HTTPException(
            status_code=500,
            detail="Database error while creating new user",
        )