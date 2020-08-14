from sqlalchemy import Boolean, Column, String

from infrastructure.common.database import Base
from infrastructure.common.entities import BaseEntity


class ToDo(Base, BaseEntity):

    text = Column(String(36), nullable=False)
    done = Column(Boolean, nullable=False, default=False)
