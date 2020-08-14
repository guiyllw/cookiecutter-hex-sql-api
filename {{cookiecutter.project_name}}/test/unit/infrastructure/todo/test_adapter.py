import pytest

from infrastructure.todo.adapters import ToDoSqlAdapter
from infrastructure.todo.entities import ToDo as ToDoEntity


class TestToDoSqlAdapter:

    def test_create_with_valid_entity_should_return_entity(
            self, session_mock, todo_model):

        adapter = ToDoSqlAdapter(session_mock)

        entity = adapter.create(todo_model)

        assert entity.text == todo_model.text
        assert entity.done is False

    def test_find_by_id_should_return_entity(
            self, session_mock):

        session_mock.query(ToDoEntity).get.return_value = ToDoEntity(text='Send email')

        adapter = ToDoSqlAdapter(session_mock)

        entity = adapter.find_by_id('id')

        assert entity.text == 'Send email'

    def test_find_all_should_return_list_of_entities(
            self, session_mock):

        session_mock.query(ToDoEntity).get.return_value = [
            ToDoEntity(text='Buy milk'),
            ToDoEntity(text='Send email')
        ]

        adapter = ToDoSqlAdapter(session_mock)

        entities = adapter.find_by_id('id')

        assert len(entities) == 2

        assert entities[0].text == 'Buy milk'
        assert entities[1].text == 'Send email'

    @pytest.mark.skip('No logic for test')
    def done(self, session_mock):
        pass
