from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from datetime import datetime
import os
from selenium.webdriver.common.keys import Keys
import json 
import time
import winsound
chrome_options = webdriver.ChromeOptions()
ti=int(input("Enter time in seconds"))

time_stamp = (datetime.now().strftime
                      (r'%d'+('-')+'%b'+('-')+'%Y'+('-')+'%H'+('.')
                       +'%M'+('-')+'%S'+'s'))
str1='C:/Users/Kaushal Barhate/Downloads/vtop/'+time_stamp
img_folder = str1
check_img_folder = os.path.isdir(img_folder)
if not check_img_folder:
    os.makedirs(img_folder)
    
txtfile=img_folder+"/old.txt" 
f=open(txtfile,"w")

def beep_sound():
    """Beep sound. frequency, duration."""
    winsound.Beep(840, 2000)

settings = {"recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}], "selectedDestinationId": "Save as PDF", "version": 2}
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings),'savefile.default_directory': img_folder}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
driver = webdriver.Chrome(r"C:\\webdrivers\\chromedriver.exe", options=chrome_options)

driver.implicitly_wait(15) 
driver.get('https://vtopcc.vit.ac.in/vtop/initialProcess')


def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        
def compare_files(a,b):
    ft=open(a,"r")
    ft1=open(b,"r")
    for x in ft:
        for y in ft1:
            if(x!=y):
                return 0
            break
    ft.close()
    ft1.close()
    


def vtop_results():
    driver.find_element_by_xpath('//*[@id="closedHTML"]/div/div/div/div[2]/div/div/a').click()
    driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/div[1]/div[1]/div[3]/div/button').click()
    
    driver.find_element_by_xpath('//*[@id="uname"]').send_keys("20BCE1099")
    driver.find_element_by_xpath('//*[@id="passwd"]').send_keys("password")
    driver.implicitly_wait(15) 
    #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="menu-toggle"]')))
    driver.find_element_by_xpath('//*[@id="menu-toggle"]').click()
    driver.find_element_by_xpath('//*[@id="accordian0"]/div[6]/div[1]/h4/a').click()
    driver.find_element_by_xpath('//*[@id="EXM0011"]').click()
    driver.find_element_by_xpath('//*[@id="semesterSubId"]').click()
   # driver.find_element_by_css_selector('.customTable-level1 tr.tableContent-level1 td')
    
    select = Select(driver.find_element_by_id('semesterSubId'))
    
    # select by value 
    select.select_by_value('CH20202117')
    
    
def vtop_results1():
    driver.find_element_by_xpath('//*[@id="semesterSubId"]').click()
    
    select = Select(driver.find_element_by_id('semesterSubId'))
    
    # select by value 
    select.select_by_value('CH20202117')
    
   
    
def vtop_tp():
    driver.find_element_by_xpath('//*[@id="semesterSubId"]').click()
    
    select = Select(driver.find_element_by_id('semesterSubId'))
    
    # select by value 
    select.select_by_value('CH2020211')
    
vtop_results()  
countdown(4)
driver.find_element_by_xpath('//*[@id="menu-toggle"]').click()     
element = driver.find_element_by_class_name("fixedTableContainer").text
f.write(element)
f.close()
def timer():
    txtfile=img_folder+"/old.txt" 
    driver.execute_script('window.print();')
    countdown(ti)
    vtop_tp()
    countdown(10)
    driver.implicitly_wait(15)
    txtfile1=img_folder+"/new.txt" 
    f1=open(txtfile1,"w")
    
    vtop_results1()
    countdown(10)
    element = driver.find_element_by_class_name("fixedTableContainer").text
    f1.write(element)
    f1.close()
    z=compare_files(txtfile,txtfile1)
    if(z==0):
        beep_sound()
        txtfile3=img_folder+"/final.txt"
        f3=open(txtfile3,"w")
        ff1=open(txtfile1,"r")
        for x in ff1:
            f3.write(x)
        ff1.close()
        f3.close()
    timer()

timer()
