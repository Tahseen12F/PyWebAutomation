# Maximize the webpage screen
from selenium import webdriver
import time
import pytest


@pytest.mark.smoke
def test_vwoLogin():
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://app.vwo.com")  # GET request to URL parameter
    print(driver.title)  # It will print Title
    driver.maximize_window()  # It will maximise the screen
    assert driver.title == "Login - VWO"
    # time.sleep(5)
