from selenium import webdriver as wd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lxml import html
import requests as rq
# import grequests
from locust import HttpLocust, TaskSet, task, seq_task
import locust.clients  as lc
from locust.clients import HttpSession
import random, time

'''
def request ( driver ):
    s = rq.session()
    cookies = driver.get_cookies ()
    for cookie in cookies:
#        s.cookies.set (cookie['name'] , cookie['value'])
    return s
'''
user = [#"Vikash@lifelabsccofit.onmicrosoft.com",
        #"VikashPA@lifelabsccofit.onmicrosoft.com",
        #"Anubhav@lifelabsccofit.onmicrosoft.com",
        #"AnubhavAdmin@lifelabsccofit.onmicrosoft.com",
        #"AnubhavPA@lifelabsccofit.onmicrosoft.com",
        #"Testuser@lifelabsccofit.onmicrosoft.com",
        #"Mahnoosh@lifelabsccofit.onmicrosoft.com",
        #"Nadeem@lifelabsccofit.onmicrosoft.com",
        #"VikashAdmin@lifelabsccofit.onmicrosoft.com",
        #"Test@lifelabsccofit.onmicrosoft.com",
        'Tester1@lifelabsccofit.onmicrosoft.com',
        'Tester2@lifelabsccofit.onmicrosoft.com',
        'Tester3@lifelabsccofit.onmicrosoft.com',
        'Tester4@lifelabsccofit.onmicrosoft.com',
        'Tester5@lifelabsccofit.onmicrosoft.com',
        'Tester6@lifelabsccofit.onmicrosoft.com',
        'Tester7@lifelabsccofit.onmicrosoft.com',
        'Tester8@lifelabsccofit.onmicrosoft.com',
        'Tester9@lifelabsccofit.onmicrosoft.com',
        'Tester10@lifelabsccofit.onmicrosoft.com',
        'Tester11@lifelabsccofit.onmicrosoft.com',
        'Tester12@lifelabsccofit.onmicrosoft.com',
        'Tester13@lifelabsccofit.onmicrosoft.com',
        'Tester14@lifelabsccofit.onmicrosoft.com',
        'Tester15@lifelabsccofit.onmicrosoft.com',
        'Tester16@lifelabsccofit.onmicrosoft.com',
        'Tester17@lifelabsccofit.onmicrosoft.com',
        'Tester18@lifelabsccofit.onmicrosoft.com',
        'Tester19@lifelabsccofit.onmicrosoft.com',
        'Tester20@lifelabsccofit.onmicrosoft.com',
        'Tester21@lifelabsccofit.onmicrosoft.com',
        'Tester22@lifelabsccofit.onmicrosoft.com',
        'Tester23@lifelabsccofit.onmicrosoft.com',
        'Tester24@lifelabsccofit.onmicrosoft.com',
        'Tester25@lifelabsccofit.onmicrosoft.com',
        'Tester26@lifelabsccofit.onmicrosoft.com',
        'Tester27@lifelabsccofit.onmicrosoft.com',
        'Tester28@lifelabsccofit.onmicrosoft.com',
        'Tester29@lifelabsccofit.onmicrosoft.com',
        'Tester30@lifelabsccofit.onmicrosoft.com',
        'Tester31@lifelabsccofit.onmicrosoft.com',
        'Tester32@lifelabsccofit.onmicrosoft.com',
        'Tester33@lifelabsccofit.onmicrosoft.com',
        'Tester34@lifelabsccofit.onmicrosoft.com',
        'Tester35@lifelabsccofit.onmicrosoft.com',
        'Tester36@lifelabsccofit.onmicrosoft.com',
        'Tester37@lifelabsccofit.onmicrosoft.com',
        'Tester38@lifelabsccofit.onmicrosoft.com',
        'Tester39@lifelabsccofit.onmicrosoft.com',
        'Tester40@lifelabsccofit.onmicrosoft.com']


class MyTaskSet(TaskSet):
    def order(self):
        #name = user[random.randint(39)]
        self.driver = wd.Chrome("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\chromedriver.exe")
        #driver = wd.PhantomJS ("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\phantomjs.exe")
        self.driver.implicitly_wait(30)
        self.driver.get("https://cco-fit-uat.lifelabs.com")
        time.sleep(1)
        self.driver.maximize_window()

        self.driver.find_elements_by_name("loginfmt")[0].send_keys('Tester1@lifelabsccofit.onmicrosoft.com')#(name)  # "VikashAdmin@lifelabsccofit.onmicrosoft.com")
        self.driver.find_elements_by_id("idSIButton9")[0].click()
        time.sleep(1)
        self.driver.find_elements_by_name("passwd")[0].send_keys("Shlok1998")
        # print(driver.get_cookies())
        time.sleep(2)
        self.driver.find_elements_by_id("idSIButton9")[0].click()
        time.sleep(2)
        self.driver.find_elements_by_id("idSIButton9")[0].click()

        @task
        def search_ord(self):
            url="https://cco-fit-uat.lifelabs.com/Search/GetSearchOrderList?sort=&page=1&pageSize=10&group=&filter=&SearchText=1015423476&searchType=2"
            a =self.client.post(url)
            print(a.text)


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 3000
    max_wait = 5000
    host = "http://localhost:8089"

# locust -f C:\Users\patelvi\PycharmProjects\NCE\CCO_Locust.py
