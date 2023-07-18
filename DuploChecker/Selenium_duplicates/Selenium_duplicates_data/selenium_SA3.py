# Import required modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")


# Using Actions class to perform a long press
def long_press_using_action_class():
    element = driver.find_element_by_xpath("//div[@id='myElement']")
    actions = ActionChains(driver)
    actions.click_and_hold(element).perform()


# Using JavaScript executor to simulate long press
def long_press_using_javascript_executor():
    element = driver.find_element_by_xpath("//div[@id='myElement']")
    driver.execute_script(
        "arguments[0].dispatchEvent(new MouseEvent('mousedown', { 'bubbles': true, 'cancelable': true, 'view': window, 'which': 1 }));",
        element)
    # Perform additional actions or wait for a desired duration
    driver.execute_script(
        "arguments[0].dispatchEvent(new MouseEvent('mouseup', { 'bubbles': true, 'cancelable': true, 'view': window, 'which': 1 }));",
        element)


# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : long_press_using_action_class , long_press_using_javascript_executor  are duplicate to each other
"""
