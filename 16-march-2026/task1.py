from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)


driver.get("https://www.amazon.in/")
sleep(2)
search=driver.find_element(By.ID,'twotabsearchtextbox')
search.clear()
search.send_keys('bottle',Keys.ENTER)
# search_button = driver.find_element(By.ID,'nav-search-submit-button')
# search_button.click()

sleep(5)
driver.quit()