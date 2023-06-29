"""
Endpoints for characters related operations.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database.engine import get_session
from database.orm_models import Character
from structures.character import CharacterRead, CharactersRead

router = APIRouter()


@router.get("/characters", response_model=CharactersRead)
async def get_characters(session: AsyncSession = Depends(get_session)) -> CharactersRead:
    """
    Get list of existing characters.

    :param session: the database session.

    :return: CharactersRead - list of data for each character.
    """
    characters = await session.execute(select(Character))
    characters_read = CharactersRead(characters=[CharacterRead(id=character.id,
                                                               name=character.name)
                                                 for character in characters.scalars()])
    return characters_read
