from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

driver.find_element(By.ID, "firstName").send_keys("bdgdeg")
driver.find_element(By.ID, "lastName").send_keys("gsgrgw")
driver.find_element(By.ID, "userEmail").send_keys("bdkgo3432@gmail.com")
driver.find_element(By.XPATH, "//label[text()='Male']").click()
driver.find_element(By.ID, "userNumber").send_keys("8694257856")
subject = driver.find_element(By.ID, "subjectsInput")
subject.send_keys("English")
subject.send_keys(Keys.ENTER)
driver.find_element(By.XPATH, "//label[text()='Reading']").click()
driver.find_element(By.ID, "uploadPicture").send_keys(r"C:\Users\gomti\OneDrive\Pictures\Screenshots\Screenshot 2026-02-09 160029.png")
driver.find_element(By.ID, "currentAddress").send_keys("Jaipur")
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
sleep(1)

driver.find_element(By.ID, "state").click()
driver.find_element(By.XPATH, "//div[text()='Rajasthan']").click()

driver.find_element(By.ID, "city").click()
driver.find_element(By.XPATH, "//div[text()='Jaipur']").click()

driver.find_element(By.ID, "submit").click()

sleep(5)
driver.quit()