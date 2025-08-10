import pytest
import allure
import logging
import unittest
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage 
from pages.home_page import HomePage 
from utils.json_reader import JsonReader
from pages.search_and_add_multiple_products import SearchAndAddMultipleProducts
from pages.cart_summary_page import CartSummaryPage
from pages.checkout_page import CheckoutPage 
from pages.shipping_billing_address_page import ShippingBillingAdressPage
from pages.submit_order_page import SubmitOrderPage
from pages.order_completion_page import OrderCompletionPage

logger = logging.getLogger(__name__)

@allure.feature("E-commerce Checkout")
@allure.story("End-to-End Checkout Flow")

def test_checkout_flow(driver):
    '''
    This main file performs an end-to-end checkout flow on the e-commerce website.
    '''
    try:
        with allure.step("Load test data"):
            test_data = JsonReader.read_test_data("test_data.json")
        # Step 1: Login with newly created credentials 
        with allure.step("Login to the application"):
            login_page = LoginPage(driver)
            driver.get("https://demowebshop.tricentis.com/login")
            logger.info("Navigating to login page")
            login_page.login(test_data["credentials"]["email"], test_data["credentials"]['password']) # Enters Test Credentials
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Log out")))
            logger.info("Login successful")
            assert driver.find_element(By.LINK_TEXT, "Log out").is_displayed(), "Login failed"          
    except Exception as e:
        logger.error("Login Failed : %s", str(e))
        screenshot_path = f"screenshots/error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(
            screenshot_path,
            name="Login Failed Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        raise
    try: 
        # Step 2: Choose item from homepage
        with allure.step("Select item from homepage"):
            home_page = HomePage(driver)
            home_page.scroll_to_item()
            home_page.choose_item()
            logger.info("Item selected from homepage")  
            driver.implicitly_wait(10)  
            home_page.enter_recipent_information(test_data["credentials"]['recipient_name'], test_data["credentials"]['recipient_email'])
            logger.info("Recipient information entered")    
            home_page.add_to_cart() 
            driver.implicitly_wait(15) 
            assert home_page.item_is_added_to_cart(), "Item not added to cart"            
            logger.info("Item added to cart successfully")
            driver.implicitly_wait(10)  
    except Exception as e: 
        logger.error("Unable to Add Item from Home Page: %s", str(e))
        screenshot_path = f"screenshots/home_page_error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(
            screenshot_path,
            name="Unable to Add Item Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        raise
    # Step 3: Search and add multiple products  
    try:
        with allure.step("Search and add Multiple Products to cart"):
            multiple_products = SearchAndAddMultipleProducts(driver)
            for product in test_data["products"]:
                try:
                    logger.info(f"Processing product: {product['name']}")
                    multiple_products.search_and_select_product(product['name'])
                    multiple_products.scroll_to_item()
                    logger.info(f"Scrolling to Add to Cart button for product: {product['name']}")
                    multiple_products.add_to_cart(product['add_to_cart_xpath'])
                    logger.info(f"Product '{product['name']}' added to cart")
                except Exception as e:
                    logger.error(f"Failed to process product {product['name']}: {e}")
                    continue  # Continue with the next product
            logger.info("All products processed successfully")
            driver.implicitly_wait(20)        
    except Exception as e: 
        logger.error("Unable to Add Item from Search Page: %s", str(e))
        screenshot_path = f"screenshots/search_error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(
            screenshot_path,
            name="Unable to Search and Add Product Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        raise    
    # Step 4: Validate cart summary 
    try:
        with allure.step("Validate cart summary"):
            cart_page = CartSummaryPage(driver)
            cart_page.navigate_to_cart()
            cart_page.get_item_count()
            cart_page.get_cart_details()
            logger.info('Getting cart details')
            cart_page.get_total_price()
            logger.info("Cart validated successfully")
            
    except Exception as e: 
        logger.error("Navigation to Cart Failed: %s", str(e))
        screenshot_path = f"screenshots/cart_navigation_error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(
            screenshot_path,
            name="Navigation to Cart Error Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        raise 
    # Step 5: Proceed to checkout
    try:
        with allure.step("Proceed to checkout"):
            checkout_page = CheckoutPage(driver)
            checkout_page.agree_to_terms()
            logger.info("Agreed to terms of service")
            checkout_page.proceed_to_checkout()
            logger.info("Proceeded to checkout") 
            driver.implicitly_wait(10)  
    except Exception as e:
        logger.error("Checkout Failed: %s", str(e))
        screenshot_path = f"screenshots/checkout_error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(
            screenshot_path,
            name="Checkout Error Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        raise
    # Step 6: Enter billing address
    try:
        with allure.step("Enter billing address"):
            
            shipping_billing_address_page = ShippingBillingAdressPage(driver)
            shipping_billing_address_page.enter_billing_address(test_data["shipping_billing_address"])
            logger.info("Successfully entered billing address")    
    except Exception as e:
        logger.error("Billing Address Entry Failed: %s", str(e))
        screenshot_path = f"screenshots/billing_address_error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(
            screenshot_path,
            name="Billing Address Error Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        raise  
    try: 
        # Step 7: Submit order
        with allure.step("Submit order"):
            submit_order_page = SubmitOrderPage(driver)
            submit_order_page.submit_order()
            driver.implicitly_wait(10)        
    except Exception as e:
        logger.error("Order Submission Failed: %s", str(e))
        screenshot_path = f"screenshots/order_submission_error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(
            screenshot_path,
            name="Order Submission Error Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        raise
    # Step 8: Validate order confirmation
    try:
        with allure.step("Validate Order confirmation"):
            order_confirmation_page = OrderCompletionPage(driver)
            order_confirmation_page.confirm_and_validate_order()
            logger.info("Order Confirmation Validated") 
            logger.info("Test Completed Successfully !")
    
    except Exception as e:
        logger.error("Order Confirmation Validation Failed: %s", str(e))
        screenshot_path = f"screenshots/order_confirmation_error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(screenshot_path)
        allure.attach.file(
            screenshot_path,
            name="Order Confirmation Error Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        raise
if __name__ == "__main__":
    unittest.main()
            
    