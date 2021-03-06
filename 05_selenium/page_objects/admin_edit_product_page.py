import allure
from .base_page import BasePage
from locators import AddProductPage


class AdminEditProductPage(BasePage):
    """
    """
    def fill_product_name(self, name):
        with allure.step("Fill product name"):
            element = self.driver.find_element_by_css_selector(AddProductPage.product_name)
            element.click()
            element.clear()
            element.send_keys(name)

    def fill_product_meta(self, meta):
        with allure.step("Fill product meta"):
            element = self.driver.find_element_by_css_selector(AddProductPage.product_meta)
            element.click()
            element.clear()
            element.send_keys(meta)

    def fill_product_model(self, model):
        with allure.step("Fill product model"):
            element = self.driver.find_element_by_link_text("Data")
            element.click()
            element = self.driver.find_element_by_css_selector(AddProductPage.product_model)
            element.click()
            element.send_keys(model)

    def save_product_button_click(self):
        with allure.step("Save product button click"):
            element = self.driver.find_element_by_css_selector(AddProductPage.save_button)
            element.click()

