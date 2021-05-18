from api.settings import MongoSettings
from motor.motor_asyncio import AsyncIOMotorClient

settings = MongoSettings()

client = AsyncIOMotorClient(
    settings.HOST,
    settings.PORT,
    uuidRepresentation='standard',
)

db = client[settings.DB]
