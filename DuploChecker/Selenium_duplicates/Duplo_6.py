from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def login(username, password):
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")
    username_field = driver.find_element_by_id("username")
    password_field = driver.find_element_by_id("password")
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button = driver.find_element_by_id("login-button")
    login_button.click()
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "success-message"))
    )
    assert success_message.text == "Login successful"
    driver.quit()

def register(name, email, password):
    driver = webdriver.Chrome()
    driver.get("https://example.com/register")
    name_field = driver.find_element_by_id("name")
    email_field = driver.find_element_by_id("email")
    password_field = driver.find_element_by_id("password")
    name_field.send_keys(name)
    email_field.send_keys(email)
    password_field.send_keys(password)
    register_button = driver.find_element_by_id("register-button")
    register_button.click()
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "success-message"))
    )
    assert success_message.text == "Registration successful"
    driver.quit()
