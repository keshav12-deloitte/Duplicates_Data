# Import required modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("https://www.example.com")

# Using send_keys() method with Keys.ENTER
def send_keys_and_enter():

    input_element = driver.find_element_by_xpath("//input[@id='myInput']")
    input_element.send_keys(Keys.ENTER)

def send_keys_using_javascript():

    # Using execute_script() method to submit form by pressing Enter key
    input_element = driver.find_element_by_xpath("//input[@id='myInput']")
    driver.execute_script("arguments[0].dispatchEvent(new KeyboardEvent('keydown', { 'bubbles': true, 'cancelable': true, 'key': 'Enter', 'keyCode': 13, 'which': 13 }));", input_element)

# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : send_keys_and_enter , send_keys_using_javascript  are duplicate to each other
"""


