#!/bin/bash

echo "🚀 Waiting for PostgreSQL..."
wait-for-it db:5432 --timeout=30 --strict

echo "🚀 Applying migrations..."
alembic upgrade head

echo "🔄 Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
