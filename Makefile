# app
up:
	docker compose -f docker-compose.yml up -d --build --force-recreate --remove-orphans

watch:
	DEV_MODE=true docker compose -f docker-compose.yml watch

stop:
	docker compose -f docker-compose.yml stop

rm:
	docker compose -f docker-compose.yml down

logs:
	docker compose -f docker-compose.yml logs


# alembic
makemigration:
	docker compose exec -e PYTHONPATH=/project/src app poetry run alembic revision --autogenerate -m "$(name)"

history:
	docker compose exec -e PYTHONPATH=/project/src app poetry run alembic history --verbose
