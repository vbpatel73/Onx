from selenium import webdriver as wd
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import time, random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import threading
from multiprocessing import Process
import gevent


def order(name):
    driver = wd.Chrome("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\chromedriver.exe")
    driver.implicitly_wait(3)
    threadLock.acquire()
    driver.get("https://cco-fit-uat.lifelabs.com")
    time.sleep(1)
    driver.find_elements_by_name("loginfmt")[0].send_keys(name)
    driver.find_elements_by_id("idSIButton9")[0].click()
    time.sleep(1)
    driver.find_elements_by_name("passwd")[0].send_keys("Shlok1998")
    # print(driver.get_cookies())
    driver.find_elements_by_id("idSIButton9")[0].click()
    time.sleep(1)
    driver.find_elements_by_id("idSIButton9")[0].click()
    s1 = time.perf_counter()
    # time.sleep(1)
    #print(time.ctime())
    driver.find_element_by_xpath("//*[@title='Order Queue']").click()
    print(time.ctime())

    order = driver.find_element_by_css_selector("div#requisition-grid tr:nth-child(1) > td:nth-child(3)").text
    print(order)
    s2 = time.perf_counter()
    print(round((s2 - s1), 3))
    threadLock.release()

# driver.find_element_by_id("btnCancel").click()


threads = []
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

threadLock = threading.Lock()
for i in range(50):
    usr =user[random.randint(1,9)]
    t = threading.Thread(target=order(usr))
    t.start()
    threads.append(t)
	#t.start()


"""
procs =[]
if __name__ == '__main__':
	for i in range(50):
		usr =user[random.randint(1,9)]
		proc = Process(target=order(usr))
		proc.start()
		proc.join()
"""
"""
greenlets = [ gevent.spawn(order(user[i])) for i in range(5) ]
gevent.joinall(greenlets)
"""
"""



if __name__ == "__main__":
	asyncio.run(main())
time.sleep(1000)
"""


