def test_api_read_users(api):
    response = api.get("/users")
    assert response.status_code == 200
    assert response.json() == {"data": [], "error": None}


def test_api_read_user_bad_id(api):
    response = api.get("/users/1")
    assert response.status_code == 422
