cleanup:
	find . -name __pycache__ -exec rm -rf {} + ;
	find . -name .mypy_cache -exec rm -rf {} + ;
	find . -name .pytest_cache -exec rm -rf {} + ;
	rm -rf mongo_db

run:
	MONGO_HOST=localhost \
MONGO_PORT=27017 \
MONGO_DB=PROD \
	python main.py

run-tests:
	MONGO_HOST=localhost \
MONGO_PORT=27017 \
MONGO_DB=TEST \
	pipenv run tests

stop-docker:
	docker-compose -f docker-compose.prod.yml stop

rm-docker:
	docker-compose -f docker-compose.prod.yml rm --force

run-docker:
	docker-compose -f docker-compose.prod.yml up

build-docker:
	docker-compose -f docker-compose.prod.yml up --build

stop-docker-tests:
	docker-compose -f docker-compose.tests.yml stop

rm-docker-tests:
	docker-compose -f docker-compose.tests.yml rm --force

run-docker-tests:
	docker-compose -f docker-compose.tests.yml up --build
