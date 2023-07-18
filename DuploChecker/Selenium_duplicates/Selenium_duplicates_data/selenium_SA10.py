# Import required modules
from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")

# Using clear() method
def clear_input():
    input_element = driver.find_element_by_xpath("//input[@id='myInput']")
    input_element.clear()

# Using JavaScript executor to clear the input value
def clear_using_javascript_executor():
    input_element = driver.find_element_by_xpath("//input[@id='myInput']")
    driver.execute_script("arguments[0].value = '';", input_element)

# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : clear_input , clear_using_javascript_executor  are duplicate to each other
"""

