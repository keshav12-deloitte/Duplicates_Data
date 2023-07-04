from selenium import webdriver


def capture_screenshot1():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    driver.save_screenshot("screenshot1.png")
    driver.quit()


def capture_screenshot2():
    driver = webdriver.Chrome()
    driver.get("https://example.com")
    driver.save_screenshot("screenshot2.png")
    driver.quit()



