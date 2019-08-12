import pytest


# https://jsonplaceholder.typicode.com/posts/1


def test_get_post_by_id(api_client):
    """ some doctest is here
    """
    post_id = 10
    r = api_client.get(path=f"/posts/{post_id}").json()
    assert r["id"] == post_id


def test_new_post(api_client):
    """ some doctest is here
    """
    json = {
        "id": 101,
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    r = api_client.post(path=f"/posts/", data=json).json()
    assert r["id"] == json["id"]


def test_edit_post(api_client):
    """ some doctest is here
    """
    post_id = 1
    body = {
        "id": 1,
        "title": "new_title",
        "body": "bar",
        "userId": 1
    }
    r = api_client.put(path=f"/posts/{post_id}", data=body).json()
    assert r["title"] == body["title"]


@pytest.mark.parametrize("user_id", [-1, 0])
def test_no_error_if_filter_todos_by_wrong_user_id(api_client, user_id):
    """ some doctest is here
    """
    params = {"userId": user_id}
    r = api_client.get(path=f"/users/{user_id}/todos", params=params)
    assert r.status_code == 200


@pytest.mark.parametrize("user_id", [-1, 0])
def test_no_error_if_filter_post_by_wrong_user_id(api_client, user_id):
    """ some doctest is here
    """
    r = api_client.get(path=f"/users/{user_id}/posts")
    assert r.status_code == 200
