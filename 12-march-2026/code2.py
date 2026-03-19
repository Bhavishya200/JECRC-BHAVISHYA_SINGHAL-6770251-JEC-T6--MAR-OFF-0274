from selenium import webdriver
import time

while True:
    # Chrome
    chrome = webdriver.Chrome()
    chrome.get("https://www.google.com")
    time.sleep(3)
    chrome.quit()

    # Edge
    edge = webdriver.Edge()
    edge.get("https://www.edge.com")
    time.sleep(3)
    edge.quit()

    break