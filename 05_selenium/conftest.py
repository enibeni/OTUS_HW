import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import Application
from page_objects.admin_login_page import AdminLoginPageObject


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="http://127.0.0.1:8080/",
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
def app(request):
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    implicit_wait = request.config.getoption("--wait")
    app = Application(browser, base_url, implicit_wait)
    app.open_home_page()
    yield app
    app.driver.quit()


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
