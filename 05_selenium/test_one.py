from selenium.webdriver.common.keys import Keys
from locators.main_page import MainPage
from locators.admin_page import AdminPage
from selenium.webdriver.common.action_chains import ActionChains


def test_home_page(app):
    """ check home page title
    """
    assert app.wd.title == "Your Store"


def test_logo_is_clickable(app):
    """ test logo click
    """
    element = app.wd.find_element_by_css_selector(MainPage.logo)
    element.click()


def test_open_featured_product(app):
    """ test open featured product
    """
    element = app.wd.find_element_by_xpath(MainPage.featured_product)
    element.click()


def test_search_input_and_click(app):
    """ test search input
    """
    element = app.wd.find_element_by_css_selector(MainPage.search_input)
    element.click()
    element.send_keys("foo" + Keys.ENTER)


def test_admin_panel_auth_with_wrong_cred(app):
    """ test auth in admin panel
    """
    app.open_admin_panel()
    element = app.wd.find_element_by_css_selector(AdminPage.username_input)
    element.click()
    element.send_keys("foo")
    element = app.wd.find_element_by_css_selector(AdminPage.password_input)
    element.click()
    element.send_keys("bar")
    element = app.wd.find_element_by_css_selector(AdminPage.login_button)
    element.click()


def test_open_product_category(app):
    """ test open product category
    """
    desktops_link = app.wd.find_element_by_link_text("Components")
    ActionChains(app.wd).move_to_element(desktops_link).pause(2).perform()
    app.wd.find_element_by_link_text("Monitors (2)").click()
    app.wd.find_element_by_partial_link_text("Monitors")


