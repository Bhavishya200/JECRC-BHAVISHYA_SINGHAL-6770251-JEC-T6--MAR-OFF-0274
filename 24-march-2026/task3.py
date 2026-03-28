from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()

main = driver.current_window_handle

driver.find_element(By.ID, "tabButton").click()
sleep(2)
handles = driver.window_handles
driver.switch_to.window(handles[1])
text = driver.find_element(By.ID, "sampleHeading").text
assert "This is a sample page" in text
print('new tab successfull')
driver.close()
driver.switch_to.window(main)

driver.find_element(By.ID, "windowButton").click()
sleep(2)
handles = driver.window_handles
driver.switch_to.window(handles[1])
text = driver.find_element(By.ID, "sampleHeading").text
assert "This is a sample page" in text
print('new window successfull')
driver.close()
driver.switch_to.window(main)

driver.find_element(By.ID, "messageWindowButton").click()

sleep(2)
handles = driver.window_handles
driver.switch_to.window(handles[-1])

sleep(2)


driver.close()
driver.switch_to.window(main)

driver.quit()