#!/usr/bin/env bash
set -o errexit  # Stop the script on any error

# Install dependencies
pip install -r requirements.txt

# Collect static files for deployment
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py migrate --noinput

