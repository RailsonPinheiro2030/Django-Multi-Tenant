#!/bin/sh
set -e

echo "DB_HOST: $POSTGRES_HOST"
echo "DB_PORT: $POSTGRES_PORT"

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST:$POSTGRES_PORT) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"


python manage.py runserver 0.0.0.0:8000
