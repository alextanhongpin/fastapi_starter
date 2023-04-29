-include .env
export

shell: ## This has to be executed outside the Makefile.
	@echo 'Run $ pipenv shell'


start:
	@uvicorn main:app --reload


up:
	@docker-compose up -d


down:
	@docker-compose down


sql-%:
	@alembic revision -m '$*'


migrate:
	@alembic upgrade head


rollback:
	@alembic downgrade -1


reset:
	@alembic downgrade base
