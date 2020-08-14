import abc
from typing import List

from domain.todo.models import ToDo


class CreateToDoAdapter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self, todo: ToDo) -> ToDo:
        pass  # pragma: no cover


class DoneToDoAdapter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def done(self, id_: str):
        pass  # pragma: no cover


class FindAllToDosAdapter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_all(self) -> List[ToDo]:
        pass  # pragma: no cover


class FindToDoByIdAdapter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_by_id(self, id_: str) -> ToDo:
        pass  # pragma: no cover
