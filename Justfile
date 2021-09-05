# .env is for the project, not for the Justfile.
set dotenv-load := false

dev-setup:
    poetry install
    pre-commit install

run:
    poetry run uvicorn app.main:app --reload

test:
     poetry run pytest tests
