from selenium import webdriver

def test_link(link_url):
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    link = driver.find_element_by_link_text(link_url)
    link.click()
    driver.quit()

def test_multiple_links():
    test_link("Link 1")
    test_link("Link 2")
    test_link("Link 3")
    test_link("Link 4")
    test_link("Link 5")



# __________________________________________
#
# from selenium import webdriver
# 
# def test_link(link_url):
#     driver = webdriver.Chrome()
#
#     driver.get("https://example.com")
#
#     link = driver.find_element_by_link_text(link_url)
#     link.click()
#
#     # ... Continue with link validation and assertion
#
#     driver.quit()
#
# def test_multiple_links():
#     links_to_test = [
#         "Link 1",
#         "Link 2",
#         "Link 3",
#         "Link 4",
#         "Link 5"
#     ]
#
#     for link_url in links_to_test:
#         test_link(link_url)
