from api.controllers.connect import close_mongo_connection, connect_to_mongo
from fastapi import FastAPI
from api.routers import users

app = FastAPI()

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

app.include_router(users.router)