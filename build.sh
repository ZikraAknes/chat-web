#!/usr/bin/env bash

set -o errexit

pip3 install -r requirements.txt

# Make sure static files are properly collected
python3 manage.py collectstatic --noinput

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py populate_data