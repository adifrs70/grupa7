import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.emag.ro/#opensearch')
get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()
# date = browser.find_element(by=By.XPATH, value='//*[@id="card_grid"]')
date = browser.find_element(by=By.CLASS_NAME, value='card-v2')
time.sleep(10)