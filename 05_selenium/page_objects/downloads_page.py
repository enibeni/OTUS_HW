from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.downloads_page import DownloadsLocators
from .base_page import BasePage
from locators import AdminMainPage


class DownloadsPage(BasePage):
    """
    """

    def admin_open_downloads_page(self):
        """ Open downloads page
        """
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, AdminMainPage.catalog)))
        element.click()
        element = self.driver.find_element_by_css_selector(DownloadsLocators.downloads_thumb)
        element.click()

    def admin_upload_file(self, download_name, filename):
        """ Upload file
        """
        element = self.driver.find_element_by_css_selector(".btn-primary")
        element.click()
        element = self.driver.find_element_by_css_selector('input.form-control')
        element.send_keys(download_name)
        input_manager = self.driver.find_element_by_css_selector("#input-filename")
        input_manager.send_keys(filename)
        element = self.driver.find_element_by_css_selector("#input-mask")
        element.send_keys(filename)
        self.driver.find_element_by_css_selector("button[type='submit']").click()
