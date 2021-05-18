from fastapi import FastAPI

from api import routers

app = FastAPI()

routers.setup(app)
