from fastapi import Depends

from application.webapi.dependencies.adapters import resolve_todo_adapter
from domain.todo.use_cases import (
    CreateToDoUseCase,
    DoneToDoUseCase,
    FindAllToDosUseCase,
    FindToDoByIdUseCase
)
from infrastructure.todo.adapters import ToDoSqlAdapter


def resolve_create_todo_uc(
        adapter: ToDoSqlAdapter = Depends(resolve_todo_adapter)) -> CreateToDoUseCase:
    return CreateToDoUseCase(adapter)


def resolve_done_todo_uc(
        adapter: ToDoSqlAdapter = Depends(resolve_todo_adapter)) -> DoneToDoUseCase:
    return DoneToDoUseCase(adapter)


def resolve_find_all_todos_uc(
        adapter: ToDoSqlAdapter = Depends(resolve_todo_adapter)) -> FindAllToDosUseCase:
    return FindAllToDosUseCase(adapter)


def resolve_find_todo_by_id_uc(
        adapter: ToDoSqlAdapter = Depends(resolve_todo_adapter)) -> FindToDoByIdUseCase:
    return FindToDoByIdUseCase(adapter)
