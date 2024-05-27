from selenium import webdriver
import time


def test_vwoLogin():
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://app.vwo.com")  # GET request to URL parameter
    time.sleep(5)
