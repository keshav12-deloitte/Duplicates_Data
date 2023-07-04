from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'device',
    'appPackage': 'com.example.app',
    'appActivity': 'com.example.app.MainActivity'
}


# Function to perform login with username and password
def login_with_correct_username(username, password):
    username_field = driver.find_element_by_id('username')
    username_field.clear()
    username_field.send_keys(username)

    password_field = driver.find_element_by_id('password')
    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element_by_id('login')
    login_button.click()


def login_with_incorrect_username(username, password):
    username_field = driver.find_element_by_id('username')
    username_field.clear()
    username_field.send_keys(username)

    password_field = driver.find_element_by_id('password')
    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element_by_id('login')
    login_button.click()


def login_with_incorrect_pasword(username, password):
    username_field = driver.find_element_by_id('username')
    username_field.clear()
    username_field.send_keys(username)

    password_field = driver.find_element_by_id('password')
    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element_by_id('login')
    login_button.click()


def login_with_empty_fields(username, password):
    username_field = driver.find_element_by_id('username')
    username_field.clear()
    username_field.send_keys(username)

    password_field = driver.find_element_by_id('password')
    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element_by_id('login')
    login_button.click()


# Launch the Appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Test scenario 1
# Perform some actions
login_with_correct_username('user1', 'pass1')
login_with_incorrect_username('user112', 'pass1')
login_with_incorrect_pasword('user1', 'pass112')
login_with_empty_fields('', '')
# Close the Appium server
driver.quit()
