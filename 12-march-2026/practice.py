#To open Chrome browser
from selenium import webdriver
from time import sleep

# driver = webdriver.Edge()
# sleep(5)
# driver = webdriver.Chrome()
# driver.get("https://google.com")
# driver.maximize_window()
# sleep(5)
# driver.minimize_window()
# sleep(7)

# driver = webdriver.Edge()
# driver.get("https://google.com")
# driver.maximize_window()
# sleep(5)
# driver.back()
# sleep(5)
# driver.forward()
# sleep(5)
# driver.refresh()
# sleep(5)
# driver.minimize_window()
# sleep(7)
# driver.quit()
# sleep(5)

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://google.com")
driver.maximize_window()

# driver.close()
# driver.quit()
print(driver.current_url)
print(driver.title)