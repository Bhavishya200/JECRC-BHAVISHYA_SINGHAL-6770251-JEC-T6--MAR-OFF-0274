from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://demoqa.com/radio-button")
driver.maximize_window()
sleep(3)
print(driver.title)
yes = driver.find_element(By.ID,"yesRadio")
yes.click()
result = driver.find_element(By.CLASS_NAME,"mt-3")
print("result :",result.text)
print("id :", yes.get_attribute("id") )
print("class :", yes.get_attribute("class"))
print("url :", driver.current_url)
sleep(3)
driver.quit()