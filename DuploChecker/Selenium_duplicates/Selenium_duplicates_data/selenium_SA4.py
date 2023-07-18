# Import required modules
from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")


# Using send_keys()
def entering_keys():
    element = driver.find_element_by_xpath("//input[@id='myInput']")
    element.send_keys("Hello, World!")


# Using JavaScript executor
def entering_keys_using_javascript_executor():
    element = driver.find_element_by_xpath("//input[@id='myInput']")
    driver.execute_script("arguments[0].value = 'Hello, World!';", element)


# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : entering_keys , entering_keys_using_javascript_executor  are duplicate to each other
"""
