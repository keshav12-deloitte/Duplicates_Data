import unittest
from selenium import webdriver


class LoginPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com/login")

    def test_valid_login(self):
        # Test valid login credentials
        username = "myusername"
        password = "mypassword"

        # Locate and interact with the username and password input fields
        username_input = self.driver.find_element_by_id("username")
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_id("password")
        password_input.send_keys(password)

        # Locate and click the login button
        login_button = self.driver.find_element_by_id("login-btn")
        login_button.click()

        # Assertion: Verify successful login
        welcome_message = self.driver.find_element_by_id("welcome-message").text
        expected_message = f"Welcome, {username}!"
        self.assertEqual(welcome_message, expected_message, "Login not successful")

    def test_invalid_login(self):
        # Test invalid login credentials
        username = "invaliduser"
        password = "wrongpassword"

        # Locate and interact with the username and password input fields
        username_input = self.driver.find_element_by_id("username")
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_id("password")
        password_input.send_keys(password)

        # Locate and click the login button
        login_button = self.driver.find_element_by_id("login-btn")
        login_button.click()

        # Assertion: Verify error message is displayed
        error_message = self.driver.find_element_by_id("error-message").text
        expected_message = "Invalid username or password"
        self.assertEqual(error_message, expected_message, "Error message not displayed")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
