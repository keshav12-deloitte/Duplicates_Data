from selenium import webdriver

def fill_registration_form(name, email, password):
    driver = webdriver.Chrome()
    driver.get("https://example.com/register")
    name_field = driver.find_element_by_id("name")
    name_field.send_keys(name)
    email_field = driver.find_element_by_id("email")
    email_field.send_keys(email)
    password_field = driver.find_element_by_id("password")
    password_field.send_keys(password)
    driver.quit()


def fill_contact_form(name, email, message):
    driver = webdriver.Chrome()
    driver.get("https://example.com/contact")
    name_field = driver.find_element_by_id("name")
    name_field.send_keys(name)
    email_field = driver.find_element_by_id("email")
    email_field.send_keys(email)
    message_field = driver.find_element_by_id("message")
    message_field.send_keys(message)
    driver.quit()