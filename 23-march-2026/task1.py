from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.utils import keys_to_typing

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://www.royalchallengers.com/')
driver.maximize_window()

action = ActionChains(driver)
sleep(3)
img = driver.find_element(By.XPATH,'//img[@src="https://tg3.s3.ap-south-1.amazonaws.com/revents/puma-mer/152/71418301_1.jpg"]')
action.scroll_to_element(img).perform()
sleep(3)

for i in range(0,5):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(2)

sleep(3)
driver.quit()