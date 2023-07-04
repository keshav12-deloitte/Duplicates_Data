from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'device',
    'appPackage': 'com.example.app',
    'appActivity': 'com.example.app.MainActivity'
}


# Function to toggle a checkbox by ID
def toggle_checkbox1():
    checkbox = driver.find_element_by_id('checkbox1')
    checkbox.click()


def toggle_checkbox2():
    checkbox = driver.find_element_by_id('checkbox2')
    checkbox.click()


def toggle_checkbox3():
    checkbox = driver.find_element_by_id('checkbox3')
    checkbox.click()


# Launch the Appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

toggle_checkbox1()
toggle_checkbox2()
toggle_checkbox3()
# Close the Appium server
driver.quit()
