from http import HTTPStatus
from typing import List

from fastapi import Depends, HTTPException, Response
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from application.webapi.dependencies.use_cases import (
    resolve_create_todo_uc,
    resolve_done_todo_uc,
    resolve_find_all_todos_uc,
    resolve_find_todo_by_id_uc
)
from domain.todo.models import ToDo
from domain.todo.use_cases import (
    CreateToDoUseCase,
    DoneToDoUseCase,
    FindAllToDosUseCase,
    FindToDoByIdUseCase
)

router = InferringRouter()


@cbv(router)
class ToDoCBV:

    create_todo_uc: CreateToDoUseCase = Depends(resolve_create_todo_uc)
    done_todo_uc: DoneToDoUseCase = Depends(resolve_done_todo_uc)
    find_all_todos_uc: FindAllToDosUseCase = Depends(resolve_find_all_todos_uc)
    find_todo_by_id_uc: FindToDoByIdUseCase = Depends(resolve_find_todo_by_id_uc)

    @router.post('/')
    async def create(self, todo: ToDo) -> ToDo:
        return self.create_todo_uc.create(todo)

    @router.patch('/{id_}')
    async def done(self, id_: str):
        if self.find_todo_by_id_uc.find_by_id(id_) is None:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

        self.done_todo_uc.done(id_)

        return Response(status_code=HTTPStatus.OK)

    @router.get('/')
    async def find_all(self) -> List[ToDo]:
        return self.find_all_todos_uc.find_all()

    @router.get('/{id_}')
    async def find_by_id(self, id_: str) -> ToDo:
        todo = self.find_todo_by_id_uc.find_by_id(id_)
        if not todo:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND)

        return todo
