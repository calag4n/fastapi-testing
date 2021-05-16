import pytest
import copy
from fastapi.testclient import TestClient

from api.app import app
from api.controllers.users import users_collection

"""
I would like to POST and GET data from a db named 'TEST_DB' not from the 'PROD_DB' initialized in `api/controllers/connect.py` .
Her, even on the prod DB, the `client.post()` method doesn't work, I don't know why,
I tried a different approach (based on FastAPI's Dependencie Injection) visible on the 'anotherWay' branch.
"""

new_user = {
    "email": "user@example.com",
    "password": "some_password"
}

users = [
    {
        "email": "admin@soup.com",
        "password": "password",
    },
    {
        "email": "three@point.com",
        "password": "secrets",
    },
    {
        "email": "xanarchy@lil.com",
        "password": "treesap",
    },
]


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client


@pytest.fixture
def loop(client: TestClient):
    yield client.task.get_loop()


def test_create_user(client):
    # The trailing slash in necessary, check the link
    # https://github.com/tiangolo/fastapi/issues/2060
    response = client.post('/users/', json=new_user)
    assert response.status_code == 201
    assert response.json() == new_user



async def prepare_test_list_users():
    await users_collection.drop()
    await users_collection.insert_many(copy.deepcopy(users))


def test_list_users(client, loop):
    loop.run_until_complete(prepare_test_list_users())
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == users
