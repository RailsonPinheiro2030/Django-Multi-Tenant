#!/bin/sh
set -e

echo "DB_HOST: $POSTGRES_HOST"
echo "DB_PORT: $POSTGRES_PORT"

echo "DOMAIN_NAM: $DOMAIN_NAME"
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST:$POSTGRES_PORT) ..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

python manage.py makemigrations --noinput
#python manage.py create_tenant --schema_name=public --nome=$APP_NAME --trial=False --domain-is_primary=True --domain-domain=$DOMAIN_NAME --noinput
python manage.py migrate_schemas --shared --noinput
python manage.py runserver 0.0.0.0:8000
