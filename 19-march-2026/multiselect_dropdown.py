from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://abc.com/")
driver.maximize_window()

# driver.implicitly_wait(1)
# ele = driver.find_element(By.XPATH,'(//a[@class="AnchorLink"]/parent::li/descendant::img)[1]')
# print(ele.get_attribute("src"))

wait = WebDriverWait(driver, 10)

loading_circle = wait.until(EC.invisibility_of_element_located((By.ID,'preloader-animated_svg__svg3')))

title_abc = driver.find_element(By.XPATH,'//span[text()="ABC SHOWS, SPECIALS & MORE"]')

assert 'SPECIALS' in title_abc.text, 'not found'
print('working fine')

driver.quit()

