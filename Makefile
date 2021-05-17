cleanup:
	find . -name __pycache__ -exec rm -rf {} + ;
	find . -name .mypy_cache -exec rm -rf {} + ;
	find . -name .pytest_cache -exec rm -rf {} + ;

run:
	MONGO_HOST=localhost \
MONGO_PORT=27017 \
MONGO_DB=PROD \
	pipenv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

run-tests:
	MONGO_HOST=localhost \
MONGO_PORT=27017 \
MONGO_DB=TEST \
	pipenv run pytest . $1

run-docker:
	docker-compose -f docker-compose.prod.yml up

run-docker-tests:
	docker-compose -f docker-compose.tests.yml up

