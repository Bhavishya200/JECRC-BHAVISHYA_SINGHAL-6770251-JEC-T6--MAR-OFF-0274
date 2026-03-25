from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://in.pinterest.com/')
driver.maximize_window()
sleep(3)
#to the bottom of the page
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(3)
#to the origin of the page
driver.execute_script('window.scrollTo(0,0);')
sleep(3)
#using scroll by
driver.execute_script('window.scrollBy(0,500);') #scrolling down
sleep(3)
driver.execute_script('window.scrollBy(0,-200);') #scrolling up having origin at 500px
sleep(3)
#scrolling to element
ele=driver.find_element(By.XPATH,'(//div[@class="ADXRXN AsRsEE"])[3]/descendant::img')
driver.execute_script('arguments[0].scrollIntoView();',ele)
sleep(3)

#clicking
click_ele = driver.find_element(By.XPATH,'(//div[text()="Join Pinterest"])[1]')
driver.execute_script('arguments[0].click();',click_ele)
sleep(3)


driver.quit()