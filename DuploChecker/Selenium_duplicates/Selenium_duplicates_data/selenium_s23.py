# Import required modules
from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()


# Open a new browser window/tab
def switch_to_window():
    driver.execute_script("window.open('https://www.example.com');")


# Using switch_to.window() method
def switch_to_window_using_index():
    handles = driver.window_handles
    driver.switch_to.window(handles[1])  # Switch to the newly opened window/tab


# Using switch_to.window() method with window name or handle
def switch_to_window_by_name():
    driver.switch_to.window("window_name")  # Switch to window with the given name or handle


# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : switch_to_window , switch_to_window_using_index , switch_to_window_by_name are duplicate to each other
"""
