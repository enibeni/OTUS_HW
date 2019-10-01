import pytest
from page_objects.main_page import MainPageObject
from page_objects.product_page_object import ProductPageObject
from page_objects.search_result_page import SearchResultPageObject


class TestMainPage:
    """ Test Main Page
    """

    @pytest.mark.skip()
    def test_home_page(self, driver, main_page):
        """ check home page title
        """
        assert driver.title == "Your Store"

    @pytest.mark.webtest
    def test_add_to_cart_success_alert(self, driver, main_page):
        """ test success alert when add product to cart
        """
        MainPageObject(driver).click_featured_product(1)
        ProductPageObject(driver).add_product_to_cart()
        ProductPageObject(driver).check_success_alert("Success: You have added")

    @pytest.mark.webtest
    def test_add_to_comparison_success_alert(self, driver, main_page):
        """ test success alert when add product to comparison
        """
        MainPageObject(driver).click_featured_product(1)
        ProductPageObject(driver).add_product_to_cart()
        ProductPageObject(driver).check_success_alert("Success: You have added")

    @pytest.mark.webtest
    def test_search_input_and_click(self, driver, main_page):
        """ test search input
        """
        text_to_search = "test"
        MainPageObject(driver).search_by_text(text_to_search)
        SearchResultPageObject(driver).check_search_query(text_to_search)

    @pytest.mark.xfail(reason="Wrong expression to search")
    def test_open_product_category(self, driver, main_page):
        """ test open product category
        """
        category_to_check = "Monitorss"
        MainPageObject(driver).click_category(category_to_check)
        ProductPageObject(driver).check_product_category(category_to_check)



