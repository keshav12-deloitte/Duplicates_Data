from selenium import webdriver

def navigate_to_page(page_url):
    driver = webdriver.Chrome()

    driver.get("https://example.com")

    nav_link = driver.find_element_by_link_text(page_url)
    nav_link.click()

    # ... Continue with navigation validation and assertion

    driver.quit()

def test_navigation_scenarios():
    navigate_to_page("About Us")

    # ... Additional navigation scenarios with different page URLs
    navigate_to_page("Contact")
    navigate_to_page("Products")
    navigate_to_page("Services")
    navigate_to_page("FAQ")


# ----------------------
# from selenium import webdriver
#
# def navigate_to_page(page_url):
#     driver = webdriver.Chrome()
#
#     driver.get("https://example.com")
#
#     nav_link = driver.find_element_by_link_text(page_url)
#     nav_link.click()
#
#     # ... Continue with navigation validation and assertion
#
#     driver.quit()
#
# def test_navigation_scenarios():
#     page_urls = [
#         "About Us",
#         "Contact",
#         "Products",
#         "Services",
#         "FAQ"
#     ]
#
#     for page_url in page_urls:
#         navigate_to_page(page_url)
