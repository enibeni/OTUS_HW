import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.product_page import ProductPage
from locators.common import Common


class ProductPageObject(BasePage):
    """
    """

    def check_product_category(self, category):
        with allure.step("Check product category"):
            element = self.driver.find_element_by_css_selector(ProductPage.product_category)
            assert str(element.text).startswith(category)

    def add_product_to_cart(self):
        with allure.step("Add product to cart"):
            element = self.driver.find_element_by_css_selector(ProductPage.add_to_cart)
            element.click()

    def add_product_to_comparison(self):
        with allure.step("Add product to comparison"):
            element = self.driver.find_element_by_css_selector(ProductPage.add_to_compare_list)
            element.click()

    def open_cart(self):
        with allure.step("Open cart"):
            element = self.driver.find_element_by_css_selector(Common.cart_button)
            element.click()

    def check_cart_label(self, label):
        with allure.step("Check cart label"):
            element = self.driver.find_element_by_css_selector(Common.cart_button_label)
            assert str(element.text).startswith(label)

    def check_success_alert(self, message):
        with allure.step("Check success alert"):
            wait = WebDriverWait(self.driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ProductPage.success_alert)))
            assert str(element.text).startswith(message)
