from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service=Service(r"C:\Users\rushi\Desktop\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(2)c

def start_browser():
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.ID,"firstName").send_keys("Rushi")
    driver.find_element(By.ID,"lastName").send_keys("Pansare")
    driver.find_element(By.ID,"userEmail").send_keys("rushipansare@gmail.com")
    driver.find_element(By.ID,"gender-radio-1").click()
    
    
def basic_details():
    driver.find_element(By.ID,"userNumber").send_keys("7498554659")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    driver.find_element(By.ID,"currentAddress").send_keys("At post Bahul Tal khed ")
    time.sleep(3)
    driver.find_element(By.CLASS_NAME,"css-13cymwt-control").click()
    
    
def part_3():
    driver.find_element(By.ID,"subjectsInput").send_keys("Testing")
    time.sleep(2)    
    driver.find_element(By.ID,"uploadPicture").send_keys(r"C:\Users\rushi\Desktop\TCS_DOCUMENT\Medical_Certificate_Rushi.pdf")
    driver.find_element(By.ID,"submit").click()
    time.sleep(4)
    

    
start_browser()
basic_details()
part_3()
