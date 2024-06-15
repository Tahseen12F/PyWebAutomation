# Using Relative XPATH
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


def test_vwoLogin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    username = driver.find_element(By.XPATH, "//input[@name ='username']")
    username.send_keys("a12")
    time.sleep(5)
    driver.quit()