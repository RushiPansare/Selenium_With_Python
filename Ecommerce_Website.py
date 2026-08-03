from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

service=Service(r"C:\Users\rushi\Desktop\selenium\chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get(r"https://automationexercise.com/")
driver.maximize_window()
time.sleep(3)

def sign_up():
    driver.find_element(By.LINK_TEXT,"Signup / Login").click()
    driver.find_element(By.NAME,"name").send_keys("Rushi Pansare")
    driver.find_element(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/input[3]").send_keys("rushipans@gmail.com")
    driver.find_element(By.XPATH,"//*[@id='form']/div/div/div[3]/div/form/button").click()
    time.sleep(2)

def register_page():
        driver.find_element(By.ID,"id_gender1").click()
        driver.find_element(By.ID,"password").send_keys("Rushi@5360")
        days=Select(driver.find_element(By.ID,"days"))
        days.select_by_index(16)
        months=Select(driver.find_element(By.ID,"months"))
        months.select_by_index(9)
        years=Select(driver.find_element(By.ID,"years"))
        years.select_by_visible_text("2005")
        driver.find_element(By.ID,"newsletter").click()
        driver.find_element(By.ID,"first_name").send_keys("Rushi")
        driver.find_element(By.ID,"last_name").send_keys("Pansare")
        driver.find_element(By.ID,"company").send_keys("Tata Consultancy Services")
        driver.find_element(By.ID,"address1").send_keys("At post Bahul Tal khed Dist Pune")
        driver.find_element(By.ID,"address2").send_keys("Bahul Rishi's House")
        country=Select(driver.find_element(By.ID,"country"))
        country.select_by_index(0)
        driver.find_element(By.ID,"state").send_keys("Maharashtra")
        driver.find_element(By.ID,"city").send_keys("Pune")
        
        time.sleep(4)
        driver.find_element(By.ID,"zipcode").send_keys("410501")
        driver.find_element(By.ID,"mobile_number").send_keys("7498554659")
        driver.find_element(By.XPATH,"//*[@id='form']/div/div/div/div/form/button").click()
        driver.find_element(By.LINK_TEXT,"Continue").click()
        time.sleep(10)
        
def login_page():
    pass
    driver.find_element(By.LINK_TEXT,"Signup / Login").click()
    driver.find_element(By.NAME,"email").send_keys("rushipansare38@gmail.com")
    driver.find_element(By.NAME,"password").send_keys("Rushi@5360")
    driver.find_element(By.XPATH,"//*[@id='form']/div/div/div[1]/div/form/button").click()
    time.sleep(4)                                       
    driver.find_element(By.XPATH,"//*[@id='slider-carousel']/ol/li[2]").click()
    driver.find_element(By.XPATH,"//*[@id='slider-carousel']/ol/li[3]").click()
    driver.find_element(By.XPATH," //*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a").click()
    time.sleep(2)
    
def product_page():
    ele=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/img")
    action=ActionChains(driver)
    action.move_to_element(ele).click().perform()
    time.sleep(2)
    ele2=driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/img")
    action1=ActionChains(driver)
    action1.move_to_element(ele2).click().perform()
    driver.find_element(By.XPATH,"/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/ul/li/a").click()
    qty = driver.find_element(By.ID, "quantity")
    qty.clear()
    qty.send_keys("5")
    driver.find_element(By.XPATH,"/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button").click()
    time.sleep(3)
    driver.find_element(By.LINK_TEXT,"View Cart").click()
    driver.find_element(By.XPATH,"//*[@id='do_action']/div[1]/div/div/a").click()
    driver.find_element(By.NAME,"message").send_keys("The item is good")
    driver.find_element(By.LINK_TEXT,"Place Order").click()
    driver.find_element(By.NAME,"name_on_card").send_keys("Rushi Sunil Pansare")
    driver.find_element(By.NAME,"card_number").send_keys("123456789231")
    driver.find_element(By.NAME,"cvc").send_keys("123")
    driver.find_element(By.NAME,"expiry_month").send_keys("09")
    driver.find_element(By.NAME,"expiry_year").send_keys("2029")
    driver.find_element(By.XPATH,"//*[@id='submit']").click()
    driver.find_element(By.LINK_TEXT,"Download Invoice").click()
    driver.find_element(By.XPATH,"//*[@id='form']/div/div/div/div/a").click()
    time.sleep(5)

def contact_us_page():
    driver.find_element(By.LINK_TEXT,"Contact us").click()
    driver.find_element(By.NAME,"name").send_keys("Rushi Pansare")
    driver.find_element(By.NAME,"email").send_keys("rushipansare@gmail.com")
    driver.find_element(By.NAME,"subject").send_keys("about product")
    driver.find_element(By.NAME,"message").send_keys("your app is not working well ")
    driver.find_element(By.NAME,"upload_file").send_keys(r"C:\Users\rushi\Desktop\TCS_DOCUMENT\NSR_CARD.pdf")
    driver.find_element(By.NAME,"submit").click()
    driver.switch_to.alert.accept()
    driver.find_element(By.LINK_TEXT,"Home").click()
    driver.find_element(By.LINK_TEXT,"Logout").click()
    time.sleep(4)    
    
    


        
                                        
        
        


    
    
    
    
def main():
    sign_up()
    register_page()
    login_page()
    product_page()
    contact_us_page()
    
    
    
    
main()

