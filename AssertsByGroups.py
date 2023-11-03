from appium import webdriver
from appium.options.android import UiAutomator2Options
from typing import Any, Dict  
from Environments import*
from Elements import*
from assertDefinitions_pipeline import*
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from selenium.webdriver.common.keys import Keys

def Login_user():
    send_keys(Elements_variable.login_email,Elements_variable.login_email_value)
    send_keys(Elements_variable.login_password,Elements_variable.login_password_value)
    click_by_xpath(Elements_variable.Button_login)
    (10)

def Create_account():
    click_by_xpath(Elements_variable.Button_create_account)
    send_keys(Elements_variable.add_email_acconunt_,Elements_variable.add_email_acconunt_value)
    send_keys(Elements_variable.add_password_account,Elements_variable.add_password_account_value)
    send_keys(Elements_variable.add_password_account_repeat,Elements_variable.add_password_account_repeat_value)
    click_by_xpath(Elements_variable.Button_register)

def add_product_cart():
    click_by_xpath(Elements_variable.select_product1)
    click_by_xpath(Elements_variable.add_product1)
    click_by_xpath(Elements_variable.add_button_cart)

def Checkout_logged_in():
    click_by_xpath(Elements_variable.button_paymant)
    click_by_xpath(Elements_variable.button_pay_now)
    click_by_xpath(Elements_variable.button_ok)

def Search_field():
    click_by_xpath(Elements_variable.Elements_heroes)
    send_keys(Elements_variable.search_field,Elements_variable.search_field_value)
    click_by_xpath(Elements_variable.Select_heroes)

def Select_multiple_products():
    sleep(5)
    click_by_xpath(Elements_variable.Button_return_navigate)
    click_by_xpath(Elements_variable.Button_return_navigate)
    click_by_xpath(Elements_variable.select_product2)
    click_by_xpath(Elements_variable.add_product2)
    click_by_xpath(Elements_variable.add_button_cart2)