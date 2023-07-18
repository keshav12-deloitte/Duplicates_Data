from selenium.webdriver.chrome import webdriver


class Class2:
    def __init__(self):
        self.driver = None

    def open_browser(self):
        self.driver = webdriver.ChromeRemoteConnection

    def login(self, username, password):
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("login_btn").click()

    def navigate_to_dashboard(self):
        self.driver.find_element_by_id("dashboard_link").click()

    def perform_action(self):
        self.driver.find_element_by_id("action_button").click()

    def close_browser(self):
        self.driver.quit()
