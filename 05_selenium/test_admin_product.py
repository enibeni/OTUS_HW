from random import randint
from locators.admin_main_page import AdminMainPage
from locators.add_product_page import AddProductPage


class TestAdminProductCrud:
    """ Test Product crud operations
    """

    def test_admin_add_product_with_only_required_fields(self, app, admin_session, create_product):
        """ test creation of product when only required fields are filled
        """
        element = app.wd.find_element_by_xpath(AdminMainPage.success_alert)
        assert str(element.text).startswith("Success: You have modified products!")

    def test_edit_product(self, app, admin_session, create_product):
        """ test edit product
        """
        name = create_product
        new_meta = f"test_edit_meta_{randint(1, 1000)}"
        app.admin_find_product_by_name(name)
        element = app.wd.find_element_by_xpath(AdminMainPage.found_product_edit_button)
        element.click()
        element = app.wd.find_element_by_css_selector(AddProductPage.product_meta)
        element.click()
        element.clear()
        element.send_keys(new_meta)
        element = app.wd.find_element_by_css_selector(AddProductPage.save_button)
        element.click()

        element = app.wd.find_element_by_xpath(AdminMainPage.success_alert)
        assert str(element.text).startswith("Success: You have modified products!")

    def test_delete_product(self, app, admin_session):
        """ test delete product
        """
        app.admin_open_product_creation()
        name = app.admin_create_product()
        app.admin_find_product_by_name(name)
        element = app.wd.find_element_by_xpath(AdminMainPage.found_product_select_button)
        element.click()
        element = app.wd.find_element_by_css_selector(AdminMainPage.delete_button)
        element.click()
        app.wd.switch_to_alert().accept()
        element = app.wd.find_element_by_xpath(AdminMainPage.success_alert)
        assert str(element.text).startswith("Success: You have modified products!")

