from unittest.mock import MagicMock

import pytest

from domain.todo.models import ToDo as ToDoModel


@pytest.fixture(scope='function')
def todo_adapter_mock():
    mock = MagicMock()
    yield mock
    mock.reset_mock()


@pytest.fixture(scope='function')
def todo_model():
    todo = ToDoModel(text='Buy milk')

    return todo
