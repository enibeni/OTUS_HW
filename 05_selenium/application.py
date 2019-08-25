from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Application:
    def __init__(self, browser_name, base_url):
        self.browser = browser_name
        self.base_url = base_url if 'http' in base_url else f'http://{base_url}'
        if self.browser == 'chrome':
            chrome_options = Options()
            chrome_options.add_argument("--start-fullscreen")
            chrome_options.add_argument("--headless")
            self.wd = webdriver.Chrome(chrome_options=chrome_options)
        elif self.browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif self.browser == 'safari':
            self.wd = webdriver.Safari()
        else:
            raise ValueError(f'Unrecognized browser {browser_name}')

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)
