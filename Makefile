-include .env
export


.PHONY: docs


shell: ## This has to be executed outside the Makefile.
	@echo 'Run $ pipenv shell'


start:
	@uvicorn main:app --reload


up:
	@docker-compose up -d


down:
	@docker-compose down


src_files := {api,database,repository,tests,usecase}
lint:
	@# Make sure to run this in pipenv shell
	black ${src_files} # Format code.
	flake8 ${src_files} # Run analysis.
	isort ${src_files} # Sort imports.
	mypy ${src_files} # Run static type checking.
	#pylint .


sql: # Creates a new migration file.
	@alembic revision -m $(name)


migrate: # Runs migration.
	@alembic upgrade head


rollback: # Rollback migration by one step.
	@alembic downgrade -1


reset: # Resets the database.
	@alembic downgrade base


psql: # Access the postgres shell.
	@PGPASSWORD=$(DB_PASS) docker-compose exec db psql -U $(DB_USER) $(DB_NAME)


docs:
	@open http://localhost:8000/docs


test:
	PYTHONPATH=. pytest tests
