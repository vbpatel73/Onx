from realbrowserlocusts import FirefoxLocust, ChromeLocust, PhantomJSLocust
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from locust import TaskSet, task
import openpyxl as xl
import time

'''
wb = xl.load_workbook('C:\\Users\\patelvi.DIAGLABS\\Desktop\\patients_CCO.xlsx')
data = wb['Sheet5']
pat = []
for x in range(1, 501):
    p = data.cell(x, 1).value
    pat.append(p)
'''
user = ["Vikash@lifelabsccofit.onmicrosoft.com",
        "VikashPA@lifelabsccofit.onmicrosoft.com",
        "Anubhav@lifelabsccofit.onmicrosoft.com",
        "AnubhavAdmin@lifelabsccofit.onmicrosoft.com",
        "AnubhavPA@lifelabsccofit.onmicrosoft.com",
        "Testuser@lifelabsccofit.onmicrosoft.com",
        "Mahnoosh@lifelabsccofit.onmicrosoft.com",
        "Nadeem@lifelabsccofit.onmicrosoft.com",
        "VikashAdmin@lifelabsccofit.onmicrosoft.com",
        "Test@lifelabsccofit.onmicrosoft.com"]


class LocustUserBehavior(TaskSet):
    name = ""
    pa = ""

    def on_start(self):

        self.client.get("https://cco-fit-uat.lifelabs.com")
        time.sleep(1)
        self.client.maximize_window()
        self.client.find_elements_by_name("loginfmt")[0].send_keys('Tester1@lifelabsccofit.onmicrosoft.com')
        self.client.find_elements_by_id("idSIButton9")[0].click()
        time.sleep(1)
        self.client.find_elements_by_name("passwd")[0].send_keys("Shlok1998")
        time.sleep(2)
        self.client.find_elements_by_id("idSIButton9")[0].click()
        time.sleep(2)
        self.client.find_elements_by_id("idSIButton9")[0].click()
        time.sleep(2)

    @task
    def order(self):

        url = "https://cco-fit-uat.lifelabs.com/Search/GetSearchOrderList?sort=&page=1&pageSize=10&group=&filter=&SearchText=1015423476&searchType=2"
        a = self.client.post(url)
        print(a.text)


class LocustUser(ChromeLocust):
    # class LocustUser(ChromeLocust):
    # class LocustUser(PhantomJSLocust):

    host = "not really used"
    timeout = 30  # in seconds in waitUntil thingies
    min_wait = 100
    max_wait = 1000
    screen_width = 1200
    screen_height = 600
    task_set = LocustUserBehavior