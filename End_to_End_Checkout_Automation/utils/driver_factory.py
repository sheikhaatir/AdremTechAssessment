from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver():
        options = webdriver.ChromeOptions()
        # Disable popups and password manager
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--incognito")  
        options.add_argument("--disable-save-password-bubble")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2, 
            "profile.default_content_settings.cookies": 2, 
            "profile.block_third_party_cookies": True,
            "profile.formfill_enabled": False 
        })
        return webdriver.Chrome(options=options)
