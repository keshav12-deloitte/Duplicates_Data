# Import required modules
from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("https://www.example.com")


# Using is_displayed() method
def element_is_displayed():
    element = driver.find_element_by_xpath("//div[@id='myElement']")
    is_displayed = element.is_displayed()
    print(is_displayed)


# Using execute_script() method to check display property
def element_is_displayed_using_javascript():
    element = driver.find_element_by_xpath("//div[@id='myElement']")
    is_displayed = driver.execute_script("return window.getComputedStyle(arguments[0]).display !== 'none';", element)
    print(is_displayed)


# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : element_is_displayed , element_is_displayed_using_javascript  are duplicate to each other
"""
