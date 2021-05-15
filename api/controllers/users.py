from uuid import uuid4

from api.models.User import User

from .connect import db

users_collection = db.get_collection("users")


async def get_users():
    users = []
    async for user in users_collection.find():
        users.append(user)
    return users


async def add_user(user_in: User):
    user_model = User(**user_in.dict())

    user = await users_collection.insert_one(user_model.dict())
    new_user = await users_collection.find_one({"_id": user.inserted_id})
    return new_user
