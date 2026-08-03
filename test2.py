from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
import time

service=Service(r"C:\Users\rushi\Desktop\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://www.google.com")
    

def invoke_chrome():
    driver.maximize_window()
    print(driver.title)
    time.sleep(5)
    driver.minimize_window()
    driver.quit()
    

def main():
    invoke_chrome()
    
    
main()