#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

python manage.py createsuperuser --username $DJANGO_SUPERUSER_USERNAME \
--password $DJANGO_SUPERUSER_PASSWORD   --email $DJANGO_SUPERUSER_EMAIL --noinput
