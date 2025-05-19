from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get('https://ya.ru')
sleep(2)

driver.get('https://google.com')
sleep(2)
driver.save_screenshot('./screen.png')
driver.back()
sleep(2)

driver.forward()

sleep(2)