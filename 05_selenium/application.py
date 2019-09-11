from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from locators.admin_login_page import AdminLoginPage
from locators.add_product_page import AddProductPage
from locators.admin_main_page import AdminMainPage


class Application:
    def __init__(self, browser_name, base_url, implicit_wait):
        if browser_name == 'chrome':
            chrome_options = Options()
            # chrome_options.add_argument("--start-fullscreen")
            # chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        elif browser_name == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser_name == 'safari':
            self.driver = webdriver.Safari()
        else:
            raise ValueError(f'Unrecognized browser {browser_name}')

        self.base_url = base_url if 'http' in base_url else f'http://{base_url}'
        self.driver.implicitly_wait(implicit_wait)

    def open_home_page(self):
        """ Open main page
        """
        wd = self.driver
        wd.get(self.base_url)

    def open_admin_panel(self):
        """ Open admin page
        """
        wd = self.driver
        wd.get(f"{self.base_url}/admin")

    def admin_page_login(self, login, password):
        """ Open admin login page and login
        """
        wait = WebDriverWait(self.driver, 10)
        self.open_admin_panel()
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, AdminLoginPage.username_input)))
        element.click()
        element.send_keys(login)
        element = self.driver.find_element_by_css_selector(AdminLoginPage.password_input)
        element.click()
        element.send_keys(password)
        element = self.driver.find_element_by_css_selector(AdminLoginPage.login_button)
        element.click()