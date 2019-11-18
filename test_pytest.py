from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import allure
import openpyxl as xl
from selenium import webdriver as wd
from pywinauto.keyboard import SendKeys
from openpyxl.drawing import image
import time, shutil, datetime
import random
import requests as rq
import json
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from allure_commons.types import AttachmentType

import os

from pyutil import fileutil
from tabulate import tabulate
import win32com.client as cli

root_dir = "C:\\Users\\patelvi\\PycharmProjects\\NCE\\"


def report():
	report_time = str(datetime.datetime.today().strftime('%y%m%d_%H%M'))
	os.system("allure generate onx/report -o onx\\reports\\" + report_time)
	#os.system("allure serve onx/report")
	outlook = cli.Dispatch('outlook.application')
	mail = outlook.CreateItem(0)
	# mail.Display ()  # required to paste chart
	mail.To = 'vikash.patel@lifelabs.com'
	mail.Subject = 'Test Execution Report of  ' + str(datetime.date.today())
	mail.HTMLBody = '<p>Dear All,</p>' \
	                '<p>Please find  the Test execution report with following link  <b>' + 'http://10.144.56.84:8000/' + report_time + '/</b></p>' \
                   '<p>Please send any feedback on this status report to Vikash.  </p>' \
                   '<p>Thanks </p>'


options = wd.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
Chrome_driver = wd.Chrome(r'C:\\Users\patelvi\\PycharmProjects\\NCE\\onx\\Drivers\\chrome_driver.exe',chrome_options=options)

#FF_driver = wd.Firefox(r'C:\\Users\\patelvi\\PycharmProjects\\NCE\\onx\\Drivers\\geckodriver.exe')

@pytest.fixture(scope="session", autouse=True, params=[Chrome_driver])  # ,wd.Chrome()wd.Firefox(),wd.Ie()])
def browser(request):
	driver = request.param
	driver.get('https://www.kroger.com/')
	driver.maximize_window()
	driver.implicitly_wait(30)
	time.sleep(3)
	driver.find_element_by_xpath("//button[.='Next']").click()
	time.sleep(5)
	driver.find_element_by_xpath(
		'//button[@class="kds-Button kds-Button--primaryInverse kds-Button--hasIconOnly EducationTooltip-CloseButton"]').click()

	time.sleep(2)
	sign_in = driver.find_element_by_xpath('//div[.="Sign In"]')
	hover(driver, sign_in)
	driver.find_element_by_xpath('//a[.="Create Account"]').click()
	time.sleep(5)
	driver.find_element_by_id('AccountCreate-firstNameInput').send_keys('vv')
	driver.find_element_by_id('AccountCreate-lastNameInput').send_keys('pp')
	email = 'vv' + str(random.randint(1111, 9999)) + '@gmail.com'
	driver.find_element_by_id('AccountCreate-emailInput').send_keys(email)
	driver.find_element_by_id('AccountCreate-passwordInput').send_keys('A12345678')
	driver.find_element_by_id('loyaltyCardButton-virtualCard').click()
	card_no = random.randint(1111111111, 9999999999)
	print(card_no)
	print(email)
	driver.find_element_by_id('AccountCreate-virtualCardInput').send_keys(card_no)
	driver.find_element_by_id('AccountCreate-submitButton').click()
	time.sleep(3)
	yield driver
	driver.close()
	report()


def hover(driver, ele):
	action = ActionChains(driver)
	action.move_to_element(ele).perform()


