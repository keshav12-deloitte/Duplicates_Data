# Import required modules
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to a webpage
driver.get("https://www.example.com")

# Trigger an alert dialog
def handling_alert():
    driver.execute_script("alert('This is an alert!');")

# Using switch_to.alert() and accept() method to accept the alert
def handling_alert_type_2():
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.accept()

# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : handling_alert , handling_alert_type_2  are duplicate to each other
"""

