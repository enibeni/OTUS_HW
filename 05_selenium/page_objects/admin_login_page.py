from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AdminLoginPage
from .base_page import BasePage


class AdminLoginPageObject(BasePage):
    """
    """

    def admin_page_login(self, login, password):
        """ Open admin login page and login
        """
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, AdminLoginPage.username_input)))
        element.click()
        element.send_keys(login)
        element = self.driver.find_element_by_css_selector(AdminLoginPage.password_input)
        element.click()
        element.send_keys(password)
        element = self.driver.find_element_by_css_selector(AdminLoginPage.login_button)
        element.click()