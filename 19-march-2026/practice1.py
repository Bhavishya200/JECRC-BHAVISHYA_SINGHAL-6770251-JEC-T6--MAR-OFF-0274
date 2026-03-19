from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://abc.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 5)
ele = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@id='hero-items']//div[contains(@class,'tile--hero')]//img[@data-mptype='image']")))


print(ele)
for img in ele:
    print(img.get_attribute("src"))

driver.quit()