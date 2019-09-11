from page_objects.main_page import MainPageObject


def test_home_page(app):
    """ check home page title
    """
    assert app.driver.title == "Your Store"


def test_logo_is_clickable(app):
    """ test logo click
    """
    MainPageObject(app.driver).click_logo()


def test_open_featured_product(app):
    """ test open featured product
    """
    MainPageObject(app.driver).click_featured_product(1)


def test_search_input_and_click(app):
    """ test search input
    """
    MainPageObject(app.driver).search_by_text(text="test")


def test_open_product_category(app):
    """ test open product category
    """
    MainPageObject(app.driver).click_category("Monitors")



