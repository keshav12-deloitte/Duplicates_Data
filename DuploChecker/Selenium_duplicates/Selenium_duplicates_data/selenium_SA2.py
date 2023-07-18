# Import required modules
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")


# Using JavaScript executor to scroll to an element
def scroll_using_javascript_executor():
    element = driver.find_element_by_xpath("//div[@id='myElement']")
    driver.execute_script("arguments[0].scrollIntoView();", element)


# Using Actions class to scroll by offset

def scroll_using_action_class():
    actions = ActionChains(driver)
    actions.move_by_offset(0, 500).perform()  # Scroll down by 500 pixels


# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : scroll_using_javascript_executor , scroll_using_action_class  are duplicate to each other
"""
