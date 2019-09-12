import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.admin_login_page import AdminLoginPageObject


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="http://127.0.0.1:80/",
        help="Site url to test"
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Which browser to use"
    )
    parser.addoption(
        "--wait",
        action="store",
        default="10",
        help="Timeout to implicitly wait for an element to be found"
    )


@pytest.fixture(scope='session')
def driver(request):
    browser = request.config.getoption("--browser")
    implicit_wait = request.config.getoption("--wait")
    if browser == 'chrome':
        chrome_options = Options()
        # chrome_options.add_argument("--start-fullscreen")
        # chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'safari':
        driver = webdriver.Safari()
    else:
        raise ValueError(f'Unrecognized browser {browser}')

    driver.implicitly_wait(implicit_wait)

    yield driver
    # driver.quit()


@pytest.fixture()
def main_page(driver, request):
    base_url = request.config.getoption('--url')
    return driver.get(base_url)


@pytest.fixture()
def admin_page(request, driver):
    path = "/admin"
    base_url = request.config.getoption('--url')
    driver.get(f"{base_url}{path}")
    AdminLoginPageObject(driver).admin_page_login(login="user", password="bitnami1")
    yield
    # app.logout()



