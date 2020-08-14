from fastapi import Depends
from sqlalchemy.orm import Session

from application.webapi.dependencies.database import resolve_db_session
from infrastructure.todo.adapters import ToDoSqlAdapter


def resolve_todo_adapter(session: Session = Depends(resolve_db_session)):
    return ToDoSqlAdapter(session)
