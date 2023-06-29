"""
Pydantic CRUD structure(s) for Character entity.
"""
from pydantic import BaseModel, UUID4


class CharacterRead(BaseModel):
    """
    Structure for a response with a single Character info.
    """
    id: UUID4
    name: str


class CharactersRead(BaseModel):
    """
    Structure for a response with a list of Characters info.
    """
    characters: list[CharacterRead]
