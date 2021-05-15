def test_post_user(test_client, test_user):
    response = test_client.post('/users', json=test_user)
    assert response.status_code == 201


def test_get_users(test_client, test_user):
    response = test_client.get("/users")
    assert response.status_code == 200
    assert response.json() == [test_user]
