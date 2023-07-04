from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'device',
    'appPackage': 'com.example.app',
    'appActivity': 'com.example.app.MainActivity'
}

# Function to navigate to a specific page
def navigate_to_home_page():
    driver.find_element_by_accessibility_id('Home').click()


def navigate_to_account_page():
    driver.find_element_by_accessibility_id('Account').click()

def navigate_to_settings_page():
    driver.find_element_by_accessibility_id('Settings').click()

# Launch the Appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


navigate_to_home_page()
navigate_to_settings_page()
navigate_to_account_page()


driver.quit()
