#!/bin/bash

echo "🚀 Waiting for PostgreSQL..."
wait-for-it db:5432 --timeout=30 --strict

echo "🚀 Applying migrations..."
alembic upgrade head

echo "🔄 Starting tests..."
pytest -v --maxfail=5 --disable-warnings --tb=short

if [ $? -eq 0 ]; then
  echo "✅ Tests passed successfully!"
else
  echo "❌ Tests failed."
  exit 1
fi