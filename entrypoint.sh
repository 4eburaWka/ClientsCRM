#!/bin/bash
set -e

echo "Try to migrate..."
until uv run manage.py migrate; do
    sleep 2
done

exec uv run gunicorn --bind 0.0.0.0:8000 crm.wsgi:application 