# Close() vs Quit()

from selenium import webdriver
import time
import pytest


def test_vwoLogin():
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://app.vwo.com")  # GET request to URL parameter
    print(driver.title)  # It will print Title
    print(driver.session_id)
    driver.maximize_window()  # It will maximise the screen
    assert driver.title == "Login - VWO"

    driver.close()  # It will close the current tab only
    time.sleep(10)
    driver.quit()  # It will close all the tabs/windows
