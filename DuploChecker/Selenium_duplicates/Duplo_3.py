from selenium import webdriver


def search_products(keyword):
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    driver.implicitly_wait(10)
    search_box = driver.find_element_by_id("search-box")
    search_box.send_keys(keyword)
    search_box.submit()
    driver.quit()


def add_to_cart(product_id):
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    driver.implicitly_wait(10)
    product = driver.find_element_by_id(product_id)
    product.click()
    add_to_cart_button = driver.find_element_by_id("add-to-cart-button")
    add_to_cart_button.click()
    driver.quit()


#Duplicates it has 
# from selenium import webdriver
#
# def set_implicit_wait(driver, seconds):
#     driver.implicitly_wait(seconds)
#
# def search_products(keyword):
#     driver = webdriver.Chrome()
#
#     driver.get("https://example.com")
#
#     set_implicit_wait(driver, 10)  # Set implicit wait to 10 seconds
#
#     search_box = driver.find_element_by_id("search-box")
#     search_box.send_keys(keyword)
#     search_box.submit()
#
#     # ... Continue with search result validation and assertion
#
#     driver.quit()
#
# def add_to_cart(product_id):
#     driver = webdriver.Chrome()
#
#     driver.get("https://example.com")
#
#     set_implicit_wait(driver, 10)  # Set implicit wait to 10 seconds
#
#     product = driver.find_element_by_id(product_id)
#     product.click()
#
#     add_to_cart_button = driver.find_element_by_id("add-to-cart-button")
#     add_to_cart_button.click()
#
#     # ... Continue with cart validation and assertion
#
#     driver.quit()
