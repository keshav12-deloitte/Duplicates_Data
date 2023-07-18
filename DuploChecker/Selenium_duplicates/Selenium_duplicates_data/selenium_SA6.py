# Import required modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")

# Using Actions class to right-click on an element
element = driver.find_element_by_xpath("//div[@id='myElement']")
actions = ActionChains(driver)
actions.context_click(element).perform()

# Using JavaScript executor to trigger context menu
element = driver.find_element_by_xpath("//div[@id='myElement']")
driver.execute_script("var event = new MouseEvent('contextmenu', { 'bubbles': true, 'cancelable': true, 'view': window }); arguments[0].dispatchEvent(event);", element)

# Close the WebDriver
driver.quit()

"""

"""
