from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver = webdriver.Chrome(options=opts)
driver.get("https://www.amazon.in/")

driver.implicitly_wait(10)

first = driver.find_element(By.CSS_SELECTOR,'#twotabsearchtextbox')
print(first)

second = driver.find_element(By.CSS_SELECTOR,'a[id="nav-logo-sprites"]')
print(second)

third = driver.find_element(By.CSS_SELECTOR,'a[id="nav-cart"]')
print(third)

fourth = driver.find_element(By.CSS_SELECTOR, "#nav-tools .nav-div a")
print(fourth)

fifth = driver.find_elements(By.CSS_SELECTOR, "#nav-xshop .nav-div a")
print(len(fifth))

print('complete')
driver.quit()