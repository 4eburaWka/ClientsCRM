FROM python:3.13-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY pyproject.toml .

RUN uv sync

COPY . .

EXPOSE 8000

RUN chmod +x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]