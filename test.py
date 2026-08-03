from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
service=Service(r"c:\Users\rushi\Desktop\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://www.google.com")

time.sleep(4)
driver.quit()