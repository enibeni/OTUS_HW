from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from locators import MainPage


class MainPageObject:

    def __init__(self, driver):
        self.driver = driver

    def click_logo(self):
        element = self.driver.find_element_by_css_selector(MainPage.logo)
        element.click()

    def click_featured_product(self, number):
        index = number - 1
        feature_product = self.driver.find_elements_by_css_selector(MainPage.Featured.products['css'])[index]
        product_name = feature_product.find_element_by_css_selector(MainPage.Featured.names['css']).text
        feature_product.click()
        return product_name

    def search_by_text(self, text):
        element = self.driver.find_element_by_css_selector(MainPage.search_input)
        element.click()
        element.send_keys(text + Keys.ENTER)

    def click_category(self, category_name):
        desktops_link = self.driver.find_element_by_link_text("Components")
        ActionChains(self.driver).move_to_element(desktops_link).pause(2).perform()
        self.driver.find_element_by_partial_link_text(category_name).click()
        # self.driver.find_element_by_partial_link_text("Monitors")