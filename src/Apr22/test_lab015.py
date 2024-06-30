# Use of CSS Selector
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


def test_vwoLogin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    username = driver.find_element(By.CSS_SELECTOR, "#login-username")
    username.send_keys("TF")
    time.sleep(5)
    driver.quit()