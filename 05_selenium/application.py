from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from locators.admin_login_page import AdminLoginPage
from locators.add_product_page import AddProductPage
from locators.admin_main_page import AdminMainPage
from random import randint


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
        element = self.wd.find_element_by_css_selector(AdminLoginPage.username_input)
        element.click()
        element.send_keys(login)
        element = self.wd.find_element_by_css_selector(AdminLoginPage.password_input)
        element.click()
        element.send_keys(password)
        element = self.wd.find_element_by_css_selector(AdminLoginPage.login_button)
        element.click()

    def admin_open_product_creation(self):
        """ Open product creation page
        """
        element = self.wd.find_element_by_css_selector(AdminMainPage.catalog)
        element.click()
        element = self.wd.find_element_by_css_selector(AdminMainPage.products_menu)
        element.click()

    def admin_create_product(self, **kwargs):
        """ Create new product
        :param kwargs: name, meta, model
        :return: name
        """
        name = kwargs.get("name", f"test_product_{randint(1, 1000)}")
        meta = kwargs.get("meta", f"test_meta_{randint(1, 1000)}")
        model = kwargs.get("model", f"test_model_{randint(1, 1000)}")

        element = self.wd.find_element_by_css_selector(AdminMainPage.add_product)
        element.click()
        element = self.wd.find_element_by_css_selector(AddProductPage.product_name)
        element.click()
        element.send_keys(name)
        element = self.wd.find_element_by_css_selector(AddProductPage.product_meta)
        element.click()
        element.send_keys(meta)
        element = self.wd.find_element_by_link_text("Data")
        element.click()
        element = self.wd.find_element_by_css_selector(AddProductPage.product_model)
        element.click()
        element.send_keys(model)
        element = self.wd.find_element_by_css_selector(AddProductPage.save_button)
        element.click()

        return name

    def admin_find_product_by_name(self, name):
        """ Find product by name using search input
        """
        element = self.wd.find_element_by_css_selector(AdminMainPage.search_by_product_name)
        element.click()
        element.clear()
        element.send_keys(name)
        element = self.wd.find_element_by_css_selector(AdminMainPage.search_filter_button)
        element.click()

