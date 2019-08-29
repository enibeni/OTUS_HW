from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators.admin_page import AdminPage


class Application:
    def __init__(self, browser_name, base_url):
        self.browser = browser_name
        self.base_url = base_url if 'http' in base_url else f'http://{base_url}'
        if self.browser == 'chrome':
            chrome_options = Options()
            chrome_options.add_argument("--start-fullscreen")
            # chrome_options.add_argument("--headless")
            self.wd = webdriver.Chrome(chrome_options=chrome_options)
        elif self.browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif self.browser == 'safari':
            self.wd = webdriver.Safari()
        else:
            raise ValueError(f'Unrecognized browser {browser_name}')

    def open_home_page(self):
        """ Open main page
        """
        wd = self.wd
        wd.get(self.base_url)

    def open_admin_panel(self):
        """ Open admin page
        """
        wd = self.wd
        wd.get(f"{self.base_url}/admin")

    def admin_page_login(self, login, password):
        """ Open admin login page and login
        """
        self.open_admin_panel()
        element = self.wd.find_element_by_css_selector(AdminPage.username_input)
        element.click()
        element.send_keys(login)
        element = self.wd.find_element_by_css_selector(AdminPage.password_input)
        element.click()
        element.send_keys(password)
        element.find_element_by_xpath(AdminPage.login_button)
        element.click()
