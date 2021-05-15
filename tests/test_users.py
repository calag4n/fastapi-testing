from api.app import app
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient

client = TestClient(app)
"""
I would like to POST and GET data from a db named 'TEST_DB' not from the 'PROD_DB' initialized in api/controllers/connect.py .
I tried a different approach (based on FastAPI's Dependencie Injection) visible on the 'anotherWay' branch.
"""

new_user = jsonable_encoder({
    "email": "user@example.com",
    "password": "some_password"
})


def test_post_user():
    response = client.post('/users', json=new_user)
    assert response.status_code == 201


def test_read_main():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == new_user
