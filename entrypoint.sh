#!/bin/sh
set -e

echo "Waiting for postgres..."
while ! pg_isready -h $DATABASE_HOST -p $DATABASE_PORT -U $DATABASE_USER
do
  echo "Database is not ready yet. Retrying in 2 seconds..."
  sleep 2
done
echo "PostgreSQL started"

python manage.py migrate --noinput

python manage.py collectstatic --noinput

exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3