import allure
from .base_page import BasePage
from locators.search_result_page import SearchResultPage


class SearchResultPageObject(BasePage):
    """
    """
    def check_search_query(self, query):
        with allure.step("Check search query"):
            element = self.driver.find_element_by_css_selector(SearchResultPage.search_query)
            assert str(element.text).startswith(f"Search - {query}")
