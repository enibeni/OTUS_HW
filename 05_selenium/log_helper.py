import os
import time
import logging
from datetime import date
from selenium.webdriver.support.event_firing_webdriver import AbstractEventListener


class SessionLogger:

    def __init__(self, name):
        self.name = name

    def start_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.DEBUG)

        log_directory = './logs/'
        os.makedirs(log_directory, exist_ok=True)
        file_log = logging.FileHandler(f'logs/logs_{date.today()}.log')
        file_log.setLevel(logging.DEBUG)
        file_format = logging.Formatter('%(levelname)-5s [%(asctime)s] [%(name)s]: %(message)s')
        file_log.setFormatter(file_format)
        logger.addHandler(file_log)

        console_log = logging.StreamHandler()
        console_log.setLevel(logging.DEBUG)
        console_format = logging.Formatter('%(levelname)-5s [%(asctime)s] [%(name)s]: %(message)s')
        console_log.setFormatter(console_format)
        logger.addHandler(console_log)
        return logger


class MyListener(AbstractEventListener):

    def __init__(self, logger):
        self.logger = logger

    def on_exception(self, exception, driver):
        self.logger.error(exception)
        scr_directory = './screenshots/'
        os.makedirs(scr_directory, exist_ok=True)
        driver.save_screenshot(f'{scr_directory}{driver.name}_{time.strftime("%Y-%m-%d_%H:%M:%S")}.png')
