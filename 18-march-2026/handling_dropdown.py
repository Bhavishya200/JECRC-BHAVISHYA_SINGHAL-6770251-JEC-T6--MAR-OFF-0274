from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# driver.get("https://www.lenskart.com/")
# driver.maximize_window()
# sleep(2)

# eye = driver.find_element(By.ID, "lrd1")
# # print(eye.text)
#
# assert 'EYE' == eye.text, 'didnt find'
# print('success')

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2)

country_dropdown = driver.find_element(By.ID, 'country')
dropdown = Select(country_dropdown)
dropdown.select_by_value('australia')
sleep(2)
dropdown.select_by_index(3)
sleep(2)
dropdown.select_by_visible_text('Japan')

sleep(4)
driver.quit()
