import pytest

from application import Application


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="127.0.0.1",
        help="Site url to test"
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Which browser to use"
    )


@pytest.fixture(scope='session')
def app(request):
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    app = Application(browser, base_url)
    app.open_home_page()
    yield app
    app.wd.quit()
