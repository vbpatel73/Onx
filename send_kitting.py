from selenium import webdriver as wd
import openpyxl as xl
import time
import asyncio
import requests as rq
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

wb = xl.load_workbook('C:\\Users\\patelvi\\Desktop\\CCO_patients_30_8.xlsx')
data = wb['Sheet1']
pat = []
for x in range(4,40):
    p = data.cell(x, 1).value
    pat.append(p)
print(pat)

user = [#"VikashPA@lifelabsccofit.onmicrosoft.com",
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


async def order(name, pat):
    driver = wd.Chrome("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\chromedriver.exe")
    driver.implicitly_wait(10)

    driver.get("https://cco-fit-uat.lifelabs.com")
    time.sleep(1)
    driver.maximize_window()
    driver.find_elements_by_name("loginfmt")[0].send_keys(name)  # "VikashAdmin@lifelabsccofit.onmicrosoft.com")
    driver.find_elements_by_id("idSIButton9")[0].click()
    time.sleep(2)
    driver.find_elements_by_name("passwd")[0].send_keys("Shlok1998")
    time.sleep(2)
    driver.find_elements_by_id("idSIButton9")[0].click()
    time.sleep(3)
    driver.find_elements_by_id("idSIButton9")[0].click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@title='Order Queue']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@title='Next Requisition']").click()
    time.sleep(2)
    #order = driver.find_element_by_xpath(("//*[@id='order-form']/div[1]/table/tbody/tr/td/b")).text
    #print(name)
    #print(order)
    #print(pat)
    driver._switch_to.window(driver.window_handles[1])
    driver.close()
    driver._switch_to.window(driver.window_handles[0])
    driver.find_element_by_id('Order_OhipBillNumber').send_keys("131313" + Keys.TAB)
    time.sleep(2)
    driver.find_element_by_id('Order_PatientOhipNumber').send_keys(str(pat) + Keys.TAB + Keys.TAB)
    time.sleep(7)
    '''
    if driver.find_element_by_id('btSelectAddress').is_displayed():
        driver.find_element_by_id('btSelectAddress').click()

    if driver.find_element_by_id('HCNPopup_wnd_title').is_displayed():
        driver.find_element_by_xpath('/html/body/div[10]/div[1]/div').click()
        time.sleep(2)
        driver.find_element_by_id('btnSaveProblemQueue').click()
    '''

    await asyncio.sleep(5)
    a = driver.find_element_by_id('btnSaveKitting')
    actionChains = ActionChains(driver)
    actionChains.move_to_element(a).perform()
    actionChains.double_click(a).perform()
    #a.click()
    '''
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[7]/div[3]/button').click()
   
    actionChains = ActionChains(driver)
    actionChains.move_to_element(a).perform()
    actionChains.double_click(a).perform()
    #time.sleep (3)
    #driver.find4_element_by_xpath('/html/body/div[7]/div[3]/button').click()
    #driver.quit()
    '''


o = []
for i in range(35):
    u = user[i]
    pa = pat[i]
    o.append(order(u, pa))


async def main():
    # await asyncio.gather(*s)
    await asyncio.gather(*o)


if __name__ == "__main__":
    asyncio.run(main())
#time.sleep(1000)
