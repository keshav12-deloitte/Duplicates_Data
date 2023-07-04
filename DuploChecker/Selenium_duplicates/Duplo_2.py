from selenium import webdriver
from selenium.webdriver.support.ui import Select


def select_country(country):
    driver = webdriver.Chrome()
    driver.get("https://example.com/registration")
    country_dropdown = Select(driver.find_element_by_id("country"))
    country_dropdown.select_by_visible_text(country)
    driver.quit()


def select_state(state):
    driver = webdriver.Chrome()
    driver.get("https://example.com/profile")
    state_dropdown = Select(driver.find_element_by_id("state"))
    state_dropdown.select_by_visible_text(state)
    driver.quit()
