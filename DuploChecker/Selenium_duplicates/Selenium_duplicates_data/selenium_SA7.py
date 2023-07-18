# Import required modules
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")

# Using Select class and option value
def clicking_on_dropdown_using_value():
    select_element = Select(driver.find_element_by_xpath("//select[@id='myDropdown']"))
    select_element.select_by_value("option_value")

# Using Select class and visible text
def clicking_on_dropdown_by_visible_value():
    select_element = Select(driver.find_element_by_xpath("//select[@id='myDropdown']"))
    select_element.select_by_visible_text("Option Text")

# Using JavaScript executor to select an option
def clicking_dropdown_using_javascript_executor():
    option_element = driver.find_element_by_xpath("//option[@value='option_value']")
    driver.execute_script("arguments[0].selected = true;", option_element)

# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : clicking_on_dropdown_using_value , clicking_on_dropdown_by_visible_value   clicking_dropdown_using_javascript_executor are duplicate to each other"""
