"""
Contains all ORM models for corresponding database tables.
"""
import uuid

from sqlalchemy import Column, Text, ForeignKey
from sqlalchemy.orm import relationship
from database.orm_base import BaseORMModel


class User(BaseORMModel):
    """
    User ORM model representing the 'users' table.
    """
    __tablename__ = "users"

    dialogues = relationship("Dialogue", back_populates="user")


class Character(BaseORMModel):
    """
    Character ORM model representing the 'characters' table.
    """
    __tablename__ = "characters"

    name = Column(Text, nullable=False)
    dialogues = relationship("Dialogue", back_populates="character")


class Dialogue(BaseORMModel):
    """
    Dialogue ORM model representing the 'dialogues' table.
    """

    __tablename__ = "dialogues"

    messages = relationship("Message", back_populates="dialogue")

    user_id = Column(ForeignKey(User.id), nullable=False, index=True)
    user = relationship(User, back_populates="dialogues")

    character_id = Column(ForeignKey(Character.id), nullable=False, index=True)
    character = relationship(Character, back_populates="dialogues")


class Message(BaseORMModel):
    """
    Message ORM model representing the 'messages' table.
    """
    __tablename__ = "messages"

    content = Column(Text)

    dialogue_id = Column(ForeignKey(Dialogue.id), nullable=False, index=True)
    dialogue = relationship(Dialogue, back_populates="messages")