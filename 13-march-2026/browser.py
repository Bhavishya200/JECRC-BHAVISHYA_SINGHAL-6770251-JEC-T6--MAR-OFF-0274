from selenium import webdriver
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
opts.add_argument("--headless") 
driver = webdriver.Chrome(options=opts)
driver.get("https://www.google.com")
sleep(5)
print('Its working fine')