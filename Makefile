.PHONY: up down migrations migrate test

up:
	docker-compose up -d --build --remove-orphans --force-recreate

down:
	docker-compose down

migrations:
	docker-compose exec backend alembic revision --autogenerate -m "$(date +'%Y%m%d%H%M%S')"

migrate:
	docker-compose exec backend alembic upgrade head

test:
	docker-compose -f docker-compose.test.yml up --build | grep -v 'test_db'