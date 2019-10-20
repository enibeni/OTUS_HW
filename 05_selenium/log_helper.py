import os
import time
import logging
import sqlite3
from datetime import date
from selenium.webdriver.support.event_firing_webdriver import AbstractEventListener


initial_sql = """CREATE TABLE IF NOT EXISTS log(
                    TimeStamp TEXT,
                    FuncName TEXT,
                    LogLevelName TEXT,
                    Message TEXT,
                    Exception TEXT
               )"""

insertion_sql = """INSERT INTO log(
                    TimeStamp,
                    FuncName,
                    LogLevelName,
                    Message,
                    Exception
               )
               VALUES (
                    '%(dbtime)s',
                    '%(funcName)s',
                    '%(levelname)s',
                    '%(msg)s',
                    '%(exc_text)s'
               );
               """


class SQLiteLoggerHandler(logging.Handler):

    def __init__(self, db='log.db'):
        logging.Handler.__init__(self)
        self.db = db
        conn = sqlite3.connect(self.db)
        conn.execute(initial_sql)
        conn.commit()

    def format_time(self, record):
        """ Create a time stamp
        """
        record.dbtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))

    def emit(self, record):
        self.format(record)
        self.format_time(record)
        if record.exc_info:  # for exceptions
            record.exc_text = logging._defaultFormatter.formatException(record.exc_info)
        else:
            record.exc_text = ""

        # Insert the log record
        sql = insertion_sql % record.__dict__
        conn = sqlite3.connect(self.db)
        conn.execute(sql)
        conn.commit()


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

        db_log = SQLiteLoggerHandler()
        logger.addHandler(db_log)
        return logger


class MyListener(AbstractEventListener):

    def __init__(self, logger):
        self.logger = logger

    def on_exception(self, exception, driver):
        self.logger.error(exception)
        scr_directory = './screenshots/'
        os.makedirs(scr_directory, exist_ok=True)
        driver.save_screenshot(f'{scr_directory}{driver.name}_{time.strftime("%Y-%m-%d_%H:%M:%S")}.png')
