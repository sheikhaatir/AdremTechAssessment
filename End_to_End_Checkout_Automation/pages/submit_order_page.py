import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.order_completion_page import OrderCompletionPage

logger = logging.getLogger(__name__)

class SubmitOrderPage: 
    '''
    Handles the submit order page interactions.
    '''
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.submit_order_button = (By.XPATH, "//input[@value='Continue']")

    def submit_order(self):
        """Click confirm button to place the order and load Thank You page."""
        logger.info("Submitting Order")
        confirm_button = self.driver.find_element(By.XPATH, "//input[@value='Confirm']")
        logger.info("Clicking confirm button to place the order")
        confirm_button.click() 
        logging.info("Confirm button clicked. Waiting for Thank You page to load...")
        return OrderCompletionPage(self.driver)
