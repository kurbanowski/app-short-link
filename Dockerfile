FROM python:3.12.3-slim
ENV POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_HOME="/opt/poetry" \
    PATH="/root/.local/bin:$PATH"
WORKDIR /app

RUN pip install poetry && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root
