# Import required modules
from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("https://www.example.com")

# Using refresh() method
def refresh_page():
    driver.refresh()

# Using navigate.refresh() method
def using_navigate_refresh():

    driver.navigate.refresh()

# Using execute_script() method to refresh the page
def refresh_using_javascript():

    driver.execute_script("location.reload();")

# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : refresh_page , using_navigate_refresh , refresh_using_javascript are duplicate to each other
"""

