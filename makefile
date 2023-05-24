# Define o diretório onde o arquivo alembic.ini está localizado

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  run               to run the application"
	@echo "  test              to run the tests"
	@echo "  db-migrate        to run the database migrations create a new migration"
	@echo "  db-upgrade        to run the database migrations to the latest version"
	@echo "  db-downgrade      to run the database migrations to the previous version"
	@echo "  db-downgrade-base to run the database migrations to the base version"

db-migrate:
	cd src/adapters/gateways/databases/alembic && alembic revision --autogenerate -m "$1"

db-upgrade:
	cd src/adapters/gateways/databases/alembic && alembic upgrade head

db-downgrade:
	cd src/adapters/gateways/databases/alembic && alembic downgrade -1

db-downgrade-base:
	cd src/adapters/gateways/databases/alembic && alembic downgrade base

db-history:
	cd src/adapters/gateways/databases/alembic && alembic history

db-current:
	cd src/adapters/gateways/databases/alembic && alembic current

db-show:
	cd src/adapters/gateways/databases/alembic && alembic show

db-docker-up:
	docker-compose up -d