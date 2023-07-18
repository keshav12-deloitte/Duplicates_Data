# Import required modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")

# Using Actions class for drag and drop
def drag_drop_using_action_class():

    source_element = driver.find_element_by_xpath("//div[@id='sourceElement']")
    target_element = driver.find_element_by_xpath("//div[@id='targetElement']")
    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()

# Using JavaScript executor for drag and drop
def drag_drop_using_javascript_executor():

    source_element = driver.find_element_by_xpath("//div[@id='sourceElement']")
    target_element = driver.find_element_by_xpath("//div[@id='targetElement']")
    driver.execute_script("var event = new MouseEvent('mousedown', { 'bubbles': true, 'cancelable': true, 'view': window }); arguments[0].dispatchEvent(event);", source_element)
    driver.execute_script("var event = new MouseEvent('mousemove', { 'bubbles': true, 'cancelable': true, 'view': window, 'clientX': 200, 'clientY': 200 }); arguments[0].dispatchEvent(event);", target_element)
    driver.execute_script("var event = new MouseEvent('mouseup', { 'bubbles': true, 'cancelable': true, 'view': window }); arguments[0].dispatchEvent(event);", target_element)

# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : drag_drop_using_action_class , drag_drop_using_javascript_executor  are duplicate to each other
"""
