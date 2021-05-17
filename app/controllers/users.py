from typing import Any
from typing import Dict
from typing import List

from app.models import User
from app.models import UserCreate
from app.models import UserRead
from app.models import UserUpdate
from app.models import UserDelete
from app.controllers.db import db


collection = db['users']

UserDict = Dict[str, Any]


async def create_user(user_create: UserCreate) -> UserDict:
    user = User(**user_create.dict())

    result = await collection.insert_one(user.dict())
    user_dict = await collection.find_one(
        {'_id': result.inserted_id}
    )

    return user_dict


async def read_users() -> List[UserDict]:
    users_dicts = []
    async for user_dict in collection.find():
        users_dicts.append(user_dict)

    return users_dicts


async def read_user(user_read: UserRead) -> UserDict:
    return await collection.find_one(user_read.dict())


async def update_user(user_update: UserUpdate) -> UserDict:
    filter_ = user_update.dict(include={'id'})
    update = user_update.dict(exclude={'id'})

    # TODO some validation
    result = await collection.update_one(filter_, {'$set': update})
    return await collection.find_one(filter_)


async def delete_user(user_delete: UserDelete) -> bool:
    # TODO maybe return deleted user
    result = await collection.delete_one(user_delete.dict())

    return result.deleted_count == 1

