from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AdminMainPage, AdminLoginPage


class AdminLoginPageObject:
    """
    """
    def __init__(self, driver):
        self.driver = driver

    def open_admin_login_panel(self):
        """ Open admin page
        """
        driver = self.driver
        driver.open(path="/admin")

