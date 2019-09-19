import os
import pytest
import logging
from selenium.webdriver import Chrome, Firefox, Safari
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from browsermobproxy import Server
from page_objects.admin_login_page import AdminLoginPageObject
from log_helper import SessionLogger, MyListener


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
def driver(request, logger, proxy):
    browser = request.config.getoption("--browser")
    implicit_wait = request.config.getoption("--wait")
    if browser == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument(f'--proxy-server={proxy.proxy}')
        chrome_options.add_experimental_option('w3c', False)
        # chrome_options.add_argument("--start-fullscreen")
        # chrome_options.add_argument("--headless")
        driver = EventFiringWebDriver(Chrome(options=chrome_options), MyListener(logger))
    elif browser == 'firefox':
        driver = Firefox()
    elif browser == 'safari':
        driver = Safari()
    else:
        raise ValueError(f'Unrecognized browser {browser}')

    driver.implicitly_wait(implicit_wait)

    yield driver
    driver.quit()


@pytest.fixture(scope='session', autouse=True)
def proxy():
    server = Server(os.path.join(os.path.dirname(__file__), 'browsermob-proxy-2.1.4/bin/browsermob-proxy'))
    server.start()
    proxy = server.create_proxy()
    proxy.new_har(title='test_har')
    yield proxy
    server.stop()


@pytest.fixture()
def main_page(driver, request, logger):
    base_url = request.config.getoption('--url')
    driver.get(base_url)
    logger.debug('Main page opened')
    yield


@pytest.fixture()
def admin_page(request, driver, logger):
    path = "/admin"
    base_url = request.config.getoption('--url')
    driver.get(f"{base_url}{path}")
    AdminLoginPageObject(driver).admin_page_login(login="user", password="bitnami1")
    logger.debug('Admin page opened')
    yield
    # app.logout()


@pytest.fixture(scope='session')
def logger():
    logger = SessionLogger(name='session_logger').start_logger()
    yield logger
    logging.shutdown()


@pytest.fixture(scope='session', autouse=True)
def logs_setup_teardown(logger):
    logger.debug('===== New test session ====')
    yield
    logger.debug('==== End of test session ====')



