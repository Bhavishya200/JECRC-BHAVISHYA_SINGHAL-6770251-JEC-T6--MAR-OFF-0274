from inspect import isframe

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()
sleep(2)


#single iframe
# iframe = driver.find_element(By.ID, 'singleframe')
# driver.switch_to.frame(iframe)
# sleep(2)
# driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('asdfghjk')
# sleep(2)

#nested iframe

driver.find_element(By.XPATH,'//a[text()="Iframe with in an Iframe"]').click()
upper_iframe = driver.find_element(By.XPATH,'//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(upper_iframe)
inner_frame = driver.find_element(By.XPATH,'//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inner_frame)
driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('asdfghjk')
sleep(2)
driver.switch_to.parent_frame() #switch to parent frame
driver.switch_to.default_content() #switches to default page


driver.quit()