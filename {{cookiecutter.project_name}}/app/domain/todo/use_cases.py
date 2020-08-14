from typing import List

from domain.todo.adapters import (
    CreateToDoAdapter,
    DoneToDoAdapter,
    FindAllToDosAdapter,
    FindToDoByIdAdapter
)
from domain.todo.models import ToDo


class CreateToDoUseCase:
    def __init__(self, create_todo_adapter: CreateToDoAdapter):
        self.create_todo_adapter = create_todo_adapter

    def create(self, todo: ToDo) -> ToDo:
        return self.create_todo_adapter.create(todo)


class DoneToDoUseCase:
    def __init__(self, done_todo_adapter: DoneToDoAdapter):
        self.done_todo_adapter = done_todo_adapter

    def done(self, id_: str):
        self.done_todo_adapter.done(id_)


class FindAllToDosUseCase:
    def __init__(self, find_all_todos_adapter: FindAllToDosAdapter):
        self.find_all_todos_adapter = find_all_todos_adapter

    def find_all(self) -> List[ToDo]:
        return self.find_all_todos_adapter.find_all()


class FindToDoByIdUseCase:
    def __init__(self, find_todo_by_id_adapter: FindToDoByIdAdapter):
        self.find_todo_by_id_adapter = find_todo_by_id_adapter

    def find_by_id(self, id_: str) -> ToDo:
        return self.find_todo_by_id_adapter.find_by_id(id_)
