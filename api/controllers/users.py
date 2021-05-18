from uuid import UUID
from typing import List
from typing import TYPE_CHECKING

from api.models import User
from api.models import UserCreate
from api.models import UserUpdate
from api.controllers.db import db

if TYPE_CHECKING:
    from api.hints import UserDictNative

collection = db['users']


async def create_user(user_create: UserCreate) -> 'UserDictNative':
    user = User(**user_create.dict())

    result = await collection.insert_one(user.dict())
    user_dict = await collection.find_one({'_id': result.inserted_id})

    return user_dict


async def read_users() -> List['UserDictNative']:
    users_dicts = []
    async for user_dict in collection.find():
        users_dicts.append(user_dict)

    return users_dicts


async def read_user(user_uid: UUID) -> 'UserDictNative':
    return await collection.find_one({'uid': user_uid})


async def update_user(user_uid: UUID,
                      user_update: UserUpdate) -> 'UserDictNative':
    filter_dict = {'uid': user_uid}
    update_dict = user_update.dict(exclude_none=True)

    if update_dict:
        await collection.update_one(filter_dict, {'$set': update_dict})

    return await collection.find_one(filter_dict)


async def delete_user(user_uid: UUID) -> bool:
    # TODO maybe return deleted user
    result = await collection.delete_one({'uid': user_uid})

    return result.deleted_count == 1
