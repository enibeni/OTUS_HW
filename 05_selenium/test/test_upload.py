import os
import time
from page_objects.downloads_page import DownloadsPage


def test_upload_file(driver, admin_page):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'Z7pqKcPxxsg.jpg')
    DownloadsPage(driver).admin_open_downloads_page()
    DownloadsPage(driver).admin_upload_file("name", filename)


    time.sleep(10)
