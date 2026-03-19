from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)


# name = driver.find_element(By.ID,'name')
# name.clear()
# name.send_keys("Temporary name") # send the particular text to particular field
# sleep(1)
# name1 = driver.find_element(By.XPATH,'//input[@placeholder="Enter EMail"]')
# name1.clear()
# name1.send_keys("temporary@gmail.com")
# sleep(5)
#
# print(name.get_attribute('placeholder'))
# print(name1.get_attribute('value'))
#
# driver.find_element(By.ID,'male').click()
# driver.find_element(By.XPATH,'//label[text()="Monday"]/preceding-sibling::input').click()
# name2 = driver.find_element(By.XPATH,'//input[@id="monday"]/following-sibling::label')
# print(name2.text)

# name3 = driver.find_elements(By.NAME,'gender')
# value = input('Enter gender: ')
# for i in name3:
#     if i.get_attribute("value") == value:
#         i.click()
#         sleep(5)
#         break
#
# sleep(5)

name3 = driver.find_elements(By.XPATH,'//div[@class="form-group"]/child::div[@class="form-check form-check-inline"]/child::input[@type="checkbox"]')
print(len(name3))

for i in name3:
    i.click()
    label = i.find_element(By.XPATH, './following-sibling::label')
    print(label.text)
    sleep(2)

for i in reversed(name3):
    i.click()
    sleep(2)

sleep(5)
driver.quit()
search=driver.find_element(By.ID,'monday')
search.click()

# search_button = driver.find_element(By.ID,'nav-search-submit-button')
# search_button.click()

sleep(5)
driver.quit()