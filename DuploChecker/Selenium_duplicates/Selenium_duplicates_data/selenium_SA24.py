# Import required modules
from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()


# Maximize the browser window using maximize_window() method
def maximize_window():
    driver.maximize_window()


# Using execute_script() method to maximize the window
def maximize_window_javascript():
    driver.execute_script("window.moveTo(0, 0); window.resizeTo(window.screen.availWidth, window.screen.availHeight);")

# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : maximize_window , maximize_window_javascript  are duplicate to each other
"""

