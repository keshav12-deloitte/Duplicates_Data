from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'device',
    'appPackage': 'com.example.app',
    'appActivity': 'com.example.app.MainActivity'
}

# Function to check if an element is visible
def is_element_visible(element_id):
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((MobileBy.ID, element_id)))
        return True
    except:
        return False

# Launch the Appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Test scenario 1
# Perform some actions
if is_element_visible('button1'):
    print("Button 1 is visible")

# Test scenario 5
# Perform some actions with duplicate code
if is_element_visible('button2'):
    print("Button 2 is visible")

if is_element_visible('button3'):
    print("Button 3 is visible")

# Close the Appium server
driver.quit()
