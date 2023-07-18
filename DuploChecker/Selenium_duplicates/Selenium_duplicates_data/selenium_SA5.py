# Import required modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")

# Using Actions class to hover over an element
def normal_hover():
    element = driver.find_element_by_xpath("//div[@id='myElement']")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

# Using JavaScript executor to trigger hover event
def hover_using_javasript():
        
    element = driver.find_element_by_xpath("//div[@id='myElement']")
    driver.execute_script("var event = new MouseEvent('mouseover', { 'bubbles': true, 'cancelable': true, 'view': window }); arguments[0].dispatchEvent(event);", element)

# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : normal_hover , hover_using_javasript  are duplicate to each other
"""
