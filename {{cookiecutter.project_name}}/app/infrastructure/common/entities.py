from uuid import uuid4

from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func


class BaseEntity:
    id_ = Column('id', String(36),
                 primary_key=True,
                 default=lambda: str(uuid4()))

    created_at = Column(DateTime(timezone=True),
                        default=func.now())

    updated_at = Column(DateTime(timezone=True),
                        default=func.now(), onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        return cls.__name__

    @classmethod
    def from_model(cls, model):
        entity = cls()
        entity.__dict__.update(model.dict())

        return entity
