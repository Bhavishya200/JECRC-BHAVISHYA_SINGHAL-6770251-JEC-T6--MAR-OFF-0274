from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# driver.get("https://testautomationpractice.blogspot.com/")
# sleep(2)
#
# male = driver.find_element(By.ID,'male')
# male.click()
# print(male.is_displayed())
# print(male.is_enabled())
#
# check = driver.find_element(By.XPATH,'//label[text()="Monday"]/preceding-sibling::input')
# check.click()
# print(check.is_selected())
#
# name2 = driver.find_element(By.XPATH,'//input[@id="monday"]/following-sibling::label')
# print(name2.text)

driver.get("https://www.jiomart.com/?tab=smart-buys")
driver.find_element(By.ID, "btn_location_close_icon").click()
apply = driver.find_element(By.ID, 'btn_pincode_submit')
print(apply.is_enabled())

driver.find_element(By.ID, 'rel_pincode').send_keys('302033')
print(apply.is_enabled())

msg = driver.find_element(By.ID, 'delivery_pin_msg')
print(msg.text)


sleep(5)
driver.quit()