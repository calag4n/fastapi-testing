from fastapi import FastAPI

from .routers import users

app = FastAPI()

users.setup(app)
