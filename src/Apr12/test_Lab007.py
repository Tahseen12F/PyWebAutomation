# Print the page - source
from selenium import webdriver
import time
import pytest


@pytest.mark.smoke
def test_vwoLogin():
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://app.vwo.com")  # GET request to URL parameter
    print(driver.title)  # It will print Title
    print(driver.page_source)
    print(driver.session_id)
    driver.maximize_window()  # It will maximise the screen
    assert driver.title == "Login - VWO"