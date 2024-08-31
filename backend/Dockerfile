FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry gunicorn

RUN poetry config virtualenvs.create false && poetry install --no-root

COPY . /app/

RUN mkdir -p /app/_backend/logs
RUN mkdir -p /app/logs

RUN chmod +x /app/run.sh

CMD ["./run.sh"]