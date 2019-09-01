from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


def test_move_elements_to_basket(app):
    """ Test drag and drop
    """
    app.wd.switch_to.frame(
        app.wd.find_element(
            By.CSS_SELECTOR, 'iframe[src="https://marcojakob.github.io/dart-dnd/basic/"]'
        )
    )
    documents = app.wd.find_elements(By.CSS_SELECTOR, 'img[class="document"]')
    trash = app.wd.find_element(By.CSS_SELECTOR, '[class="trash"]')
    ActionChains(app.wd).drag_and_drop(documents[0], trash).perform()
    # pop out already removed document from a list
    documents.pop(0)
    # trash changes class name after the first removed document
    trash_full = app.wd.find_element(By.CSS_SELECTOR, '[class="trash full"]')
    for document in documents:
        ActionChains(app.wd).drag_and_drop(document, trash_full).perform()
    # check iframe not longer contain any documents
    assert not app.wd.find_elements(By.CSS_SELECTOR, 'img[class="document"]')
