from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get(r'C:\Users\gomti\OneDrive\Pictures\Desktop\se\20-march-2026\playlist.html')
driver.maximize_window()

song_list = driver.find_element(By.ID,'songs')
select = Select(song_list)

if select.is_multiple:
    for i in select.options:
        if 'Girl' in i.text or 'Love' in i.text:
            select.select_by_visible_text(i.text)
            print(i.text)
driver.find_element(By.XPATH, '//button[text()="Add to Playlist"]').click()
sleep(2)
driver.quit()
