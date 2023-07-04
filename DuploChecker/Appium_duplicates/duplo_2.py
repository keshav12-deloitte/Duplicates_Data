from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'device',
    'appPackage': 'com.example.app',
    'appActivity': 'com.example.app.MainActivity'
}

# Function to perform a swipe action
def swipe(start_x, start_y, end_x, end_y):
    action = TouchAction(driver)
    action.press(x=start_x, y=start_y).wait(1000).move_to(x=end_x, y=end_y).release().perform()

# Function to find an element by id and click on it
def find_element_by_id_and_click(element_id):
    element = driver.find_element_by_id(element_id)
    element.click()

# Function to find an element by class name and click on it
def find_element_by_class_name_and_click(class_name):
    element = driver.find_element_by_class_name(class_name)
    element.click()

# Launch the Appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Test scenario 1
# Perform some actions
find_element_by_id_and_click('button1')
swipe(100, 500, 100, 100)
find_element_by_class_name_and_click('android.widget.Button')

# Test scenario 2
# Perform some actions with duplicate code
def find_element_by_id_and_tap(element_id):
    element = driver.find_element_by_id(element_id)
    element.click()

def find_element_by_class_name_and_tap(class_name):
    element = driver.find_element_by_class_name(class_name)
    element.click()

find_element_by_id_and_tap('button2')
swipe(200, 500, 200, 100)
find_element_by_class_name_and_tap('android.widget.Button')

# Test scenario 3
# Perform some actions with duplicate code
def find_element_by_id_and_press(element_id):
    element = driver.find_element_by_id(element_id)
    element.click()

def find_element_by_class_name_and_press(class_name):
    element = driver.find_element_by_class_name(class_name)
    element.click()

find_element_by_id_and_press('button3')
swipe(300, 500, 300, 100)
find_element_by_class_name_and_press('android.widget.Button')

# Close the Appium server
driver.quit()
