from appium import webdriver
from appium.options.android import UiAutomator2Options
from typing import Any, Dict  
from Environments import*
from Elements import*
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_caps = (Elements_variable.desired_cap)
appium_server_ulr = (ulr)
options = UiAutomator2Options()
options.load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server_ulr, options=options)  

sleep(10)

#START_TEST

#login_user
el1 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.login_email)
el1.send_keys(Elements_variable.login_email_value)
el2 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.login_password)
el2.send_keys(Elements_variable.login_password_value)
el3 = driver.find_element(by=AppiumBy.CLASS_NAME, value=Elements_variable.Button_login)
el3.click()

sleep(5)

#search_field_produt
el4 = driver.find_element(by=AppiumBy.CLASS_NAME, value=Elements_variable.search_field)
el4.send_keys(Elements_variable.search_field_value)
sleep(10)
el5 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.select_image)
el5.click()

#END_TEST

driver.quit