from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2)
for i in range(0,2):
    if i==0:
        driver.find_element(By.ID,'male').click()
    else:
        driver.find_element(By.ID,'female').click()
days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
for i in days:
    check=driver.find_element(By.XPATH,'//label[text()="'+i+'"]')
    check.click()


for i in reversed(days):
    check=driver.find_element(By.XPATH,'//label[text()="'+i+'"]')
    check.click()

driver.quit()