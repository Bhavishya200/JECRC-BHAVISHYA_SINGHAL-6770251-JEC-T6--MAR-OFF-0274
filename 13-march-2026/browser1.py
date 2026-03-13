from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opts)
driver.get("https://testautomationpractice.blogspot.com/")
sleep(1)
