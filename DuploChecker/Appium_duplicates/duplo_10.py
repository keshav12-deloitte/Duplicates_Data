from appium import webdriver


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def sign_up(self, username, password):
        username_field = self.driver.find_element_by_id('username')
        username_field.clear()
        username_field.send_keys(username)

        password_field = self.driver.find_element_by_id('password')
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element_by_id('login')
        login_button.click()

    def perform_login(self, username, password):
        username_field = self.driver.find_element_by_id('username')
        username_field.clear()
        username_field.send_keys(username)

        password_field = self.driver.find_element_by_id('password')
        password_field.clear()
        password_field.send_keys(password)
        self.click_login_button()


# Launch the Appium server
desired_caps = {
    'platformName': 'Android',
    'deviceName': 'device',
    'appPackage': 'com.example.app',
    'appActivity': 'com.example.app.MainActivity'
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

login_page = LoginPage(driver)
login_page.perform_login('user1', 'pass1')

login_page.sign_up('user2', 'pass2')
login_page.click_login_button()

driver.quit()
