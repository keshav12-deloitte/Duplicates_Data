from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'device',
    'appPackage': 'com.example.app',
    'appActivity': 'com.example.app.MainActivity'
}

# Launch the Appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# Function to find an element by id and click on it
def find_element_by_id_and_click():
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ID, 'button1')))
    element.click()


def find_element_by_id_and_click():
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ID, 'button2')))
    element.click()


def find_element_by_id_and_click():
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ID, 'button3')))
    element.click()


def find_element_by_id_and_click():
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ID, 'button4')))
    element.click()



# Close the Appium server
driver.quit()
