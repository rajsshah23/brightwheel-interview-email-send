# brightwheel-interview-email-send
Brightwheel Interview Question

## Build and Run
You need to have `just`, `poetry`, and `pip` installed.

1. To install `pre-commit`: `pip install pre-commit`
2. To install `just`: https://github.com/casey/just#installation
3. To install `poetry`: https://python-poetry.org/docs/#installation
4. Once you have all the above mentioned tools, navigate to the project's root dir, and run: `just dev-setup`
5. To run the tests: `just test`
6. To spin up the service: `just run`


Note: API docs will be at: http://127.0.0.1:8000/docs

## How to use the code
1. You can use the docs at http://127.0.0.1:8000/docs to interact with the code.
2. The `EMAIL_SEND_VENDOR` env variablein `.env` controls what email vendor will be used.

## How to read the code
1. The `/app` dir has the source code.
2. `app/main.py` is where FastAPI app is created.
3. `app/routes/send_email.py` has the routes defined for sending emails + checking their status.
4.  `app/setup/settings.py` has the env config for the app. It reads the values from `.env`.
5. `app/clients/email_send_client.py` is the abstract interface class for the email service.
6. `app/clients/utils.py` decides which email vendor class to create (Spendgrid or Snailgun), based on the env settings.

## Design:
- All the source code (besides the tests) is in the `/app` dir
- Tests are in the `/tests` dir
- I used polymorphism to dynamically decide, based on the configuration, what email vendor to use

I used the following technologies, and the reasons why I used them:
-  Python 3.9.7
    - I used Python because I am most comfortable with it right now.
    - 3.9.7 is the latest Python version.
- FastAPI for a web service framework
  - https://fastapi.tiangolo.com/
  - It is very fast and modern.
  - It has support to automatically generate API docs from the code
  - It natively supports dependency injection.
- Black for formatting
  - https://black.readthedocs.io/en/stable/
  - Black is an easy-to-use Python code formatter. I have personally enjoyed using it.
- Pre-commit
  - https://pre-commit.com/
  - It provides hooks for automatically formatting code + other things, before the code can be committed.
  - This ensures that the code will always be formatted according to the adopted standard.
- Justfile
  - https://github.com/casey/just
  - It is like Makefile, but without the Makefile whitespace requirements.
- Poetry for dependency management
  - https://python-poetry.org/
  - Poetry is a great way to create a virtual environment within the project, manage dependencies, and run/test the project.
- Pytest for running tests
  - I used `pytest` for running tests since I am familiar with it.



Other TODOs:
1. Add better responses for when there is an exception.
2. Add support for spinning up the app in a Docker container
3. Setup a SQL database to store the incoming requests, their send status, which email vendor was used, vendor send id, etc.
4. Add authentication to the service
