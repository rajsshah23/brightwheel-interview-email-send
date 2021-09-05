set dotenv-load := false

dev-setup:
    poetry install
    pre-commit install

run:
    poetry run uvicorn app.main:app --reload

test:
     poetry run pytest tests
