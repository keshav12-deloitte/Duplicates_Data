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

# Launch the Appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# Function to find an element by id and assert its text
def assert_element_text_by_id1():
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ID, 'label1')))
    assert element.text == 'Hello', f"Text assertion failed for element {'label1'}"


def assert_element_text_by_id2():
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ID, 'label2')))
    assert element.text == 'World', f"Text assertion failed for element {'label2'}"


def assert_element_text_by_id3():
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((MobileBy.ID, 'label3')))
    assert element.text == 'Login Page', f"Text assertion failed for element {'label3'}"


assert_element_text_by_id1()
assert_element_text_by_id2()
assert_element_text_by_id3()
# Close the Appium server
driver.quit()
