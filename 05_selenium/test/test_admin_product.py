import pytest
import allure
from random import randint
from page_objects.admin_main_page import AdminMainPageObject
from page_objects.admin_edit_product_page import AdminEditProductPage


@allure.feature('Admin page')
class TestAdminProductCrud:
    """ Test Product crud operations
    """

    @allure.story('admin page test')
    def test_admin_add_product_with_only_required_fields(self, driver, create_product):
        """ test creation of product when only required fields are filled
        """
        AdminMainPageObject(driver).admin_check_success_alert()

    @allure.story('admin page test')
    def test_edit_product(self, driver, create_product):
        """ test edit product
        """
        name = create_product
        new_meta = f"test_edit_meta_{randint(1, 1000)}"
        AdminMainPageObject(driver).admin_find_product_by_name(name)
        AdminMainPageObject(driver).admin_edit_product_click()
        AdminEditProductPage(driver).fill_product_meta(new_meta)
        AdminEditProductPage(driver).save_product_button_click()
        AdminMainPageObject(driver).admin_check_success_alert()

    @allure.story('admin page test')
    def test_delete_product(self, driver, admin_page):
        """ test delete product
        """
        name = AdminMainPageObject(driver).admin_create_product()
        AdminMainPageObject(driver).admin_find_product_by_name(name)
        AdminMainPageObject(driver).admin_found_product_select_click()
        AdminMainPageObject(driver).admin_delete_button_click()
        driver.switch_to_alert().accept()
        AdminMainPageObject(driver).admin_check_success_alert()


@pytest.fixture()
def create_product(driver, admin_page):
    name = AdminMainPageObject(driver).admin_create_product()
    yield name
    AdminMainPageObject(driver).admin_delete_product(name)

