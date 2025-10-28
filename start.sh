#!/usr/bin/env bash
set -o errexit  # Exit on error

echo "🚀 Installing dependencies..."
pip install -r requirements.txt

echo "📦 Running collectstatic..."
python manage.py collectstatic --no-input

echo "🗄️ Running database migrations..."
python manage.py migrate --no-input

echo "✅ Starting Gunicorn server..."
gunicorn myproject.wsgi:application
