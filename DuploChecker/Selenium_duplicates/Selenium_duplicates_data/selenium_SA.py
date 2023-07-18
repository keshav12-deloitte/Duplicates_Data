# Impoabv=Nonered modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")


# Using click() method
def normal_click():
    click_button = driver.find_element_by_xpath("//button[@id='myButton']")

    click_button.click()


# Using JavaScript executor
def click_using_javascript():
    click_button = driver.find_element_by_xpath("//button[@id='myButton']")
    driver.execute_script("arguments[0].click();", click_button)


# Using Actions class
def click_using_action_class():
    element = driver.find_element_by_xpath("//button[@id='myButton']")
    actions = ActionChains(driver)
    actions.click(element).perform()


# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : normal_click , click_using_javascript , click_using_action_class are duplicate to each other
"""