FROM python:3.8-slim-buster

RUN pip install pipenv

COPY Pipfile /
COPY Pipfile.lock /

WORKDIR /app

RUN pipenv install

COPY . /app

CMD ["pipenv", "run", "python", "-m", "pytest"]
