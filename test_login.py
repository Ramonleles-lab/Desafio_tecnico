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

#login_user
el1 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.login_email)
el1.send_keys(Elements_variable.login_email_value)
el2 = driver.find_element(by=AppiumBy.XPATH, value=Elements_variable.login_password)
el2.send_keys(Elements_variable.login_password_value)
el3 = driver.find_element(by=AppiumBy.CLASS_NAME, value=Elements_variable.Button_login)
el3.click()

#END_TEST

driver.quit()