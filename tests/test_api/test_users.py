import random
import secrets
import pytest
import uuid
import copy
from typing import List
from typing import cast
from typing import TYPE_CHECKING

from httpx import AsyncClient

from app.controllers.users import collection as users_collection

if TYPE_CHECKING:
    from app.hints import UserDictMixin
    from app.hints import UserDictNative
    from app.hints import UserDictTransmitted


_emails = [
    'first@domain.net',
    'admin@soup.com',
    'three@point.com',
    'xanarchy@lil.com',
    'second@domain.ru',
    'frisbee@foradog.sh',
]


def user_as_transmitted(user_dict: 'UserDictNative') -> 'UserDictTransmitted':
    user_copy: 'UserDictNative' = copy.deepcopy(user_dict)
    user_copy['uid'] = str(user_copy['uid'])  # type: ignore

    return cast('UserDictTransmitted', user_copy)


def get_random_email() -> str:
    return random.choice(_emails)


def get_random_password() -> str:
    return secrets.token_urlsafe(16)


def get_uuid() -> uuid.UUID:
    return uuid.uuid4()


def get_random_users(count: int = 5) -> List['UserDictNative']:
    return [
        {
            'uid': get_uuid(),
            'email': get_random_email(),
            'password': get_random_password(),
        }
        for _ in range(count)
    ]



@pytest.fixture
async def drop_users_collection():
    yield

    await users_collection.delete_many({})

    exinsting_users: int = 0

    async for _ in users_collection.find():
        exinsting_users += 1

    assert 0 == exinsting_users



@pytest.fixture(scope='function')
async def users():
    users: List['UserDictNative'] = get_random_users()
    result = await users_collection.insert_many(copy.deepcopy(users))

    assert len(result.inserted_ids) == len(users)

    yield [
        user_as_transmitted(user_dict)
        for user_dict in users
    ]


@pytest.mark.usefixtures('drop_users_collection')
@pytest.mark.asyncio
async def test_create_user(client: AsyncClient):
    new_user: UserDictMixin = {
        'email': get_random_email(),
        'password': get_random_password(),
    }

    response = await client.post('/users/', json=new_user)
    response_dict = response.json()

    with pytest.raises(KeyError):
        response_dict['error']

    created_user: 'UserDictNative' = response_dict['result']

    del created_user['uid']  # type: ignore

    assert created_user == new_user


def sorted_user_list(user_list: List['UserDictTransmitted']):
    return sorted(user_list, key=lambda user_dict: user_dict['uid'])


@pytest.mark.usefixtures('drop_users_collection')
@pytest.mark.asyncio
async def test_read_users(
    client: AsyncClient,
    users: List['UserDictTransmitted'],
) -> None:
    response = await client.get('/users/')
    response_dict = response.json()

    with pytest.raises(KeyError):
        response_dict['error']

    existing_users = response_dict['result']

    assert sorted_user_list(users) == sorted_user_list(existing_users)


@pytest.mark.usefixtures('drop_users_collection')
@pytest.mark.asyncio
async def test_read_user(client: AsyncClient, users: list):
    retrieved_users: List['UserDictTransmitted'] = []

    # Act
    for user in users:
        user_uid: str = user['uid']
        response = await client.get(f'/users/{user_uid}')
        response_dict  = response.json()

        with pytest.raises(KeyError):
            response_dict['error']

        retrieved_user: 'UserDictTransmitted' = response_dict['result']
        retrieved_users.append(retrieved_user)

    # Assert
    assert sorted_user_list(users) == sorted_user_list(retrieved_users)


@pytest.mark.usefixtures('drop_users_collection')
@pytest.mark.asyncio
async def test_update_user(
    client: AsyncClient,
    users: List['UserDictTransmitted'],
):
    updated_users: List['UserDictTransmitted'] = []

    # Act
    for user in users:
        user_uid = user['uid']

        del user['uid']  # type: ignore

        user['email'] = get_random_email()
        user['password'] = get_random_password()

        response = await client.put(f'/users/{user_uid}', json=user)
        response_dict  = response.json()

        with pytest.raises(KeyError):
            response_dict['error']

        updated_user: 'UserDictTransmitted' = response_dict['result']
        updated_users.append(updated_user)

        user['uid'] = user_uid

        assert user == updated_user

    # Assert
    assert sorted_user_list(users) == sorted_user_list(updated_users)


@pytest.mark.usefixtures('drop_users_collection')
@pytest.mark.asyncio
async def test_delete_user(
    client: AsyncClient,
    users: List['UserDictTransmitted'],
):
    # Act
    for user in users:
        user_uid = user['uid']

        response = await client.delete(f'/users/{user_uid}')
        response_dict  = response.json()

        with pytest.raises(KeyError):
            response_dict['error']

        # Assert
        assert response_dict['result'] is True
