from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # we import this to use static dropdown automation
import time


service=Service(r"C:\Users\rushi\Desktop\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://practice.expandtesting.com/dropdown")
driver.maximize_window()
time.sleep(2)

def drop_down():
    drop=Select(driver.find_element(By.ID,"dropdown"))
    drop.select_by_value('1')
    time.sleep(2)
    d2=Select(driver.find_element(By.ID,"elementsPerPageSelect"))
    d2.select_by_value('100')
    time.sleep(2)
    d3=Select(driver.find_element(By.ID,"country"))
    d3.select_by_visible_text("India")
    time.sleep(2)





drop_down()























































