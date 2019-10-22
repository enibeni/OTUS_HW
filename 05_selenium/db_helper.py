import pymysql
from contextlib import contextmanager
from random import randint


class SqlDBHelper():
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='bn_opencart',
            password='',
            db='bitnami_opencart'
        )
    def close_connection(self):
        self.connection.close()

    @contextmanager
    def db_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            yield cursor
        except Exception as e:
            raise Exception("Возникла ошибка при попытке выполнить запрос запрос к БД. {} \n".format(e))
        finally:
            cursor.close()

    def create_product_in_db(self):
        product_id = randint(1000, 9999)
        with self.db_query(f"""
        INSERT oc_product(product_id, model, quantity, sku, upc, ean, 
        jan, isbn, mpn, location, image, stock_status_id, manufacturer_id, 
        tax_class_id, date_added, date_modified)
        VALUES ({product_id}, 'test_model_{product_id}', '1', '', '', '', '', 
        '', '', '', '', '6', '0', '0', '2019-09-01 13:59:38', '2019-09-01 13:59:38')
        """):
            pass
        with self.db_query(f"""
        INSERT oc_product_description(product_id, language_id, name, description, 
        tag, meta_title, meta_description, meta_keyword)
        VALUES ({product_id}, '1', 'test_product_{product_id}', '', 
        '', 'meta_title_{product_id}', '', '')
        """):
            pass
        return f"test_product_{product_id}"


