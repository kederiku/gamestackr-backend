.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall; poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: migrate
migrate:
	poetry run python -m gamestackr.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m gamestackr.manage makemigrations

.PHONY: run-server
run-server:
	poetry run python -m gamestackr.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m gamestackr.manage createsuperuser

.PHONY: docker-cleanup
docker-cleanup:
	docker image prune -f
	docker builder prune -f

.PHONY: test
test:
	poetry run pytest -v -rs -n auto --show-capture=no

.PHONY: test-detailed
test-detailed:
	poetry run pytest -vv -rs -s

.PHONY: up-dependencies-only
up-dependencies-only:
	test -f .env || touch .env
	docker compose -f docker-compose.dev.yaml up --force-recreate db

.PHONY: update
update: install migrate install-pre-commit ;
