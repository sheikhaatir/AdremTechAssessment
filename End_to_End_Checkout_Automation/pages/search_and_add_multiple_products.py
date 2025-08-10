from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import logging
from utils.json_reader import JsonReader 

logger = logging.getLogger(__name__)

class SearchAndAddMultipleProducts:
    '''
    Search each item from text box and select it from the search results.
    '''
    def __init__(self, driver, wait_time=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)
        self.search_field = (By.ID, "small-searchterms")
        self.search_button = (By.XPATH, "//input[@value='Search']")
        self.test_data = JsonReader.read_test_data("test_data.json")["products"]

    def navigate_to_homepage(self):
        try:
            homepage_url = "https://demowebshop.tricentis.com"
            if self.driver.current_url != homepage_url:
                logger.info("Navigating to homepage")
                self.driver.get(homepage_url)
                self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".header-logo"))
                )
                logger.info("Homepage loaded successfully")
        except Exception as e:
            logger.error(f"Error navigating to homepage: {e}")
            raise

    def search_and_select_product(self, product_name):
        try:
            logger.info(f"Searching for product: {product_name}")
            self.navigate_to_homepage()
            search_input = self.wait.until(EC.element_to_be_clickable(self.search_field))
            search_input.click()
            search_input.clear()
            search_input.send_keys(product_name)
            try:
                self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ui-autocomplete")))
                search_input.send_keys(Keys.ARROW_DOWN)
                search_input.send_keys(Keys.ENTER)
                logger.info(f"Selected {product_name} from autocomplete")
            except:
                logger.info(f"No autocomplete for {product_name}, clicking search button")
                search_button = self.wait.until(EC.element_to_be_clickable(self.search_button))
                search_button.click()
                self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-title")))
            expected_url = next(
                (product["url"] for product in self.test_data if product["name"] == product_name),
                None
            )
            if expected_url and self.driver.current_url != expected_url:
                logger.warning(f"Unexpected URL: {self.driver.current_url}, expected: {expected_url}")
            logger.info(f"Navigated to product page for: {product_name}")
        except Exception as e:
            logger.error(f"Error searching for product {product_name}: {e}")
            self.driver.save_screenshot(f"error_search_{product_name.replace(' ', '_')}.png")
            raise

    def scroll_to_item(self):
        """Scroll to ensure the page is in view."""
        try:
            logger.info("Scrolling to view the page")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except Exception as e:
            logger.error(f"Error scrolling: {e}")
            raise

    def add_to_cart(self, add_to_cart_xpath):
        try:
            logger.info(f"Attempting to add product to cart with XPath: {add_to_cart_xpath}")
            # Wait for the "Add to Cart" button to be clickable
            cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart_xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cart_button)
            cart_button.click()
            logger.info("Successfully clicked Add to Cart button")
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bar-notification.success")))
            logger.info("Product added to cart successfully")
        except Exception as e:
            logger.error(f"Error adding product to cart with XPath {add_to_cart_xpath}: {e}")
            self.driver.save_screenshot(f"error_add_to_cart_{add_to_cart_xpath.replace('/', '_')}.png")
            raise