from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lxml import html
import requests
import time
import random
from gevent import monkey
monkey.patch_all()
import gevent


def request ( driver ):
    s = requests.Session ()
    cookies = driver.get_cookies ()
    for cookie in cookies:
        s.cookies.set (cookie['name'] , cookie['value'])
    return s

loc = ['STAYNERPSC',
    'BATHURSTSTPSC',
    'CREDITVALLEYPSC',
    'BORDENPSC',
    'SOUTHGATEPSC',
    'LAKECOWICHANPSC',
    'CMLPSC',
    'TOWERSPSC',
    'ALBERTPARKPSC',
    'MIDTOWNPSC'
    ]
Login_time =[]
appt_time = []
serve_time = []
def login ():
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")
    #driver = wd.Chrome('C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\chromedriver.exe',
                    #   options=chrome_options)
    driver = wd.PhantomJS ("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\phantomjs.exe")
    s1 = time.perf_counter ()
    l1 =random.choice(loc)
    driver.get ("http://sdwvwwpwt101:83/Training/default.aspx")
    try:
        element = WebDriverWait (driver , 1000).until (
            EC.visibility_of_element_located (
                (By.ID , "ctl00_MainContent_LoginView1_Login1_UserName"))
        )
    except TimeoutException:
        return False
    driver.find_element_by_id ('ctl00_MainContent_LoginView1_Login1_UserName').send_keys ('BATHURSTSTPSC')
    driver.find_element_by_id ('ctl00_MainContent_LoginView1_Login1_Password').send_keys ("LifeLabs1")
    driver.find_element_by_id ('ctl00_MainContent_LoginView1_Login1_LoginButton').click ()
    driver.get("http://sdwvwwpwt101:83/Training/psc/DaySheet.aspx")
    #time.sleep(30)

    try:
        element = WebDriverWait (driver , 1000).until (
            EC.visibility_of_element_located (
                (By.ID , "ctl00_MainContent_DaySheet1_RadGrid1_ctl00_ctl02_ctl00_btnAdd"))
        )
    except TimeoutException:
        return False
    s2 = time.perf_counter()
    driver.find_element_by_id("ctl00_MainContent_DaySheet1_RadGrid1_ctl00_ctl02_ctl00_btnAdd").click()
    driver.find_element_by_id ("ctl00_MainContent_DaySheet1_RadGrid1_ctl00_ctl02_ctl02_RadTextBoxFirstName").send_keys("test"+str(random.randint(10,500)))
    driver.find_element_by_id ("ctl00_MainContent_DaySheet1_RadGrid1_ctl00_ctl02_ctl02_RadTextBoxLastName").send_keys("test"+str(random.randint(10,500)))
    driver.find_element_by_id ("ctl00_MainContent_DaySheet1_RadGrid1_ctl00_ctl02_ctl02_Button1").click()

    driver.get ("http://sdwvwwpwt101:83/Training/psc/DaySheet.aspx")
    s3 = time.perf_counter ()
    t =driver.find_elements_by_xpath ("//input[@value='Served']")
    Login_time.append(str(round((s2-s1),3)))
    appt_time.append(str (round((s3-s2),3)))

def serve_appt():
    #driver = wd.PhantomJS("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\phantomjs.exe")
    driver = wd.Chrome('C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\chromedriver.exe')
    driver.implicitly_wait(5)
    driver.get("http://sdwvwwpwt101:83/Training/default.aspx")
    driver.find_element_by_id('ctl00_MainContent_LoginView1_Login1_UserName').send_keys('BATHURSTSTPSC')
    driver.find_element_by_id('ctl00_MainContent_LoginView1_Login1_Password').send_keys("LifeLabs1")
    driver.find_element_by_id('ctl00_MainContent_LoginView1_Login1_LoginButton').click()
    driver.get("http://sdwvwwpwt101:83/Training/psc/DaySheet.aspx")
    time.sleep(3)
    for i in range(468):
        s1= time.perf_counter()
        b = driver.find_element_by_css_selector("span#ctl00_MainContent_DaySheet1_CurWait").text
        #print(b)
        driver.find_element_by_xpath('//*[@id="ctl00_MainContent_DaySheet1_RadGrid1_ctl00_ctl04_btServed"]').click()
        c =driver.find_element_by_css_selector("span#ctl00_MainContent_DaySheet1_CurWait").text
        #print(c)
        while b == c :
            time.sleep(0.25)
            c = driver.find_element_by_css_selector("span#ctl00_MainContent_DaySheet1_CurWait").text
        s2 = time.perf_counter()
        serve_time.append(round((s2-s1),3))

#greenlets = [ gevent.spawn(login) for i in range(300) ]
greenlets = [ gevent.spawn(serve_appt) for i in range(1) ]
gevent.joinall(greenlets)
print(Login_time )
print (appt_time)
print(serve_time)
gevent.killall(greenlets)