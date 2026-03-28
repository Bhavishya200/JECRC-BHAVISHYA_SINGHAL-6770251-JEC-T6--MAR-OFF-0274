from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get("https://codepen.io/gdw96/pen/jOypoYL")
driver.maximize_window()

sleep(3)
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.clear()
password.clear()
username.send_keys("name")
password.send_keys("password")

hidden = driver.find_element(By.ID, "showPsswd")
actions = ActionChains(driver)
actions.click_and_hold(hidden).perform()
sleep(2)
actions.release().perform()

register_btn = driver.find_element(By.CLASS_NAME, "submit")
register_btn.click()

sleep(3)
driver.back()
sleep(3)

driver.switch_to.default_content()


sleep(2)
assert "Registration" in driver.page_source
print('successfull')
driver.quit()