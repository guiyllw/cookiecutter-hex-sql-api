install:
	@pipenv install

webapi-dev:
	@uvicorn --app-dir app/app --reload webapi:app

webapi:
	@uvicorn --app-dir app/app webapi:app

test-unit:
	@pytest test/unit

test-coverage:
	@pytest --cov-report html --cov=app test/unit

test-mutation:
	@mutmut run

lint:
	@isort . --check --diff
	@flake8

format:
	@isort -rc .

safety:
	@pipenv check

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@find . -name "*.cache" -type d | xargs rm -rf
	@find . -name "*htmlcov" -type d | xargs rm -rf
	@find . -name "*html" -type d | xargs rm -rf
	@rm -f .mutmut-cache
	@rm -f .coverage
	@rm -f coverage.xml



default: webapi-dev
