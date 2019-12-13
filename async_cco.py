from selenium import webdriver as wd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time , random
import asyncio


async def order(name):
    driver = wd.PhantomJS("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\phantomjs.exe")
    #driver = wd.Chrome("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\chromedriver.exe")
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
    driver.find_element_by_xpath("//*[@title='Order Queue']").click()

    await asyncio.sleep(5)

    s1 = time.perf_counter()
    #driver.find_element_by_xpath("//*[@title='Problem Queue']").click()
    #time.sleep(2)
    #driver.find_element_by_xpath('//*[@id="tabstrip"]/ul/li[3]/span[2]').click()
    #time.sleep(15)
    driver.find_element_by_id("btnNextRequisition").click()
    #driver.find_element_by_xpath('//*[@id="btnNextRequisition"]').click()
    #print(time.ctime())
    time.sleep(2)
    order = driver.find_element_by_xpath(("//*[@id='order-form']/div[1]/table/tbody/tr/td/b")).text
    s2 = time.perf_counter()
    print(round((s2 - s1), 3))
    #print(name + "|" + order)
    #driver.find_element_by_id("btnCancel").click()

async def problem_order(name):
    driver = wd.PhantomJS("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\phantomjs.exe")
    #driver = wd.Chrome("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\chromedriver.exe")
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

    await asyncio.sleep(5)

    s1 = time.perf_counter()
    driver.find_element_by_xpath("//*[@title='Problem Queue']").click()
    time.sleep(2)
    element = WebDriverWait(driver, 175).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="tabstrip"]/ul/li[3]/span[2]')))
    driver.find_element_by_xpath('//*[@id="tabstrip"]/ul/li[3]/span[2]').click()
    #time.sleep(15)
    driver.find_element_by_id("btnNextRequisition").click()
    time.sleep(2)
    order = driver.find_element_by_xpath(("//*[@id='order-form']/div[1]/table/tbody/tr/td/b")).text
    s2 = time.perf_counter()
    print(round((s2 - s1), 3))


async def search_order(name,id):
    #driver = wd.PhantomJS("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\phantomjs.exe")
    driver = wd.Chrome("C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\chromedriver.exe")
    driver.implicitly_wait (3)

    driver.get("https://cco-fit-uat.lifelabs.com")
    time.sleep(1)
    driver.maximize_window()

    driver.find_elements_by_name("loginfmt")[0].send_keys(name)#"VikashAdmin@lifelabsccofit.onmicrosoft.com")
    driver.find_elements_by_id("idSIButton9")[0].click()
    time.sleep(1)
    driver.find_elements_by_name("passwd")[0].send_keys("Shlok1998")
    #print(driver.get_cookies())
    time.sleep (2)
    driver.find_elements_by_id("idSIButton9")[0].click()
    time.sleep(2)
    driver.find_elements_by_id("idSIButton9")[0].click()
    time.sleep(3)
    driver.find_element_by_xpath("//*[@title='Search Order']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='Search']/div/div[1]/div/div[2]/div/ul/li[4]").click()
    #print("done")
    await asyncio.sleep(5)
    driver.find_element_by_id("SearchText").send_keys(id)
    time.sleep(2)
    driver.find_element_by_id('btSearch').click()
    s1 = time.perf_counter()
    element = WebDriverWait(driver, 175).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='OrderListGrid']/table/tbody/tr/td[2]/a" )))
    # order = driver.find_element_by_xpath (("//*[@id='OrderListGrid']/table/tbody/tr/td[2]/a")).text
    # print (order)
    #time.sleep(2)

    driver.find_element_by_xpath(("//*[@id='OrderListGrid']/table/tbody/tr/td[2]/a")).click()
    order = driver.find_element_by_xpath(("//*[@id='order-form']/div[1]/table/tbody/tr/td/b")).text
    #print(order)
    s2 = time.perf_counter()
    print(round((s2 - s1), 3))
    #print(name + "|" + order)
    #driver.find_element_by_id("btnCancel").click()



users = ["Vikash@lifelabsccofit.onmicrosoft.com",
         "VikashPA@lifelabsccofit.onmicrosoft.com",
         "Anubhav@lifelabsccofit.onmicrosoft.com" ,
         "AnubhavAdmin@lifelabsccofit.onmicrosoft.com" ,
         "AnubhavPA@lifelabsccofit.onmicrosoft.com" ,
         "Testuser@lifelabsccofit.onmicrosoft.com" ,
         "Mahnoosh@lifelabsccofit.onmicrosoft.com" ,
         "Nadeem@lifelabsccofit.onmicrosoft.com" ,
         "VikashAdmin@lifelabsccofit.onmicrosoft.com" ,
         "Test@lifelabsccofit.onmicrosoft.com"]

