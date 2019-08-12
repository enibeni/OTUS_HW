import pytest


@pytest.fixture(scope="class")
def name_in_lowercase():
    return "batman"


@pytest.fixture(scope="class")
def even_and_odds():
    even = [x for x in range(1, 50) if x % 2 == 0]
    odds = [x for x in range(50) if x % 2 != 0]
    return even, odds


@pytest.fixture(scope="session")
def numbers():
    return [1, 2, 3]


@pytest.fixture(scope="function")
def numbers_with_duplicates():
    return [1, 2, 3]


@pytest.fixture(scope="module")
def dict_with_keys_inserted_one_by_one():
    d = {}
    d["first"] = 1
    d["second"] = 2
    d["third"] = 3
    d["fourth"] = 4
    d["fifth"] = 5
    d["last"] = 6
    return d


@pytest.fixture(scope="function", autouse=True)
def fixture_for_request_info(request):
    yield
    print("___________________________")
    print(f"{request.node}")
    print(f"{request.scope}")
    print(f"{request.cls}")
    print(f"{request.module}")
    print("___________________________")
