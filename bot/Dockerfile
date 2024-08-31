FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN pip install poetry
RUN poetry install --no-root --only main
COPY . /app
CMD ["poetry", "run", "start-bot"]