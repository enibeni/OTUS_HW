import pytest


# --url=https://dog.ceo/api

def test_get_random_dog(api_client):
    """ some doctest is here
    """
    r = api_client.get(
        path="/breeds/image/random").json()

    assert r['status'] == 'success'
    assert isinstance(r['message'], str)


def test_get_random_dog_by_breed(api_client):
    """ some doctest is here
    """
    breed = "hound"
    r = api_client.get(
        path=f"/breed/{breed}/images/random").json()

    assert r['status'] == 'success'
    assert isinstance(r['message'], str)


def test_get_all_breeds(api_client):
    """ some doctest is here
    """
    r = api_client.get(
        path="/breeds/list/all").json()

    assert r['status'] == 'success'
    assert len(r['message']) > 0


def test_get_all_dogs_by_breed(api_client):
    """ some doctest is here
    """
    breed = "hound"
    r = api_client.get(
        path=f"/breed/{breed}/images").json()

    assert r['status'] == 'success'
    assert len(r['message']) > 0


def test_get_all_sub_breeds(api_client):
    """ some doctest is here
    """
    breed = "hound"
    r = api_client.get(
        path=f"/breed/{breed}/list").json()

    assert r['status'] == 'success'
    assert len(r['message']) > 0
