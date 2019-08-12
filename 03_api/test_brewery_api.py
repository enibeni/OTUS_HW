import pytest


# --url=https://api.openbrewerydb.org/breweries


@pytest.mark.parametrize("brewery_id", [1, 100])
def test_get_brewery_by_id(api_client, brewery_id):
    """ some doctest is here
    """
    r = api_client.get(path=f"/{brewery_id}").json()
    assert r['id'] == brewery_id


@pytest.mark.parametrize("brewery_id", [-1, 0])
def test_error_code_404_if_get_brewery_by_wrong_id(api_client, brewery_id):
    """ some doctest is here
    """
    r = api_client.get(path=f"/{brewery_id}")
    assert r.status_code == 404


@pytest.mark.parametrize("filter_param, value, response_param", [
    ("by_city", "Alameda", "city"),
    ("by_type", "micro", "brewery_type"),
    ("by_name", "Almanac Beer Company", "name")])
def test_get_list_of_breweries_by_filter_param(api_client, filter_param, value, response_param):
    """ some doctest is here
    """
    params = {filter_param: value}
    r = api_client.get(path="/", params=params).json()
    assert r[0][response_param] == value


@pytest.mark.parametrize("per_page", [0, 1, 10])
def test_pagination_per_page_amount(api_client, per_page):
    """ some doctest is here
    """
    params = {"per_page": per_page}
    r = api_client.get(path="/", params=params).json()
    assert len(r) == per_page


@pytest.mark.parametrize("query", ["Dog", "Cat"])
def test_search(api_client, query):
    """ some doctest is here
    """
    params = {"query": query}
    r = api_client.get(path="/search", params=params)
    assert query in r.text