@allure.feature("Shopping feature")
def test_shop(browser):

	time.sleep(5)
	shop = browser.find_element_by_xpath('//span["Shop"]')
	time.sleep(1)
	hover(browser, shop)
	browser.find_element_by_xpath('//a[.="Candy"]').click()
	time.sleep(2)
	browser.find_element_by_xpath('//a[.="Chocolate"]').click()
	time.sleep(2)
	browser.find_element_by_xpath('//h4[.="Brands"]').click()
	time.sleep(2)
	browser.find_element_by_xpath("//*[@id='content']//span/input").send_keys('Snickers')
	browser.find_element_by_name('Snickers').click()
	time.sleep(3)

	browser.find_element_by_xpath('(//button[.="Add to Cart"])[1]').click()
	time.sleep(2)
	browser.find_element_by_xpath('//button[.="Confirm"]').click()
	time.sleep(2)
	SendKeys("^a")
	#driver.find_element_by_xpath("(//input[@data-testid='kds-Stepper-input'])[1]").clear()
	time.sleep(5)
	browser.find_element_by_xpath("(//input[@data-testid='kds-Stepper-input'])[1]").send_keys('10')
	time.sleep(3)
	browser.find_element_by_xpath('//span[.="Cart"]').click()
	#driver.find_element_by_xpath('//*[contains(text(),"Pickup"]').click()
	item_cnt= str.replace(browser.find_element_by_xpath('//h1[@data-qa="summary-item-count"]').text,'Pickup Items: ','')
	total=browser.find_element_by_xpath('//span[@data-qa="summary-cart-section-total"]').text

	assert total == '$10.00'
	assert item_cnt == '10'
	allure.attach(browser.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)


'''

def test_create_acct(browser):

	browser.get('https://www.kroger.com/')
	browser.maximize_window()
	browser.implicitly_wait(30)
	time.sleep(3)
	browser.find_element_by_xpath("//button[.='Next']").click()
	time.sleep(5)
	browser.find_element_by_xpath('//button[@class="kds-Button kds-Button--primaryInverse kds-Button--hasIconOnly EducationTooltip-CloseButton"]').click()

	time.sleep(2)
	sign_in = browser.find_element_by_xpath('//div[.="Sign In"]')
	hover(browser, sign_in)
	browser.find_element_by_xpath('//a[.="Create Account"]').click()
	time.sleep(5)
	browser.find_element_by_id('AccountCreate-firstNameInput').send_keys('vv')
	browser.find_element_by_id('AccountCreate-lastNameInput').send_keys('pp')
	email = 'v' + str(random.randint(1111, 9999)) + '@gmail.com'
	browser.find_element_by_id('AccountCreate-emailInput').send_keys(email)
	browser.find_element_by_id('AccountCreate-passwordInput').send_keys('A12345678')
	browser.find_element_by_id('loyaltyCardButton-virtualCard').click()
	card_no = random.randint(1111111111, 9999999999)
	print(card_no)
	print(email)
	browser.find_element_by_id('AccountCreate-virtualCardInput').send_keys(card_no)
	browser.find_element_by_id('AccountCreate-submitButton').click()
	time.sleep(3)



def test_signin(browser):

	browser.get('https://www.kroger.com/')
	browser.maximize_window()
	browser.implicitly_wait(30)
	token=browser.get_cookie('XSRF-TOKEN')
	time.sleep(3)
	browser.find_element_by_xpath("//button[.='Next']").click()
	time.sleep(5)
	browser.find_element_by_xpath('//button[@class="kds-Button kds-Button--primaryInverse kds-Button--hasIconOnly EducationTooltip-CloseButton"]').click()
	time.sleep(2)

	sign_in = browser.find_element_by_xpath('(//button[@class="ListItem-Button-Dropdown text-default-800"])[5]')
	hover(browser, sign_in)
	browser.find_element_by_xpath('//a[.="Sign In"]').click()
	time.sleep(5)
	browser.find_element_by_id('SignIn-emailInput').send_keys('v7372@gmail.com')
	time.sleep(3)
	browser.find_element_by_id('SignIn-passwordInput').send_keys('A12345678')
	time.sleep(3)
	browser.find_element_by_id('SignIn-rememberMe').click()
	time.sleep(3)
	#driver.find_element_by_id('SignIn-submitButton').click()
	#SendKeys("{TAB}{TAB}{ENTER}")
	si = browser.find_element_by_id('SignIn-submitButton')
	ActionChains(browser).move_to_element(si).click().perform()
	#driver.execute_script ("arguments[0].click();" , si)


	time.sleep(5)
'''
@allure.feature("Save Coupons")
def test_save_coupon(browser):
	time.sleep(5)
	save=browser.find_element_by_xpath('//span[.="Save"]')
	hover(browser,save)
	time.sleep(2)
	browser.find_element_by_xpath('//a[.="Digital Coupons"]').click()
	time.sleep(3)
	browser.find_element_by_id('SearchableList-item-Bakery').click()
	time.sleep(3)
	browser.find_element_by_xpath('//*[contains(text(),"Added in last 7 days")]').click()
	time.sleep(3)
	browser.find_element_by_xpath('(//span[.="Load to Card"])[1]').click()
	time.sleep(2)
	acct=browser.find_element_by_xpath('(//button[@class="ListItem-Button-Dropdown text-default-800"])[5]')
	hover(browser,acct)
	browser.find_element_by_xpath('//a[.="My Coupons"]').click()
	coupon_no=browser.find_element_by_xpath('//div[@data-qa="coupons-count-format"]//span').text
	assert coupon_no =='1 Coupon'
	allure.attach(browser.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)



