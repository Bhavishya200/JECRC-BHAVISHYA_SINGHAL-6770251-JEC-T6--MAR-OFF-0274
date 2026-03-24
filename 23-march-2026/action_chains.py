from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.utils import keys_to_typing

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# driver.get('https://the-internet.herokuapp.com/drag_and_drop')
# driver.maximize_window()
# sleep(2)
#
# action = ActionChains(driver)
#
# origin_ele = driver.find_element(By.ID,'column-a')
# target_ele = driver.find_element(By.ID,'column-b')
#
# action.drag_and_drop(origin_ele,target_ele).perform()
#
# sleep(2)
# driver.quit()

#Mouse Hover
# driver.get('https://supertails.com/')
# driver.maximize_window()
#
# action = ActionChains(driver)
#
# dog = driver.find_element(By.XPATH,'(//span[contains(text(),"Dogs")][1])')
# sleep(3)
# action.move_to_element(dog).perform()
#
# sleep(2)
# driver.quit()

#Scrolling to the element

# driver.get('https://supertails.com/')
# driver.maximize_window()
#
# action = ActionChains(driver)
# sleep(3)
# cat = driver.find_element(By.XPATH,'//div[@data-ganame="Breed 5"]')
# action.scroll_to_element(cat).perform()
# sleep(3)
# action.scroll_by_amount(0,-1500).perform()
# sleep(3)
#
#
#
# sleep(3)
# driver.quit()

#keyboard action

# driver.get('https://supertails.com/')
# driver.maximize_window()
#
# action = ActionChains(driver)
#
# action.send_keys(Keys.PAGE_DOWN).perform()
# sleep(3)
# action.send_keys(Keys.PAGE_UP).perform()
# sleep(3)
# action.key_down(Keys.CONTROL).send_keys('a').perform()
# sleep(3)
# action.key_up(Keys.CONTROL).perform()
# sleep(3)

# copying and pasting for address field

# driver.get(r'C:\Users\gomti\OneDrive\Pictures\Desktop\se\23-march-2026\address_fields.html')
# driver.maximize_window()
# actions = ActionChains(driver)
#
# present = driver.find_element(By.ID,'presentAddress')
# permanent = driver.find_element(By.ID,'permanentAddress')
# present.send_keys('JECRC COLLEGE, SITAPURA INDUSTRIAL AREA, JAIPUR')
# sleep(3)
#
# present.click()
# actions.key_down(Keys.CONTROL).send_keys('a').perform()
# sleep(3)
# actions.send_keys('c').key_up(Keys.CONTROL).perform()
# permanent.click()
# actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
# sleep(3)
# driver.quit()

#password visiblity

driver.get(r'C:\Users\gomti\OneDrive\Pictures\Desktop\se\23-march-2026\index1.html')
driver.maximize_window()
actions = ActionChains(driver)
driver.find_element(By.ID,'password').send_keys('ifwqw')
sleep(2)
show = driver.find_element(By.ID,'eyeBtn')

actions.click_and_hold(show).perform()
sleep(7)
actions.release().perform()
sleep(1)
driver.quit()



