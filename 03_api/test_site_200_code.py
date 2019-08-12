def test_site_get_status_200_code(api_client):
    """ Check site status code is 200
    """
    r = api_client.get(path="/")
    assert r.status_code == 200
