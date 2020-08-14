import operator
from datetime import datetime

import stringcase
from pydantic import BaseModel


class SerializableModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        ignore_extra = True
        orm_mode = True

        alias_generator = stringcase.camelcase
        json_encoders = {
            datetime: operator.methodcaller('isoformat')
        }
