# Import required modules
from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("https://www.example.com")


# Using title property
def get_title():
    title = driver.title
    print(title)


# Using execute_script() method
def get_title_using_javascript_executor():
    title = driver.execute_script("return document.title;")
    print(title)


# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : get_title , get_title_using_javascript_executor  are duplicate to each other
"""