admin = [   "VikashPA@lifelabsccofit.onmicrosoft.com",
         "AnubhavAdmin@lifelabsccofit.onmicrosoft.com" ,
         "AnubhavPA@lifelabsccofit.onmicrosoft.com" ,
         "VikashAdmin@lifelabsccofit.onmicrosoft.com"    ]
ids = ['2JLBBAG6',
    'TPLBBAG6',
    '9PLBBAG6',
    'PDLBBAG6',
    'QMLBBAG6',
    'APLBBAG6',
    '3PLBBAG6',
    'NPLBBAG6',
    '8DLBBAG6',
    'RDLBBAG6',
    'RMLBBAG6',
    'LMLBBAG6',
    'N9LBBAG6',
    'HJLBBAG6',
    'SMLBBAG6',
    'TDLBBAG6',
    'VMLBBAG6',
    'BDLBBAG6',
    'XPLBBAG6',
    'VDLBBAG6',
    'PMLBBAG6',
    'UDLBBAG6',
    'CJLBBAG6',
    '9DLBBAG6',
    '7MLBBAG6',
    'NDLBBAG6',
    'GPLBBAG6',
    'DDLBBAG6',
    '4PLBBAG6',
    'FJLBBAG6',
    'GJLBBAG6',
    'DMLBBAG6',
    'JMLBBAG6',
    'CMLBBAG6',
    'KPLBBAG6',
    'EPLBBAG6',
    'FMLBBAG6',
    '2DLBBAG6',
    'QDLBBAG6',
    '7JLBBAG6',
    '59LBBAG6',
    'BJLBBAG6',
    'GDLBBAG6',
    'ZMLBBAG6',
    '6MLBBAG6',
    'QPLBBAG6',
    '5MLBBAG6',
    'YPLBBAG6',
    'SDLBBAG6',
    'HPLBBAG6',
    'KDLBBAG6',
    '99LBBAG6',
    'P9LBBAG6',
    'Q9LBBAG6',
    '2PLBBAG6',
    'YMLBBAG6',
    'SJLBBAG6',
    'TMLBBAG6',
    'GMLBBAG6',
    '5PLBBAG6',
    '4DLBBAG6',
    'JPLBBAG6',
    'CDLBBAG6',
    'MDLBBAG6',
    'MMLBBAG6',
    'KMLBBAG6',
    'EDLBBAG6',
    'HDLBBAG6',
    'SPLBBAG6',
    '8JLBBAG6',
    '6JLBBAG6',
    'D9LBBAG6',
    'PPLBBAG6',
    'NJLBBAG6',
    'YDLBBAG6',
    '8MLBBAG6',
    'JDLBBAG6',
    'UMLBBAG6',
    'LPLBBAG6',
    '2MLBBAG6',
    'AMLBBAG6',
    '4MLBBAG6',
    'UJLBBAG6',
    '29LBBAG6',
    'LDLBBAG6',
    'NMLBBAG6',
    '3JLBBAG6',
    '9MLBBAG6',
    'BMLBBAG6',
    'RPLBBAG6',
    'ZPLBBAG6',
    'QJLBBAG6',
    '5DLBBAG6',
    '7DLBBAG6',
    'XDLBBAG6',
    'VPLBBAG6',
    '3DLBBAG6',
    '3MLBBAG6',
    'ZDLBBAG6',
    'XMLBBAG6'
    ]
orders = []
search_ords =[]
problem_ords =[]
for i in range(100) :
    #usr = users[i]
    usr = users[random.randint(0,9)]
    #usr=admin[random.randint(0,3)]
    id = ids[i]
    search_ords.append(search_order(usr,id))


for i in range(50) :
    usr = users[random.randint(0,9)]
    #usr = admin[random.randint(0, 3)]
    orders.append(order(usr))

for i in range(50) :
    usr = users[random.randint(0,9)]
    #usr = admin[random.randint(0, 3)]
    problem_ords.append(problem_order(usr))


async def main():
    await asyncio.gather(*orders)
    #await asyncio.gather(*problem_ords)
    #await asyncio.gather(*search_ords)

if __name__ == "__main__":
    asyncio.run(main())
#time.sleep(1000)
