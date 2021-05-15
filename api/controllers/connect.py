import logging

from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
database_name = "PROD_DB"
users_collection = "users"


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client[database_name]


async def connect_to_mongo():
    logging.info("Connecting mongoDB...")
    db.client = AsyncIOMotorClient(
        MONGO_URI,
        uuidRepresentation="standard",
    )
    logging.info("Connected！")


async def close_mongo_connection():
    logging.info("Disconnecting mongoDB...")
    db.client.close()
    logging.info("Disconnected !")
