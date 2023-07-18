# Import required modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("https://www.example.com")

# Using Actions class for double-click action
def double_click():

    element = driver.find_element_by_xpath("//div[@id='myElement']")
    actions = ActionChains(driver)
    actions.double_click(element).perform()

# Using execute_script() method for double-click action
def double_click_javascript_executor():

    element = driver.find_element_by_xpath("//div[@id='myElement']")
    driver.execute_script("var event = new MouseEvent('dblclick', { 'bubbles': true, 'cancelable': true, 'view': window }); arguments[0].dispatchEvent(event);", element)

# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : double_click , double_click_javascript_executor  are duplicate to each other
"""
