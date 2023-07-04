from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'device',
    'appPackage': 'com.example.app',
    'appActivity': 'com.example.app.MainActivity'
}


# Function to validate input field
def validate_input_username():
    field_element = driver.find_element_by_id('username')
    field_element.clear()
    field_element.send_keys('')

    error_element = driver.find_element_by_id("username_error")
    actual_error_message = error_element.text
    assert actual_error_message == 'Please enter a value'

def validate_input_password():
    field_element = driver.find_element_by_id('password')
    field_element.clear()
    field_element.send_keys('')

    error_element = driver.find_element_by_id("password_error")
    actual_error_message = error_element.text
    assert actual_error_message == 'Please enter a value'

# Launch the Appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Test scenario 1
# Perform some actions
validate_input_username()
validate_input_password()

# Close the Appium server
driver.quit()
