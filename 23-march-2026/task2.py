from idlelib.mainmenu import menudefs

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.myntra.com/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

action = ActionChains(driver)
sleep(3)
men = wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@data-reactid="20"]')))
action.move_to_element(men).perform()
footwear = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[@data-reactid="92"]')))
footwear.click()
sleep(3)
action.scroll_by_amount(0,2000).perform()
sleep(3)
driver.quit()

