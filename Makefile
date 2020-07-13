

run:
	poetry run uvicorn sucuri.asgi:app --reload

migrations:
	poetry run alembic revision --autogenerate

migrate:
	poetry run alembic upgrade head

isort:
	poetry run isort -rc --atomic .

black:
	poetry run black .

flake8:
	poetry run flake8

mypy:
	poetry run mypy .

lint: flake8 mypy

format: isort black

.PHONY: run migrations migrate isort black flake8 mypy