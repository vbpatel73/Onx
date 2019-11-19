from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import os
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
	                '<p>Please find  the Test execution report with following link  <b>' + 'http://127.0.0.1:8000/' + report_time + '/</b></p>' \
                   '<p>Please send any feedback on this status report to Vikash.  </p>' \
                   '<p>Thanks </p>'



@pytest.fixture(scope="session", autouse=True, params=[
	wd.Chrome(r'C:\\Users\patelvi\\PycharmProjects\\NCE\\onx\\Drivers\\chrome_driver.exe'),
	wd.Firefox(executable_path=r'C:\\Users\\patelvi\\PycharmProjects\\NCE\\Common\\Drivers\\geckodriver.exe')
														])
def browser(request):
	driver = request.param
	driver.get('https://www.kroger.com/')
	driver.maximize_window()
	driver.implicitly_wait(30)
	time.sleep(3)
	try:
		driver.find_element_by_xpath("//button[.='Next']").click()
		time.sleep(5)
		driver.find_element_by_xpath(
			'//button[@class="kds-Button kds-Button--primaryInverse kds-Button--hasIconOnly EducationTooltip-CloseButton"]').click()

		time.sleep(2)
	except:
		pass
	yield driver
	driver.close()
	report()

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



def hover(driver, ele):
	action = ActionChains(driver)
	action.move_to_element(ele).perform()



#pytest -n=2  --alluredir=onx\report onx\test_multi.py