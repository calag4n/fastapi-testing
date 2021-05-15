from api.controllers.connect import users_collection
from api.models.User import User
from motor.motor_asyncio import AsyncIOMotorClient


async def get_users(db: AsyncIOMotorClient):
    users = []
    async for user in db[users_collection].find():
        users.append(user)
    return users


async def add_user(user_in: User, db: AsyncIOMotorClient):
    user_model = User(**user_in.dict())

    user = await db[users_collection].insert_one(user_model.dict())
    new_user = await db[users_collection].find_one({"_id": user.inserted_id})
    return new_user
