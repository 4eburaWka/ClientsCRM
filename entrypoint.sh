#!/bin/bash
set -e

echo "Try to migrate..."
until uv run manage.py migrate; do
    sleep 2
done

exec uv run manage.py runserver 