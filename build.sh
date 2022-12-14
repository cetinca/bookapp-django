#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate

# on the first run creates superuser in the DB
#python manage.py createsuperuser --noinput \
#--username $DJANGO_SUPERUSER_USERNAME \
#--email $DJANGO_SUPERUSER_EMAIL
