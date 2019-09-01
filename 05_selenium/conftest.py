import pytest
from application import Application
from locators.admin_main_page import AdminMainPage


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


@pytest.fixture()
def admin_session(app):
    app.admin_page_login(login="user", password="bitnami1")
    yield
    # app.logout()


@pytest.fixture()
def create_product(app, admin_session):
    app.admin_open_product_creation()
    name = app.admin_create_product()
    yield name
    app.admin_find_product_by_name(name)
    element = app.wd.find_element_by_xpath(AdminMainPage.found_product_select_button)
    element.click()
    element = app.wd.find_element_by_css_selector(AdminMainPage.delete_button)
    element.click()
    app.wd.switch_to_alert().accept()
