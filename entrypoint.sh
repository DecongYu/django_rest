#!/bin/sh

if [ "$DATABASE" = "postgres"]
then
    echo "waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "Postgres started"
fi

pyhton manage.py flush --no-input
pyhton manage.py migrate

exec "$@"