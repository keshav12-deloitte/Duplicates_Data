# Import required modules
from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")

# Using text property
def getting_text_using_text_property():
    element = driver.find_element_by_xpath("//div[@id='myElement']")
    text = element.text
    print(text)

# Using get_attribute() method
def getting_text_using_get_attribute():
    element = driver.find_element_by_xpath("//div[@id='myElement']")
    text = element.get_attribute("textContent")
    print(text)

# Using JavaScript executor
def getting_text_using_javascript_executor():
    element = driver.find_element_by_xpath("//div[@id='myElement']")
    text = driver.execute_script("return arguments[0].textContent;", element)
    print(text)

# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : getting_text_using_text_property , getting_text_using_get_attribute ,getting_text_using_javascript_executor are duplicate to each other
"""
