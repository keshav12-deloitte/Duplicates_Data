# Import required modules
from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")

# Using click() method
def clicking_checkbox():
    checkbox_element = driver.find_element_by_xpath("//input[@id='myCheckbox']")
    checkbox_element.click()

# Using JavaScript executor to toggle checkbox state
def clicking_checkbox_using_javascript_executor():
    checkbox_element = driver.find_element_by_xpath("//input[@id='myCheckbox']")
    driver.execute_script("arguments[0].checked = !arguments[0].checked;", checkbox_element)

# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : clicking_checkbox , clicking_checkbox_using_javascript_executor  are duplicate to each other
"""
