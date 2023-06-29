"""
Base ORM model for all other models to inherit from.
"""

import uuid
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base


Base = declarative_base()

utcnow = func.timezone("utc", func.now())


class BaseORMModel(Base):
    id: uuid.UUID = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    created_at: datetime = Column(
        DateTime(), default=datetime.utcnow, server_default=utcnow, nullable=False
    )
