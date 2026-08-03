

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

service =Service(r"C:\Users\rushi\Desktop\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=service)
# driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
driver.get("https://techbeamers.com/selenium-practice-test-page/")
driver.maximize_window()
time.sleep(4)

def task1():
    pass
    # driver.find_element(By.ID,"name").send_keys("Rushi Pansare")
    # driver.find_element(By.ID,"email").send_keys("rushipansare38@gamil.com")
    # driver.find_element(By.ID,"phone").send_keys("7498554659")
    # driver.find_element(By.ID,"textarea").send_keys("At post bahul Tal khed Dist Pune 410501")
    # time.sleep(4)
   
def task2():
    pass
    # driver.find_element(By.ID,"male").click()
    # driver.find_element(By.ID,"sunday").click()
    # drop=driver.find_element(By.ID,"country").click()
    # drop.select_by_value("germany")
    # drop1=driver.find_element(By.ID,"colors").click()
    # drop1.select_by_value("blue")
    # drop2=driver.find_element(By.ID,"animals").click()
    # drop2.select_by_value("cheetah")
    #time.sleep()
  
def date_pic():
    pass
    #  driver.find_element(By.ID,"datepicker").send_keys("13/03/2003").keys.ENTER
    # # driver.find_element(By.ID,"datepicker").send_keys("06/09/2005",Keys.ENTER)
    # # time.sleep(2)
    #   driver.find_element(By.ID,"start-date").click()
    #   driver.find_element(By.ID,"start-date").send_keys("27/01/2004")
    #   driver.find_element(By.ID,"End Date").click()
  
    # driver.find_element(By.ID,"txtDate").click()
    # time.sleep(1)
    # driver.find_element(By.LINK_TEXT,"16").click()
    # time.sleep(2)
    # time.sleep(5)
    # driver.find_element(By.ID,"start-date").send_keys("15-09-2005")
    # driver.find_element(By.ID,"end-date").send_keys("25-07-2026")
    # time.sleep(3)
    # driver.find_elements(By.CLASS_NAME,"submit-btn")[0].click()
    # time.sleep(4)

    
def file_upload():
    pass
    # driver.find_element(By.ID,"singleFileInput").send_keys(r"C:\Users\rushi\Downloads\Final_Result(6th Sem).pdf")
    # driver.find_element(By.XPATH,"//button[@type='submit']").click()
    # driver.find_element(By.ID,"multipleFilesInput").send_keys(r"C:\Users\rushi\Downloads\om_PCB_result.pdf")
    # driver.find_element(By.XPATH,"//button[@type='submit']").click()
    # time.sleep(5)

def table():
    pass
    # driver.find_element(By.LINK_TEXT,"1").click()
    # time.sleep(4)
    # driver.find_element(By.LINK_TEXT,"2").click()
    # time.sleep(4)
    # driver.find_element(By.LINK_TEXT,"3").click()
    # time.sleep(4)
    # driver.find_element(By.LINK_TEXT,"4").click()
    # time.sleep(4)
    
def alert():
    driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("alert",Keys.ENTER)
    time.sleep(6)
    # driver.find_element(By.NAME,"start").click()
    # time.sleep(5)
    # driver.find_element(By.ID,"alertBtn").click()
    # time.sleep(2)
    # a=driver.switch_to.alert
    # a.accept()
    # time.sleep(4)
    # driver.find_element(By.ID,"confirmBtn").click()
    # time.sleep(2)
    # a=driver.switch_to.alert
    # a.accept()
    # driver.find_element(By.ID,"promptBtn").click()
    # time.sleep(2)
    # a=driver.switch_to.alert
    # a.send_keys("Rushi Pansare")
    # a.accept()
    # time.sleep(4)
    
def mouse_hover():
    pass
    # to_move=driver.find_element(By.CLASS_NAME,"dropbtn")    # Mouse Hover
    # ac=ActionChains(driver)
    # ac.move_to_element(to_move).perform()
    # time.sleep(3)
    
    # source=driver.find_element(By.ID,"draggable")    # Drag and drop
    # destination=driver.find_element(By.ID,"droppable")
    # action=ActionChains(driver)
    # action.drag_and_drop(source,destination).perform()
    # time.sleep(4)
    
    
def tab_switching():
    driver.find_element(By.LINK_TEXT,"Introduction to Machine Learning with Statistics | Machine Learning |TutorialsPoint").click()
    time.sleep(2)
    count=driver.window_handles
    driver.switch_to.window(count[-1])
    time.sleep(3)
    print(driver.find_element(By.ID,"video-title-container").text)
    
    
    
def task3():
    pass
    # drop=driver.find_element(By.ID,"dropdown").click()
    # time.sleep(5)
    # driver.find_element(By.ID,"comboBox").send_keys("Item 1",Keys.ENTER)
    # time.sleep(4)
    
def main():
    # alert()
    tab_switching()
    
    
    
    
main()



