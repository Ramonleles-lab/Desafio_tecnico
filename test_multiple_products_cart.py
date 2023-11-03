from appium import webdriver
from appium.options.android import UiAutomator2Options
from typing import Any, Dict  
from Environments import*
from Elements import*
from AssertsByGroups import*
from assertDefinitions_pipeline import*
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

def test_multiple_products_cart(environment_app):
        
        #Start_test

        #username_and_password
        Login_user()

        #select_product_in_cart
        add_product_cart()

        #select_more_products
        Select_multiple_products()

        #checkout_produt
        Checkout_logged_in()

        #Quit_test
        quit_app()

        #End_test