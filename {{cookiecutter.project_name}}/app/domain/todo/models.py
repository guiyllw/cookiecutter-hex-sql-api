from pydantic import Field

from domain.common.models import SerializableModel


class ToDo(SerializableModel):

    text: str = Field()
    done: bool = False
