from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import AdminMainPage, AdminLoginPage


class AdminMainPageObject:
    """
    """

    def admin_page_login(self, app, login, password):
        """ Open admin login page and login
        """
        wait = WebDriverWait(app.driver, 10)
        # self.open_admin_login_panel()
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, AdminLoginPage.username_input)))
        element.click()
        element.send_keys(login)
        element = app.driver.find_element_by_css_selector(AdminLoginPage.password_input)
        element.click()
        element.send_keys(password)
        element = app.driver.find_element_by_css_selector(AdminLoginPage.login_button)
        element.click()

    def admin_open_product_creation(self):
        """ Open product creation page
        """
        wait = WebDriverWait(self.wd, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, AdminMainPage.catalog)))
        element.click()
        element = self.wd.find_element_by_css_selector(AdminMainPage.products_menu)
        element.click()

    def admin_create_product(self, **kwargs):
        """ Create new product
        :param kwargs: name, meta, model
        :return: name
        """
        wait = WebDriverWait(self.wd, 10)
        name = kwargs.get("name", f"test_product_{randint(1, 1000)}")
        meta = kwargs.get("meta", f"test_meta_{randint(1, 1000)}")
        model = kwargs.get("model", f"test_model_{randint(1, 1000)}")

        element = self.wd.find_element_by_css_selector(AdminMainPage.add_product)
        element.click()
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, AddProductPage.product_name)))
        element.click()
        element.send_keys(name)
        element = self.wd.find_element_by_css_selector(AddProductPage.product_meta)
        element.click()
        element.send_keys(meta)
        element = self.wd.find_element_by_link_text("Data")
        element.click()
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, AddProductPage.product_model)))
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