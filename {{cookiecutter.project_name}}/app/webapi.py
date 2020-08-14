from http import HTTPStatus
from typing import Dict

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from application.webapi.health.controller import router as health_router
from application.webapi.todo.controller import router as todo_router

app = FastAPI(title='Hexagonal ToDo Api',
              description='Template for hexagonal api')


def configure_handlers():
    def format_error(exc: Exception) -> Dict:
        return {'detail': str(exc)}

    @app.exception_handler(Exception)
    async def exception_handler(request: Request,
                                exc: Exception) -> JSONResponse:

        return JSONResponse(content=format_error(exc),
                            status_code=HTTPStatus.INTERNAL_SERVER_ERROR)


def configure_routes():
    app.include_router(health_router)

    app.include_router(
        router=todo_router,
        prefix='/todo',
        tags=['ToDo']
    )


def configure():
    configure_routes()
    configure_handlers()


configure()
