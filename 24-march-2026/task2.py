from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()

driver.find_element(By.ID, "alertButton").click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
driver.find_element(By.ID, "timerAlertButton").click()
sleep(6)
alert = driver.switch_to.alert
alert.accept()
driver.find_element(By.ID, "confirmButton").click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
result = driver.find_element(By.ID, "confirmResult").text
assert "Ok" in result
print('confirm box successfull')
driver.find_element(By.ID, "promtButton").click()
sleep(2)
alert = driver.switch_to.alert
alert.send_keys("prompt")
alert.accept()
result1 = driver.find_element(By.ID, "promptResult").text
assert "prompt" in result1
print('prompt box successfull')
sleep(2)
driver.quit()