@allure.feature("Clinic Appointment")
def test_clinic_appt(browser):
	time.sleep(5)
	ph= browser.find_element_by_xpath('//span[.="Pharmacy & Health"]')
	hover(browser,ph)
	time.sleep(2)
	browser.find_element_by_xpath('//a[contains(text(),"The Little Clinic")]').click()
	time.sleep(3)
	browser.find_element_by_xpath('//input[@name="search.clinicFinderSearchText-typeahead-searchText"]').send_keys('44870')
	browser.find_element_by_xpath('//button[.="Find"]').click()
	time.sleep(3)
	browser.find_element_by_xpath('(//button[.="Schedule Appointment"])[1]').click()
	time.sleep(3)
	sel =browser.find_element_by_xpath('//select')
	Select(sel).select_by_visible_text('General')
	sel=browser.find_element_by_xpath('(//select)[2]')
	Select(sel).select_by_visible_text('Illness')
	time.sleep(2)
	browser.find_element_by_xpath('(//div[@class="SelectableDate"])[2]').click()
	time.sleep(2)
	browser.find_element_by_xpath('(//div[@class="AvailableSlots-GridCell"])[1]').click()
	time.sleep(2)
	browser.find_element_by_name('firstName').send_keys('vv')
	browser.find_element_by_name('lastName').send_keys('pp')
	browser.find_element_by_name('phone').send_keys('1234567890')
	browser.find_element_by_name('email').send_keys('v@v.com')
	dob = browser.find_element_by_xpath('(//select)[3]')
	Select(dob).select_by_visible_text('May')
	browser.find_element_by_name('dateOfBirth.day').send_keys('05')
	browser.find_element_by_name('dateOfBirth.year').send_keys('1977')
	time.sleep(3)
	browser.find_element_by_xpath('//button[@class="kds-Button kds-Button--favorable ScheduleButton"]').click()
	time.sleep(2)
	appt = browser.find_element_by_xpath('//p[@class="confirmationCode"]').text
	print(appt)
	allure.attach(browser.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)

def test_train_api_name():
	api_key='020b637468msh24e7cdd5044d6bep11b479jsn5be08562d785'
	by_name={"search":"Rajdhani"}  #name

	req = rq.post('https://trains.p.rapidapi.com',data=json.dumps(by_name),
	              headers={'Content-Type': 'application/json',
	                       'x-rapidapi-key': api_key}
	              )
	print(req.text)
	a =json.loads(req.text)
	for b in range(len(a)):
		train_no = a[b]["train_num"]
		train_name = a[b]["name"]
		classes=a[b]["data"]["classes"]
		print(str(train_no)+"|"+train_name+"|"+str(classes))


def test_train_api_no():
	api_key = '020b637468msh24e7cdd5044d6bep11b479jsn5be08562d785'
	by_no = {"search": '12335'}  #number of train

	req = rq.post('https://trains.p.rapidapi.com', data=json.dumps(by_no),
	              headers={'Content-Type': 'application/json',
	                       'x-rapidapi-key': api_key}
	              )
	print(req.text)
	a = json.loads(req.text)
	for b in range(len(a)):
		train_name = a[b]["name"]
		classes = a[b]["data"]["classes"]
		print(train_name + "|" + str(classes))


#test_create_acct()
#test_signin()


#test_train_api_name("Rajdhani")
#test_train_api_no('12235')


#pytest --tb=no --alluredir=onx/report onx/test_pytest.py
#python -m http.server 8000 --bind 127.0.0.1
