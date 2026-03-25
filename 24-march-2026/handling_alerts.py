from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
sleep(2)

#simple alerts

# driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
# sleep(2)

#confirmation alert

# driver.find_element(By.XPATH,'//button[@onclick="jsConfirm()"]').click()
# sleep(2)
# alert = driver.switch_to.alert
# # alert.accept()
# alert.dismiss()
# sleep(2)

#prompt alert

# driver.find_element(By.XPATH,'//button[@onclick="jsPrompt()"]').click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.send_keys("asdfghj")
# sleep(2)
# alert.accept()
# #alert.dismiss()
# sleep(2)

#switching to alert using waits

wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH,'//button[@onclick="jsAlert()"]').click()
alerts = wait.until(EC.alert_is_present())
sleep(2)
alerts.accept()
sleep(2)

driver.quit()
