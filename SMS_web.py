from gevent import monkey
monkey.patch_all()
import gevent
from selenium import webdriver as wd
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from lxml import html
import requests
import time
import random


def login ():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = wd.Chrome ('C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\chromedriver.exe',options=chrome_options)

    #driver = wd.PhantomJS ("C:\\Users\\patelvi.DIAGLABS\\PycharmProjects\\NCE\\Common\\Drivers\\phantomjs.exe")
    s1 = time.perf_counter ()
    driver.get ("https://192.168.152.24/static/lifelabs/dev.html")
    time.sleep(3)
    driver.find_element_by_css_selector ("div#mapWindow input").clear()
    driver.find_element_by_css_selector("div#mapWindow input").send_keys("Peterborough,ON")
    driver.find_element_by_css_selector('div#mapWindow td:nth-child(4) > button[type="button"]').click()
    time.sleep(2)

    driver.find_element_by_partial_link_text("Alexander Crt").click()
    time.sleep (2)
    driver.find_element_by_xpath("//input[@placeholder='First name']").send_keys("SMS"+str(random.randint(1,100)))
    driver.find_element_by_xpath ("//input[@placeholder='Last name']").send_keys ("SMS"+str(random.randint(1,100)))
    driver.find_element_by_xpath ("//input[@placeholder='(###) ###-####']").send_keys (random.randint(4164160000,4164169999))
    driver.find_element_by_css_selector('td > button[type="submit"]').click()
    time.sleep (2)
    driver.find_element_by_css_selector('div.icsButtonBar > table > tbody > tr > td > button[type="button"]').click()
    driver.quit()
    s2 = time.perf_counter()
    print(round((s2-s1),3))

#login()
greenlets = [ gevent.spawn(login) for i in range(3) ]
gevent.joinall(greenlets)