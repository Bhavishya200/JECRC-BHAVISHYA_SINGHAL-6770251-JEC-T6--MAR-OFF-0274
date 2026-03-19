from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
# driver.refresh()
sleep(2)
driver.find_element(By.CLASS_NAME,"b3wTlE").click()
search = driver.find_element(By.NAME, "q")
search.send_keys("mobile",Keys.ENTER)

search = driver.find_element(By.NAME, "q")
print(search.get_attribute("value"))
sleep(2)

brand=driver.find_element(By.CLASS_NAME,"buvtMR")
print(brand.text)
# driver.find_element(By.CLASS_NAME,"ybaCDx").click()
brand.click()
sleep(4)
pic=driver.find_element(By.CLASS_NAME,'UCc1lI')
print(pic.get_attribute("src"))


driver.quit()
