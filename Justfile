set dotenv-load := false

dev-setup:
    poetry install
    pre-commit install


non-docker-run:
    poetry run uvicorn app.main:app --reload
