import logging
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class OrderCompletionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.success_message = (By.XPATH, "//*[contains(text(), 'Your order has been successfully processed!')]")
        self.order_number_element = (By.XPATH, "//*[contains(text(), 'Order number:')]")
        self.order_details_link = (By.XPATH, "//a[contains(text(), 'Click here for order details')]")

    def confirm_and_validate_order(self):
        logger.info("Validating order completion page")
        '''
        Assert presence of success message and extract order number. 
        '''
        try:
            success_message = self.wait.until(EC.presence_of_element_located(self.success_message))
            logger.info("Success message found: %s", success_message.text)
            assert "Your order has been successfully processed!" in success_message.text, "Success message not found"
            order_number_element = self.wait.until(EC.presence_of_element_located(self.order_number_element))
            order_number_text = order_number_element.text
            order_number_match = re.search(r'Order number:\s*(\d+)', order_number_text)
            if not order_number_match:
                raise AssertionError("No valid order number found in: %s" % order_number_text)
            order_number = order_number_match.group(1)
            logger.info("Extracted order number: %s", order_number)
            assert order_number.isdigit(), "Extracted order number is not a valid number: %s" % order_number
            order_details_link = self.wait.until(EC.element_to_be_clickable(self.order_details_link))
            order_details_link.click()
            logger.info("Navigated to order details page for order number: %s", order_number)
            return self  # Return self to allow chaining 
        except Exception as e:
            logger.error("Order completion validation failed: %s", str(e))
            raise