"""
Endpoints for user related operations.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database.engine import get_session
from structures.user import UserRead
from database.orm_models import User

import logging

router = APIRouter()


@router.post("/users", response_model=UserRead, status_code=200, summary="Create a new user")
async def create_user(session: Session = Depends(get_session)):
    """
    Create a new user with the provided user data.

    :param session: the database session.

    :return: UserRead - the newly created user with the ID.
    """
    logging.info(f"OLEG TEST")
    try:
        user = User()
        session.add(user)
        session.commit()
        session.refresh(user)
        return UserRead(id=user.id)
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Database error while creating a new user."
        )
