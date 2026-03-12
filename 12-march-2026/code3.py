from selenium import webdriver
import time

browsers = ['chrome', 'edge', 'firefox']

for b in browsers:

    if b == 'chrome':
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")

    elif b == 'edge':
        driver = webdriver.Edge()
        driver.get("https://www.bing.com")

    elif b == 'firefox':
        driver = webdriver.Firefox()
        driver.get("https://www.mozilla.org")
    print(driver.current_url)
    print(driver.title)

    time.sleep(3)
    driver.quit()