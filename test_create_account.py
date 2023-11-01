from appium import webdriver
from appium.options.android import UiAutomator2Options
from typing import Any, Dict  
from Environments import*
from Elements import*
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.common.keys import Keys

desired_caps = (Elements_variable.desired_cap)
appium_server_ulr = (ulr)
options = UiAutomator2Options()
options.load_capabilities(desired_caps)
driver = webdriver.Remote(appium_server_ulr, options=options)  

sleep(10)

#START_TEST

#create_account
el1 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.Button_create_account)
el1.click()
sleep(5)
el2 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.add_email_acconunt_)
el2.send_keys(Elements_variable.add_email_acconunt_value)
el3 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.add_password_account)
el3.send_keys(Elements_variable.add_password_account_value)
el4 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.add_password_account_repeat)
el4.send_keys(Elements_variable.add_password_account_repeat_value)
el5 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.Button_register)
el5.click()
sleep(10)

#END_TEST

driver.quit()