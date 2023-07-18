# Import required modules
from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()

# Navigate to the webpage
driver.get("https://www.example.com")

# Using switch_to.frame() method
def switch_to_frame():

    iframe_element = driver.find_element_by_xpath("//iframe[@id='myIframe']")
    driver.switch_to.frame(iframe_element)

# Using switch_to.frame() method with frame index
def switch_to_frame_using_index():

    driver.switch_to.frame(0)  # Switch to the first iframe

# Using switch_to.frame() method with frame name or ID
def switch_to_frame_using_framename():

    driver.switch_to.frame("frameName")  # Switch to iframe with name or ID "frameName"

# Using switch_to.frame() method with frame WebElement
def switch_to_frame_using_frame_webelement():
    iframe_element = driver.find_element_by_xpath("//iframe[@id='myIframe']")
    driver.switch_to.frame(iframe_element)

# Close the WebDriver
driver.quit()

"""
Yes i could find duplicate code from the above given code :
Method name : switch_to_frame_using_index , switch_to_frame_using_framename switch_to_frame_using_frame_webelement are duplicate to each other
"""
