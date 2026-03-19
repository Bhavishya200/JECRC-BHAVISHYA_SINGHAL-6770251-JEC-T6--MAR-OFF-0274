from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()

checkboxes = driver.find_element(By.LINK_TEXT, "Checkboxes")
dragDrop = driver.find_element(By.PARTIAL_LINK_TEXT, "Drag")

list = driver.find_elements(By.TAG_NAME, "li")
print("li count:", len(list))

driver.get("https://the-internet.herokuapp.com/tables")

website_xpath = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='jdoe@hotmail.com']/following-sibling::td[2]")
delete_xpath = driver.find_element(By.XPATH,"//table[@id='table1']//td[text()='Bach']/following-sibling::td/a[text()='delete']")
second_table = driver.find_element(By.XPATH, "(//table)[2]")
parent = driver.find_element(By.XPATH, "//td[text()='$100.00']/..")

sleep(2)
driver.quit()