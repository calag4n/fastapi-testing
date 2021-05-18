from fastapi import FastAPI

from . import users


def setup(app: FastAPI) -> None:
    users.setup(app)
