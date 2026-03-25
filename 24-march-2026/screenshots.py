import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

folder = os.path.join(os.getcwd(), 'screenshots')
os.makedirs(folder, exist_ok=True)


driver = webdriver.Chrome()
driver.get('https://in.pinterest.com/')
driver.maximize_window()
action = ActionChains(driver)

sleep(3)

driver.save_screenshot(f'{folder}/full_page.png')
sleep(3)

# ele = driver.find_element(By.XPATH,'//img[@src="https://s.pinimg.com/webapp/visual-search-1px-ecc706bc.png"]')
# action.move_to_element(ele).perform()
# sleep(1)
#
# ele.screenshot(f'{folder}/cherry_red.png')
sleep(2)
