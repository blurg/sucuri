# sucuri
plataforma que possa centralizar informações como projetos e cursos de tecnologia, com curadoria e CdC



## Install Project
```
pyenv local 3.8.3
python -m venv .venv
source .venv/bin/activate
poetry install
```

## Create Migration
```
poetry run alembic revision --autogenerate -m 'initial migration'
```

## Run Migration
```
poetry run alembic upgrade head
```