from api.controllers.connect import db, users_collection
from motor.motor_asyncio import AsyncIOMotorClient
from pytest import fixture
from starlette.config import environ
from starlette.testclient import TestClient


@fixture(scope="module", autouse=True)
def test_user():
    return {"email": "user1@example.com", "password": "OtherPassword"}


def mock_get_db() -> AsyncIOMotorClient:
    return db.client['TEST_DB']


@fixture(scope="module", autouse=True)
def test_client(test_user):
    from api.app import app
    with TestClient(app) as test_client:
        yield test_client

    import asyncio

    db = asyncio.run(mock_get_db())

    db[users_collection].insert_one(test_user)


environ['TESTING'] = 'TRUE'
