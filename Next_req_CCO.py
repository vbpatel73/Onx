
from selenium import webdriver as wd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions

#from seleniumrequests import Chrome
import time , random
import asyncio
#from bs4 import BeautifulSoup
pro = ['10.144.56.84:1234','10.144.56.36:1234','10.144.56.47:1234']

async def next_req(name):
    options = ChromeOptions()
    options.add_argument('--proxy-server='+random.choice(pro))
    #driver = wd.PhantomJS("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\phantomjs.exe")
    driver = wd.Chrome("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\chromedriver.exe",options=options)
    #driver =Chrome("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\chromedriver.exe")
    driver.implicitly_wait (3)

    driver.get("https://cco-fit-uat.lifelabs.com")
    time.sleep(1)
    driver.maximize_window()

    driver.find_elements_by_name("loginfmt")[0].send_keys(name)#"VikashAdmin@lifelabsccofit.onmicrosoft.com")
    driver.find_elements_by_id("idSIButton9")[0].click()
    time.sleep(3)
    driver.find_elements_by_name("passwd")[0].send_keys("Shlok1998")
    #print(driver.get_cookies())
    time.sleep (3)
    driver.find_elements_by_id("idSIButton9")[0].click()
    time.sleep(3)
    driver.find_elements_by_id("idSIButton9")[0].click()
    time.sleep(3)
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    driver.get("https://cco-fit-uat.lifelabs.com/name.html")
    print(driver.find_element_by_xpath("/html/body/h1").text)
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')


    await asyncio.sleep(1)
    driver.find_element_by_id("btnNextRequisition").click()
    time.sleep(2)
    #driver.get('https://cco-fit-uat.lifelabs.com/Order/EditRequisition')
    #res =driver.request('GET','https://cco-fit-uat.lifelabs.com/Order/EditRequisition')
    #a = BeautifulSoup(res.text)
    #order=a.find('b',id='order-form')
    driver._switch_to.window(driver.window_handles[1])
    driver.close()
    driver._switch_to.window(driver.window_handles[0])

    order = driver.find_element_by_xpath(("//*[@id='order-form']/div[1]/table/tbody/tr/td/b")).text
    #print(order)
    #order = driver.find_element_by_xpath(("//*[@id='order-form']/div[1]/table/tbody/tr/td/b")).text
    print(name + "|" + order +"|" + time.asctime())

    #driver.find_element_by_id("btnCancel").click()


users = ['Tester1@lifelabsccofit.onmicrosoft.com',
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
        'Tester40@lifelabsccofit.onmicrosoft.com',
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
         ]

ord=[]
for i in range(48):
    usr = users[i]
    ord.append(next_req(usr))


async def main():
    await asyncio.gather(*ord)
    #await asyncio.gather(*problem_ords)
    #await asyncio.gather(*search_ords)

if __name__ == "__main__":
    asyncio.run(main())
#time.sleep(1000)
