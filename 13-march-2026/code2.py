from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opts)
driver.get("https://the-internet.herokuapp.com/login")

first = driver.find_element(By.XPATH,'//input[@name="username"]')
print(first)

second = driver.find_element(By.XPATH,'//input[@id="password"]')
print(second)

third = driver.find_element(By.XPATH,'//button[@type="submit"]')
print(third)

fourth = driver.find_element(By.XPATH,'//a[text()="Elemental Selenium"]')
print(fourth)

fifth= driver.find_element(By.XPATH,'//h2[contains(text(),"Login Page")]')
print(fifth)

print("completed")

driver.quit()