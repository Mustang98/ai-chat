"""
Base ORM model for all other models to inherit from.
"""

from datetime import datetime
from uuid import uuid4
from typing import ClassVar
from sqlalchemy.orm import Mapper

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData
from sqlalchemy import Table


Base = declarative_base()

utcnow = func.timezone("utc", func.now())


class BaseORMModel(Base):
    __abstract__ = True
    __mapper__: ClassVar[Mapper]
    __table__: ClassVar[Table]
    __tablename__: str
    metadata: ClassVar[MetaData]

    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    created_at = Column(
        DateTime(), default=datetime.utcnow, server_default=utcnow, nullable=False
    )
