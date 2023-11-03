from appium import webdriver
from appium.options.android import UiAutomator2Options
from typing import Any, Dict  
from Environments import*
from Elements import*
from AssertsByGroups import*
from assertDefinitions_pipeline import*
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

def test_login(environment_app):
        
        #Start_test

        #username_and_password
        Login_user()

        #Quit_test
        quit_app()

        #End_test