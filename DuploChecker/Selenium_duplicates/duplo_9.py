from selenium import webdriver

def submit_form_with_data(data):
    driver = webdriver.Chrome()

    driver.get("https://example.com")

    # ... Fill in the form fields with data

    submit_button = driver.find_element_by_id("submit-button")
    submit_button.click()

    # ... Continue with validation and assertion of error messages

    driver.quit()

def test_form_submission():
    data_set1 = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "1234567890"
    }

    submit_form_with_data(data_set1)

    # ... Additional scenarios with different data sets and expected error messages
    data_set2 = {
        "name": "",
        "email": "johndoe@example.com",
        "phone": "1234567890"
    }
    submit_form_with_data(data_set2)

    data_set3 = {
        "name": "John Doe",
        "email": "",
        "phone": "1234567890"
    }
    submit_form_with_data(data_set3)

    data_set4 = {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": ""
    }
    submit_form_with_data(data_set4)
