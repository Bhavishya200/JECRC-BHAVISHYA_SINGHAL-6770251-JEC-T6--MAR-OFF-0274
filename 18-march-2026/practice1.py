from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.lenskart.com/')
driver.maximize_window()
driver.find_element(By.ID, 'autocomplete-0-input').send_keys('sunglasses', Keys.ENTER)
sleep(3)
price_dropdown = driver.find_element(By.ID, 'sortByDropdown')
dropdown = Select(price_dropdown)
dropdown.select_by_value('created')

first = driver.find_element(By.XPATH, '//div[@class="sc-23b7d3eb-6 hYdmOJ"]/child::p')
print(first.text)

sleep(3)
driver.quit()
