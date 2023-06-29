"""
Pydantic CRUD structure(s) for Message entity.
"""
from pydantic import BaseModel, UUID4


class MessageRead(BaseModel):
    """
    Structure for a response with a message info.
    """
    id: UUID4
    content: str
    sender_type: str


class MessageCreate(BaseModel):
    """
    Structure for a new message info.
    """
    dialogue_id: UUID4
    content: str
    