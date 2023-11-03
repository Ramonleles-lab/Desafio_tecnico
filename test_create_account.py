from appium import webdriver
from appium.options.android import UiAutomator2Options
from typing import Any, Dict  
from Environments import*
from Elements import*
from AssertsByGroups import*
from assertDefinitions_pipeline import*
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

def teste_create_account(environment_app):
        
        #Start_test

        #create_new_account
        Create_account()
        
        #Quit_test
        quit_app()

        #End_test