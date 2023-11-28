#!/bin/sh

dockerize -wait tcp://psql:5432 -timeout 2m

FLAG_FILE="/djangoapp/initial_setup_done.flag"

if [ ! -f $FLAG_FILE ]; then
    echo "Executando comandos de configuração inicial..."

    python manage.py makemigrations client
    python manage.py migrate_schemas --shared
    python manage.py create_tenant --domain-domain=$APP_DOMAIN --schema_name="public" --name=$APP_NAME --domain-is_primary=True


    touch $FLAG_FILE
else
    echo "Configuração inicial já foi concluída anteriormente."
fi

python manage.py runserver 0.0.0.0:8000
