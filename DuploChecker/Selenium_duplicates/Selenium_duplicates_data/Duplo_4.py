from selenium import webdriver


def handle_authentication_popup(username, password):
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    alert = driver.switch_to.alert
    alert.send_keys(username + "\t" + password)
    alert.accept()
    driver.quit()


def handle_confirmation_popup():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    alert = driver.switch_to.alert
    alert.accept()
    driver.quit()


# from selenium import webdriver
#
# def handle_popup():
#     alert = driver.switch_to.alert
#     alert.accept()
#
# def handle_authentication_popup(username, password):
#     driver = webdriver.Chrome()
#
#     driver.get("https://example.com")
#
#     handle_popup()
#
#     alert.send_keys(username + "\t" + password)
#
#     # ... Continue with page validation and assertion
#
#     driver.quit()
#
# def handle_confirmation_popup():
#     driver = webdriver.Chrome()
#
#     driver.get("https://example.com")
#
#     handle_popup()
#
#     # ... Continue with confirmation validation and assertion
#
#     driver.quit()
