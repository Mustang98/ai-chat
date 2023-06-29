"""
Endpoints for dialogue related operations.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
import logging

from database.engine import get_session
from database.orm_models import Dialogue, User, Character, Message
from structures.dialogue import DialogueCreate, DialogueRead
from structures.message import MessageRead

router = APIRouter()


@router.post("/dialogues", response_model=DialogueRead)
async def create_or_read_dialogue(dialogue_create: DialogueCreate, session: AsyncSession = Depends(get_session)) -> DialogueRead:
    """
    Create a new dialogue or return an existing one.

    :param dialogue_create: user and character id of dialogue to create.
    :param session: the database session.

    :return: information about dialogue and its messages.
    """
    try:
        # Check if the user exists
        user = await session.get(User, dialogue_create.user_id)
        if user is None:
            raise HTTPException(
                status_code=400,
                detail=f"User with id={dialogue_create.user_id} doesn't exist",
            )
        # Check if the character exists
        character = await session.get(Character, dialogue_create.character_id)
        if character is None:
            raise HTTPException(
                status_code=400,
                detail=f"Character with id={dialogue_create.character_id} doesn't exist",
            )

        # Check if the dialogue already exists
        dialogue = (
            await session.execute(
                select(Dialogue)
                .options(joinedload(Dialogue.messages))
                .where(
                    Dialogue.user_id == dialogue_create.user_id,
                    Dialogue.character_id == dialogue_create.character_id
                )
            )
        ).unique().scalar_one_or_none()
        logging.info("OLEG dialogue: %s", dialogue)
        if dialogue:
            dialogue.messages.sort(key=lambda message: message.created_at)
            # Dialogue already exists, return its information
            return DialogueRead(
                id=dialogue.id,
                messages=[
                    MessageRead(id=message.id, content=message.content, sender_type=message.sender_type)
                    for message in dialogue.messages
                ]
            )
        else:
            # Create a new dialogue
            new_dialogue = Dialogue(
                user_id=dialogue_create.user_id,
                character_id=dialogue_create.character_id
            )
            session.add(new_dialogue)
            await session.commit()

            return DialogueRead(
                id=new_dialogue.id,
                messages=[]
            )
    except SQLAlchemyError:
        await session.rollback()
        raise HTTPException(
            status_code=500,
            detail="Database error while creating new dialogue",
        )


