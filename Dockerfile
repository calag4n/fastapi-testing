# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster as builder
WORKDIR /fastapi-testing
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install --upgrade pip
RUN pip install pipenv

FROM builder AS prod
RUN pipenv install --system --skip-lock
COPY app ./app

FROM builder AS tests
RUN pipenv install --system --skip-lock --dev
COPY app ./app
COPY tests ./tests

