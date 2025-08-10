import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class CheckoutPage: 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.agree_terms_checkbox = (By.ID, "termsofservice")
        self.checkout_button = (By.ID, "checkout")
        self.cart_summary_link = (By.LINK_TEXT, "Shopping cart")  
    
    def agree_to_terms(self):
        logger.info("Agreeing to terms of service")
        self.wait.until(EC.element_to_be_clickable(self.agree_terms_checkbox)).click()
    
    def proceed_to_checkout(self):
        logger.info("Proceed to checkout")
        self.wait.until(EC.element_to_be_clickable(self.checkout_button)).click()