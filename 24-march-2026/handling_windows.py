from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
sleep(2)

# parent_handle = driver.current_window_handle
#
# driver.find_element(By.XPATH,'//a[text()="Click Here"]').click()
# sleep(2)
#
# all_windows = driver.window_handles
# print(len(all_windows))
#
# driver.switch_to.window(all_windows[1]) #you can also use -1 it give same result
#
# assert 'New' in driver.find_element(By.CLASS_NAME,'example').text
# print('done')
# driver.close()
#
# driver.switch_to.window(parent_handle)
# sleep(2)

#opening a website in new window

driver.switch_to.new_window('window')
sleep(2)
driver.get('https://in.pinterest.com/')
sleep(2)

driver.switch_to.new_window('tab')
sleep(2)
driver.get('https://in.pinterest.com/')
sleep(2)

driver.quit()