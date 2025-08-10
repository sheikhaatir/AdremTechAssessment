import pytest
import logging
from selenium import webdriver
from utils.driver_factory import DriverFactory
import logging
import os
from datetime import datetime

'''
This is a pytest configuration file that sets up the logging and WebDriver for the tests.
'''
@pytest.fixture(scope='session')
def logger():
    return logging.getLogger(__name__)

logger = logging.getLogger(__name__)
@pytest.fixture(scope="function")
def driver():
    logger.info("Setting up WebDriver")
    driver = DriverFactory.get_driver()
    driver.maximize_window()
    yield driver
    logger.info("Tearing down WebDriver")
    driver.quit()

