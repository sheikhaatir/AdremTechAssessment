import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

class LoginPage:
    '''
    Login with newly created credentials. Takes data from test_data.json.
    '''
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.email_field = (By.ID, "Email")
        self.password_field = (By.ID, "Password")
        self.login_button = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input")

    def login(self, email, password):
        logger.info("Entering email: %s", email)
        self.wait.until(EC.presence_of_element_located(self.email_field)).send_keys(email)
        logger.info("Entering password")
        self.wait.until(EC.presence_of_element_located(self.password_field)).send_keys(password)
        logger.info("Clicking login button")
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()