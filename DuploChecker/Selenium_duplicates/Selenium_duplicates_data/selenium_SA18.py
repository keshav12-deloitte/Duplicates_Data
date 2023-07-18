# Import required modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("https://www.example.com")


# Using Actions class for drag and drop
def drag_and_drop_to_target_location():
    source_element = driver.find_element_by_xpath("//div[@id='sourceElement']")
    target_element = driver.find_element_by_xpath("//div[@id='targetElement']")
    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()


# Using execute_script() method for drag and drop
def drag_and_drag_using_javascript():
    source_element = driver.find_element_by_xpath("//div[@id='sourceElement']")
    target_element = driver.find_element_by_xpath("//div[@id='targetElement']")
    driver.execute_script(
        "var source = arguments[0], target = arguments[1]; var event = new MouseEvent('mousedown', { 'bubbles': true, 'cancelable': true, 'view': window, 'clientX': source.getBoundingClientRect().left + (source.offsetWidth / 2), 'clientY': source.getBoundingClientRect().top + (source.offsetHeight / 2) }); source.dispatchEvent(event); event = new MouseEvent('mousemove', { 'bubbles': true, 'cancelable': true, 'view': window, 'clientX': target.getBoundingClientRect().left + (target.offsetWidth / 2), 'clientY': target.getBoundingClientRect().top + (target.offsetHeight / 2) }); target.dispatchEvent(event); event = new MouseEvent('mouseup', { 'bubbles': true, 'cancelable': true, 'view': window, 'clientX': target.getBoundingClientRect().left + (target.offsetWidth / 2), 'clientY': target.getBoundingClientRect().top + (target.offsetHeight / 2) }); target.dispatchEvent(event);",
        source_element, target_element)


# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : drag_and_drop_to_target_location , drag_and_drag_using_javascript  are duplicate to each other
"""

