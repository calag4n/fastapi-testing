from fastapi import FastAPI

from app import routers

app = FastAPI()

routers.setup(app)
