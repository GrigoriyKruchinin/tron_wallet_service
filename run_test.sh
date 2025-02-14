#!/bin/bash

echo "🚀 Waiting for PostgreSQL..."
wait-for-it db:5432 --timeout=30 --strict

echo "🚀 Applying migrations..."
alembic upgrade head

echo "🔄 Starting tests..."
pytest -v
