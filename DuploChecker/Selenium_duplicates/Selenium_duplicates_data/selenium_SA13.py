# Import required modules
from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")


# Using get_attribute() method
def getting_value_of_input_element_using_get_attribute():
    input_element = driver.find_element_by_xpath("//input[@id='myInput']")
    value = input_element.get_attribute("value")
    print(value)


# Using JavaScript executor
def getting_value_of_input_element_using_javascript_executor():
    input_element = driver.find_element_by_xpath("//input[@id='myInput']")
    value = driver.execute_script("return arguments[0].value;", input_element)
    print(value)


# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : getting_value_of_input_element_using_get_attribute , getting_value_of_input_element_using_javascript_executor  are duplicate to each other
"""

