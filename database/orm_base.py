"""
Base ORM model for all other models to inherit from.
"""

import uuid
from datetime import datetime
from uuid import uuid4
from typing import ClassVar
from sqlalchemy.orm import Mapper
from typing import TypeVar

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy_utils import force_instant_defaults


OrmModel = TypeVar("OrmModel", bound="BaseORMModel")

meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)
Base = declarative_base(metadata=meta)

utcnow = func.timezone("utc", func.now())

force_instant_defaults()


class BaseORMModel(Base):
    __abstract__ = True
    __mapper__: ClassVar[Mapper]
    __table__: ClassVar[Table]
    __tablename__: str
    metadata: ClassVar[MetaData]

    id = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid4, server_default=func.gen_random_uuid()
    )
    created_at: datetime = Column(
        DateTime(), default=datetime.utcnow, server_default=utcnow, nullable=False
    )
