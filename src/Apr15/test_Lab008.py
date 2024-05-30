from selenium import webdriver
import time
import pytest


def test_sessionOpen():
    driver = webdriver.Chrome()
    time.sleep(10)
    # whenever in code there is : webdriver.Chrome() - A fresh copy of browser is created
    # Once this is closed, Everything will be deleted
