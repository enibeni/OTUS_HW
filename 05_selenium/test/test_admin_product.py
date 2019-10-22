import pytest
import allure
from random import randint
from page_objects.admin_main_page import AdminMainPageObject
from page_objects.admin_edit_product_page import AdminEditProductPage
import pymysql
from db_helper import SqlDBHelper as db


@allure.feature('Admin page')
class TestAdminProductCrud:
    """ Test Product crud operations
    """

    def test_admin_db(self):
        conn = pymysql.connect(
            host='localhost',
            user='bn_opencart',
            password='',
            db='bitnami_opencart'
        )
        cursor = conn.cursor()
        product_id = randint(1000, 9999)
        cursor.execute(f"""
        INSERT oc_product(product_id, model, quantity, sku, upc, ean, jan, isbn, mpn, location, image, stock_status_id, manufacturer_id, tax_class_id, date_added, date_modified)
        VALUES ({product_id}, 'test_model_{product_id}', '1', '', '', '', '', '', '', '', '', '6', '0', '0', '2019-09-01 13:59:38', '2019-09-01 13:59:38')
        """)
        cursor.execute(f"""
        INSERT oc_product_description(product_id, language_id, name, description, tag, meta_title, meta_description, meta_keyword)
        VALUES ({product_id}, '1', 'test_product_{product_id}', '', '', 'meta_title_{product_id}', '', '')
        """)
        print(product_id)

    @allure.story('admin page test')
    def test_admin_add_product_with_only_required_fields(self, driver, create_product):
        """ test creation of product when only required fields are filled
        """
        AdminMainPageObject(driver).admin_check_success_alert()

    @allure.story('admin page test')
    def test_edit_product(self, driver, create_product):
        """ test edit product
        """
        name = create_product
        new_meta = f"test_edit_meta_{randint(1, 1000)}"
        AdminMainPageObject(driver).admin_open_product_creation()
        AdminMainPageObject(driver).admin_find_product_by_name(name)
        AdminMainPageObject(driver).admin_edit_product_click()
        AdminEditProductPage(driver).fill_product_meta(new_meta)
        AdminEditProductPage(driver).save_product_button_click()
        AdminMainPageObject(driver).admin_check_success_alert()

    @allure.story('admin page test')
    def test_delete_product(self, driver, admin_page):
        """ test delete product
        """
        name = AdminMainPageObject(driver).admin_create_product()
        AdminMainPageObject(driver).admin_find_product_by_name(name)
        AdminMainPageObject(driver).admin_found_product_select_click()
        AdminMainPageObject(driver).admin_delete_button_click()
        driver.switch_to_alert().accept()
        AdminMainPageObject(driver).admin_check_success_alert()


@pytest.fixture()
def create_product(driver, admin_page):
    name = db().create_product_in_db()
    yield name
    AdminMainPageObject(driver).admin_delete_product(name)

