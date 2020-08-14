from typing import List

from domain.todo.adapters import (
    CreateToDoAdapter,
    DoneToDoAdapter,
    FindAllToDosAdapter,
    FindToDoByIdAdapter
)
from domain.todo.models import ToDo as ToDoModel
from infrastructure.todo.entities import ToDo as ToDoEntity


class ToDoSqlAdapter(CreateToDoAdapter,
                     DoneToDoAdapter,
                     FindAllToDosAdapter,
                     FindToDoByIdAdapter):

    def __init__(self, session):
        self.session = session

    def create(self, todo: ToDoModel) -> ToDoEntity:
        todo_entity = ToDoEntity.from_model(todo)

        self.session.add(todo_entity)
        self.session.commit()

        return todo_entity

    def find_by_id(self, id_: str) -> ToDoEntity:
        return self.session.query(ToDoEntity).get(id_)

    def find_all(self) -> List[ToDoEntity]:
        return self.session.query(ToDoEntity).all()

    def done(self, id_: str):
        todo = self.session.query(ToDoEntity).filter_by(id_=id_).first()
        todo.done = True

        self.session.commit()
