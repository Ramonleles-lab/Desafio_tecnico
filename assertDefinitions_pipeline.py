from appium import webdriver
from selenium import webdriver as selenium_webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Any, Dict  
from Environments import*
from Elements import*
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver.common.keys import Keys
import pytest

fail_message = "fail_message"
pass_message = "This test has passed"
type = ""
element = ""
value = ""

def pauseBetweenActions():
        time.sleep(1)
        driver.implicitly_wait(60)

# environments
@pytest.fixture
def environment_app():
        desired_caps = Elements_variable.desired_cap
        appium_server_url = ulr
        options = UiAutomator2Options()
        options.load_capabilities(desired_caps)
        global driver
        driver= webdriver.Remote(appium_server_url, options=options)

        pauseBetweenActions() # ensure_all_first_requests_end

def click_by_xpath(element):

        pauseBetweenActions()

        elementObject = driver.find_element(AppiumBy.XPATH, element)
        
        if elementObject:
                elementObject.click()
        else:
                print(fail_message)
                assert(False)

def click(element):
       
        pauseBetweenActions()
        elementObject = driver.find_element(AppiumBy.CSS_SELECTOR, element)
        
        if elementObject:
                elementObject.click()
        else:
                print(fail_message)
                assert(False)

def send_keys(element, value):

        pauseBetweenActions()

        elementObject = driver.find_element(AppiumBy.XPATH, element)
        
        if elementObject:
                elementObject.send_keys(value)
        else:
                print(fail_message)
                assert(False)

def quit_app():
       
        driver.quit()