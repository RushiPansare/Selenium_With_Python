from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj=Service(r"C:\Users\rushi\Desktop\selenium\chromedriver.exe")
driver=webdriver.Chrome()
driver.get("https://qavalidation.com/demo-form/")

def test_form():
    driver.maximize_window()
    time.sleep(4)
    driver.find_element(By.NAME,"g4072-fullname").send_keys("Rushi Pansare")
    driver.find_element(By.NAME,"g4072-email").send_keys("rushipansare38@gmail.com")
    driver.find_element(By.ID,"g4072-phonenumber").send_keys("7498554659")
    driver.find_element(By.ID,"g4072-gender").click()
    time.sleep(6)


test_form()