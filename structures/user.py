"""
Pydantic CRUD structure(s) for User entity.
"""
from pydantic import BaseModel, UUID4


class UserRead(BaseModel):
    """
    Structure for a response with a newly created User.
    """
    id: UUID4
