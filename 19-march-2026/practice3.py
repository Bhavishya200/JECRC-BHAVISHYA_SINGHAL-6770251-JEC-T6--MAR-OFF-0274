from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

driver.get("https://www.amazon.in/")
driver.maximize_window()
search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.send_keys("laptop")

suggestions = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.s-suggestion")))
suggestions[3].click()

wait.until(EC.element_to_be_clickable((By.ID, "a-autoid-0-announce"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "s-result-sort-select_4"))).click()

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "a-icon.a-icon-checkbox"))).click()

wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']")))

name = driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result']//h2").text
price = driver.find_element(By.XPATH, "//div[@data-component-type='s-search-result']//span[@class='a-price']").text

print("Name:", name)
print("Price:", price)

driver.quit()