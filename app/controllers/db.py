from motor.motor_asyncio import AsyncIOMotorClient

from app.settings import MongoSettings

settings = MongoSettings()

client = AsyncIOMotorClient(
    settings.HOST,
    settings.PORT,
    uuidRepresentation='standard',
)

db = client[settings.DB]
