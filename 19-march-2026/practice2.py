from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://qavbox.github.io/demo/signup/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

first = wait.until(EC.presence_of_element_located((By.ID, 'username')))
first.send_keys('vhjv')
email = wait.until(EC.presence_of_element_located((By.ID, 'email')))
email.send_keys('vhbnbj123@gmail.com')
tel = wait.until(EC.presence_of_element_located((By.ID, 'tel')))
tel.send_keys('4882548635')
upload = wait.until(EC.presence_of_element_located((By.NAME, 'datafile')))
upload.send_keys(r"C:\Users\gomti\OneDrive\Pictures\Screenshots\Screenshot 2026-02-28 132654.png")

gender = wait.until(EC.presence_of_element_located((By.NAME,'sgender')))
drop = Select(gender)
drop.select_by_value('male')

radio = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@value="one"]')))
radio.click()
checkbox = wait.until(EC.presence_of_element_located((By.XPATH,'//input[@value="automationtesting"]')))
checkbox.click()

tools = wait.until(EC.presence_of_element_located((By.ID, 'tools')))
down = Select(tools)
down.select_by_value('selenium')
down.select_by_index(3)

submit = wait.until(EC.presence_of_element_located((By.ID,'submit')))
submit.click()

sleep(2)
driver.quit()