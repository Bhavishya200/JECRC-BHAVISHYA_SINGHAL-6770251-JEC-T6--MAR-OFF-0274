from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

wait = WebDriverWait(driver, 15)
sleep(3)
assert "Amazon" in driver.title
assert "amazon" in driver.current_url


search = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search.send_keys("Headphones")

search_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-search-submit-button")))
search_button.click()

price_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'₹1,000')])[2]")))
price_filter.click()

product = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(@class,'s-image-fixed-height')]/img)[1]")))

product_name = product.text
product.click()

wait.until(EC.number_of_windows_to_be(2))
driver.switch_to.window(driver.window_handles[-1])

title = wait.until(EC.presence_of_element_located((By.ID, "productTitle"))).text

price = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-price-whole']"))).text

assert product_name in title
assert price

add_to_cart = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button")))
add_to_cart.click()

cart_button = wait.until(EC.element_to_be_clickable((By.ID, "nav-cart")))
cart_button.click()

wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
assert product_name in driver.page_source

print("Test Passed Successfully")

driver.quit()