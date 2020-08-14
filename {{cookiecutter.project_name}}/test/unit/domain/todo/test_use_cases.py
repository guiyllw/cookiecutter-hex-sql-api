import pytest

from domain.todo.use_cases import CreateToDoUseCase, FindAllToDosUseCase, FindToDoByIdUseCase
from infrastructure.todo.entities import ToDo as ToDoEntity


class TestCreateToDoUseCase:

    def test_create_todo_with_valid_body_should_return_created_todo(
            self, todo_model, todo_adapter_mock):

        todo_adapter_mock.create.return_value = ToDoEntity.from_model(todo_model)

        create_todo_uc = CreateToDoUseCase(todo_adapter_mock)

        created_todo = create_todo_uc.create(todo_model)

        assert created_todo.text == todo_model.text
        assert created_todo.done is False


class TestDoneToDoUseCase:

    @pytest.mark.skip('No logic for test')
    def test_done_todo_with_should_success_silently(self, todo_model, todo_adapter_mock):
        pass


class TestFindAllToDosUseCase:

    def test_find_all_todos_should_return_list_of_todos(
            self, todo_model, todo_adapter_mock):

        todo_adapter_mock.find_all.return_value = [
            ToDoEntity(text='Buy milk'),
            ToDoEntity(text='Send email')
        ]

        find_all_todos_uc = FindAllToDosUseCase(todo_adapter_mock)

        todos = find_all_todos_uc.find_all()

        assert len(todos) == 2

        assert todos[0].text == 'Buy milk'
        assert todos[1].text == 'Send email'


class TestFindToDoByIdUseCase:

    def test_done_todo_with_should_success_silently(
            self, todo_model, todo_adapter_mock):

        todo_adapter_mock.find_by_id.return_value = ToDoEntity(text='Buy milk')

        find_todo_by_id_uc = FindToDoByIdUseCase(todo_adapter_mock)

        todo = find_todo_by_id_uc.find_by_id('id')

        assert todo.text == 'Buy milk'
