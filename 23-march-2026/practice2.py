from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://demoqa.com/droppable')
driver.maximize_window()

driver.find_element(By.ID,'droppableExample-tab-preventPropogation').click()

actions = ActionChains(driver)

origin = driver.find_element(By.ID,'dragBox')
target1 = driver.find_element(By.XPATH,'(//p[text()="Outer droppable"][1])')
target2 = driver.find_element(By.ID,'notGreedyInnerDropBox')

actions.drag_and_drop(origin,target1).perform()
sleep(3)
actions.drag_and_drop(origin,target2).perform()

sleep(3)
driver.quit()