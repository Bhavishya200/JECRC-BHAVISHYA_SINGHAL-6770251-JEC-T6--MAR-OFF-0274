from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get("https://www.cricbuzz.com/")

id1 = driver.find_element(By.ID, "leaderboard")
print(id1)

id2 = driver.find_element(By.ID, "main-header")
print(id2)

id3 = driver.find_element(By.ID, "shosh")
print(id3)

class1 = driver.find_elements(By.CLASS_NAME, "mt-6")
print(class1)

class2 = driver.find_elements(By.CLASS_NAME, "col-span-9")
print(class2)

class3 = driver.find_elements(By.CLASS_NAME, "min-h-container")
print(class3)

tag1 = driver.find_element(By.TAG_NAME, "a")
print(tag1)

tag2 = driver.find_elements(By.TAG_NAME, "div")
print(tag2)

tag3 = driver.find_elements(By.TAG_NAME, "img")
print(tag3)


css1 = driver.find_element(By.CSS_SELECTOR,'a[href*="cricket-scorecard-archives"]')
print(css1)

css2 = driver.find_element(By.CSS_SELECTOR, ".relative.overflow-hidden")
print(css2)

css3 = driver.find_element(By.CSS_SELECTOR, ".mb-12.tb\\:mb-14.wb\\:mb-0")
print(css3)

xpath1 = driver.find_element(By.XPATH, "//div[contains(text(),'RCB to kick off')]")
print(xpath1)

xpath2 = driver.find_element(By.XPATH, "//a[contains(text(),'Live Scores')]")
print(xpath2)

xpath3 = driver.find_element(By.XPATH, "(//div[contains(@class,'mt-6')])[1]")
print(xpath3)

print("complete")

sleep(5)
driver.quit()