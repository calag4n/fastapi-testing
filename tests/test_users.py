import logging
import pytest
import uuid
import copy

from httpx import AsyncClient

from app.controllers.users import collection as users_collection

log = logging.getLogger('test logger')


@pytest.fixture(scope='function')
async def drop_users_collection():
    yield

    await users_collection.delete_many({})

    exinsting_users: int = 0

    async for _ in users_collection.find():
        exinsting_users += 1

    assert 0 == exinsting_users


@pytest.fixture(scope='function')
async def users():
    def get_uuid_as_str():
        return str(uuid.uuid4())

    user_dicts = [
        {
            'id': get_uuid_as_str(),
            'email': 'admin@soup.com',
            'password': 'password',
        },
        {
            'id': get_uuid_as_str(),
            'email': 'three@point.com',
            'password': 'secrets', },
        {
            'id': get_uuid_as_str(),
            'email': 'xanarchy@lil.com',
            'password': 'treesap',
        }
    ]

    result = await users_collection.insert_many(copy.deepcopy(user_dicts))

    assert len(result.inserted_ids) == len(user_dicts)

    yield copy.deepcopy(user_dicts)

    await users_collection.delete_many({})

    exinsting_users: int = 0

    async for _ in users_collection.find():
        exinsting_users += 1

    assert 0 == exinsting_users



# @pytest.mark.usefixtures('drop_users_collection')
# @pytest.mark.asyncio
# async def test_create_user(client: AsyncClient):
#     new_user = {
#         'email': 'my@superemail.org',
#         'password': 'dvorak',
#     }

#     response = await client.post('/users/', json=new_user)
#     response_dict = response.json()

#     created_user = response_dict['result']

#     assert uuid.UUID(created_user['id'])

#     del created_user['id']

#     assert response_dict['result'] == new_user

#     with pytest.raises(KeyError):
#         response_dict['error']


# @pytest.mark.asyncio # async def test_read_users(client: AsyncClient, users: list):
#     response = await client.get('/users/')
#     response_dict = response.json()

#     existing_users = response_dict['result']

#     def sorted_user_list(user_list: list):
#         return sorted(user_list, key=lambda user_dict: user_dict['id'])

#     assert sorted_user_list(users) == sorted_user_list(existing_users)

#     with pytest.raises(KeyError):
#         response_dict['error']


@pytest.mark.asyncio
async def test_read_user(client: AsyncClient, users: list):
    exinsting_users: int = 0

    async for _ in users_collection.find():
        exinsting_users += 1

    assert exinsting_users

    for user in users:
        user_id = user['id']
        path = f'/users/{user_id}'
        response = await client.get(path)
        response_dict = response.json()
        raise AssertionError(response_dict['error'])
        existing_user = response_dict['result']

        assert user == existing_user

        with pytest.raises(KeyError):
            response_dict['error']
