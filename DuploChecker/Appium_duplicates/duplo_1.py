from appium import webdriver
import unittest

class AppiumTest :
    def  setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.example.app',
            'appActivity': 'com.example.app.MainActivity'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def verify_element_visible(self, element_id):
        element = self.driver.find_element_by_id(element_id)
        self(element.is_displayed(), "Element is not visible")

    def test_verify_login_button_visible(self):
        # Code for navigating to the login page
        self.driver.find_element_by_id("login_page_button").click()

        # Verification
        self.verify_element_visible("login_button")

    def test_verify_signup_button_visible(self):
        # Code for navigating to the signup page
        self.driver.find_element_by_id("signup_page_button").click()

        # Verification
        self.verify_element_visible("signup_button")

if __name__ == '__main__':
    unittest.main()

