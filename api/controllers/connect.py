from motor.motor_asyncio import AsyncIOMotorClient

import settings


client = AsyncIOMotorClient(
    settings.MONGO_HOST,
    settings.MONGO_PORT,
    uuidRepresentation="standard",
)

db = client[settings.MONGO_DB]
