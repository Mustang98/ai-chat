"""
Endpoints for messages related operations.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from structures.message import MessageCreate, MessageRead
from database.engine import get_session
from database.orm_models import Dialogue, Message

router = APIRouter()


@router.post("/messages", response_model=MessageRead)
async def create_message(message: MessageCreate, session: AsyncSession = Depends(get_session)) -> MessageRead:
    """
    Create a new message from user and generate character's reply.

    :param message: message content and dialogue id.
    :param session: the database session.

    :return: reply message generated by the bot
    """
    try:
        dialogue = await session.get(Dialogue, message.dialogue_id)
        if dialogue is None:
            raise HTTPException(
                status_code=400,
                detail=f"Dialogue with id={message.dialogue_id} doesn't exist",
            )
        # Save user message to database
        user_message_orm = Message(content=message.content, dialogue_id=message.dialogue_id, sender_type="user")
        session.add(user_message_orm)
        await session.commit()

        # Generate bot reply
        bot_reply_content = "I agree that " + message.content
        bot_message_orm = Message(content=bot_reply_content, dialogue_id=message.dialogue_id, sender_type="bot")
        session.add(user_message_orm)
        await session.commit()

        return MessageRead(id=bot_message_orm.id, content=bot_message_orm.content)

    except SQLAlchemyError:
        await session.rollback()
        raise HTTPException(
            status_code=500,
            detail="Database error while creating new message",
        )