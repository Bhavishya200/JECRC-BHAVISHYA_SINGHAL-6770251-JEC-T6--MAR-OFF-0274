from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://demoqa.com/droppable')
driver.maximize_window()

wait = WebDriverWait(driver, 10)
sleep(2)
origin = wait.until(EC.presence_of_element_located((By.ID,'draggable')))
target = wait.until(EC.presence_of_element_located((By.ID,'droppable')))
sleep(2)
actions = ActionChains(driver)
actions.drag_and_drop(origin,target).perform()

sleep(3)
driver.quit()