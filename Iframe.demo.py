from selenium import webdriver
from selenium.webdriver.chrome.service  import Service
from selenium.webdriver.common.by import By
import time 

service=Service(r"C:\Users\rushi\Desktop\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
time.sleep(3)

def iframe():
    IF1=driver.find_element(By.ID,"mce_0_ifr")
    driver.switch_to.frame(IF1)   # inside frame() is id of locator
    time.sleep(2)
    print(driver.find_element(By.ID,"tinymce").text)


iframe()
