from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
sleep(3)
print(driver.title)
username = driver.find_element(By.NAME, "username")
username.clear()
username.send_keys("Admin")
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123",Keys.ENTER)
link = driver.current_url
print(link)
if "dashboard" in link:
    print("successful login")

sleep(3)
driver.quit()