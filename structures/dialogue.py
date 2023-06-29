"""
Pydantic CRUD structure(s) for Dialogue entity.
"""
from pydantic import BaseModel, UUID4
from message import MessageRead


class DialogueCreate(BaseModel):
    """
    Structure for a new dialogue info.
    """
    user_id: UUID4
    character_id: UUID4


class DialogueRead(BaseModel):
    """
    Structure for a response with a dialogue info.
    """
    id: UUID4
    messages: list[MessageRead]
