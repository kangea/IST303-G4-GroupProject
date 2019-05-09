import os
import re

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

HOMEPAGE = 'http://127.0.0.1:8000/'

USER_NAME = 'testuser'
USER_PASSWORD = 'quest1234'

def test_homepage(driver):
    driver.get(HOMEPAGE)
    expected = "QuEST"
    assert driver.title == expected

def test_logginginout(driver):
    driver.get(HOMEPAGE)
    driver.find_element_by_id('loginlink').click()
    driver.find_element_by_name('username').send_keys(USER_NAME)
    driver.find_element_by_name('password').send_keys(USER_PASSWORD + Keys.RETURN)
    driver.find_element_by_id('logoutlink').click()
    expected = "You have logged out."
    p = driver.find_element_by_tag_name('p')
    assert p.text == expected

def test_products(driver):
    driver.get(HOMEPAGE)
    driver.find_element_by_id('productlink').click()
    expected = "PRODUCTS"
    h2 = driver.find_element_by_tag_name('h2')
    assert h2.text == expected

def test_brands(driver):
    driver.get(HOMEPAGE)
    driver.find_element_by_id('brandlink').click()
    expected = "FEATURED BRANDS"
    h2 = driver.find_element_by_tag_name('h2')
    assert h2.text == expected
