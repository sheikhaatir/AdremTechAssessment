from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class CartSummaryPage:
    '''
    Navigates to the cart summary page and validates the cart details.
    This class handles the cart summary page interactions, including item count, details, and subtotal validation
    '''
    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)
        self.cart_icon = (By.XPATH, "//span[normalize-space()='Shopping cart']")
        self.cart_summary_section = (By.ID, "cart-table")  
        self.cart_items = (By.CSS_SELECTOR, "tr.cart-item-row")  
        self.product_name = (By.CSS_SELECTOR, ".product-name")
        self.unit_price = (By.CSS_SELECTOR, ".product-unit-price")
        self.quantity = (By.CSS_SELECTOR, ".qty-input")
        self.item_total = (By.CSS_SELECTOR, ".product-subtotal")
        self.subtotal = (By.ID, "subtotal")

    def navigate_to_cart(self):
        logger.info("Navigating to cart page")
        self.driver.execute_script("window.scrollTo(0, 0);")  
        cart_icon = self.wait.until(EC.element_to_be_clickable(self.cart_icon))
        cart_icon.click()
        logger.info("Cart icon clicked")
        self.driver.implicitly_wait(10) 
        logger.info("Cart page loaded successfully")
        
    def get_item_count(self):
        logger.info("Getting cart item count")
        items = self.wait.until(EC.presence_of_all_elements_located(self.cart_items))
        return len(items)

    def get_cart_details(self):
        logger.info("Extracting cart details")
        items = self.wait.until(EC.presence_of_all_elements_located(self.cart_items))
        cart_details = []
        for item in items:
            try:
                name = item.find_element(*self.product_name).text.strip()
                qty = int(item.find_element(*self.quantity).get_attribute("value"))
                price = float(item.find_element(*self.unit_price).text.replace("$", "").replace(",", ""))
                total = float(item.find_element(*self.item_total).text.replace("$", "").replace(",", ""))
                cart_details.append({"name": name, "qty": qty, "price": price, "total": total})
                logger.info(f"Found item: {name}, Qty: {qty}, Price: ${price}, Total: ${total}")
            except Exception as e:
                logger.error(f"Error processing item {name}: {str(e)}")
                continue
        return cart_details

    def validate_cart(self, expected_count=None):
        logger.info("Validating cart details")
        item_count = self.get_item_count()
        if expected_count is not None:
            assert item_count == expected_count, f"Expected {expected_count} items, but found {item_count}"
        cart_details = self.get_cart_details()
        calculated_subtotal = sum(item["total"] for item in cart_details)
        displayed_subtotal = float(self.wait.until(EC.presence_of_element_located(self.subtotal)).text.replace("$", "").replace(",", ""))
        assert len(cart_details) > 0, "No items found in cart"
        assert abs(displayed_subtotal - calculated_subtotal) < 0.01, \
            f"Subtotal mismatch: expected {calculated_subtotal}, got {displayed_subtotal}"  
        logger.info(f"Cart validated successfully. Items: {item_count}, Details: {cart_details}, Subtotal: ${displayed_subtotal}")
        return cart_details, displayed_subtotal
    
    def get_total_price(self):
        """
        Calculate the total price of all items in the cart.
        """
        cart_details = self.get_cart_details()
        total_price = sum(item["total"] for item in cart_details)
        logger.info(f"Total price of items in cart: ${total_price}")
        return total_price 
    