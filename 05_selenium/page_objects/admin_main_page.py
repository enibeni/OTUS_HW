from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from locators import AdminMainPage
from .base_page import BasePage
from .admin_edit_product_page import AdminEditProductPage


class AdminMainPageObject(BasePage):
    """
    """

    def admin_open_product_creation(self):
        """ Open product creation page
        """
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, AdminMainPage.catalog)))
        element.click()
        element = self.driver.find_element_by_css_selector(AdminMainPage.products_menu)
        element.click()

    def admin_add_product_button_click(self):
        element = self.driver.find_element_by_css_selector(AdminMainPage.add_product)
        element.click()

    def admin_create_product(self, **kwargs):
        """ Create new product
        :param kwargs: name, meta, model
        :return: name
        """
        name = kwargs.get("name", f"test_product_{randint(1, 1000)}")
        meta = kwargs.get("meta", f"test_meta_{randint(1, 1000)}")
        model = kwargs.get("model", f"test_model_{randint(1, 1000)}")

        AdminMainPageObject(self.driver).admin_open_product_creation()
        AdminMainPageObject(self.driver).admin_add_product_button_click()
        AdminEditProductPage(self.driver).fill_product_name(name)
        AdminEditProductPage(self.driver).fill_product_meta(meta)
        AdminEditProductPage(self.driver).fill_product_model(model)
        AdminEditProductPage(self.driver).save_product_button_click()

        return name

    def admin_delete_product(self, name):
        AdminMainPageObject(self.driver).admin_find_product_by_name(name)
        element = self.driver.find_element_by_xpath(AdminMainPage.found_product_select_button)
        element.click()
        element = self.driver.find_element_by_css_selector(AdminMainPage.delete_button)
        element.click()
        self.driver.switch_to_alert().accept()

    def admin_find_product_by_name(self, name):
        """ Find product by name using search input
        """
        element = self.driver.find_element_by_css_selector(AdminMainPage.search_by_product_name)
        element.click()
        element.clear()
        element.send_keys(name)
        element = self.driver.find_element_by_css_selector(AdminMainPage.search_filter_button)
        element.click()

    def admin_edit_product_click(self):
        element = self.driver.find_element_by_xpath(AdminMainPage.found_product_edit_button)
        element.click()

    def admin_found_product_select_click(self):
        element = self.driver.find_element_by_xpath(AdminMainPage.found_product_select_button)
        element.click()

    def admin_delete_button_click(self):
        element = self.driver.find_element_by_css_selector(AdminMainPage.delete_button)
        element.click()

    def admin_check_success_alert(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, AdminMainPage.success_alert)))
        assert str(element.text).startswith("Success: You have modified products!")