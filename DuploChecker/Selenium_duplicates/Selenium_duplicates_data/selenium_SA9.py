# Import required modules
from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")

# Using submit() method on a form element
def submitting_a_form():

    form_element = driver.find_element_by_xpath("//form[@id='myForm']")
    form_element.submit()

# Using JavaScript executor to submit a form
def submitting_a_form_using_javascript_executor():
    form_element = driver.find_element_by_xpath("//form[@id='myForm']")
    driver.execute_script("arguments[0].submit();", form_element)

# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : submitting_a_form , submitting_a_form_using_javascript_executor  are duplicate to each other
"""

