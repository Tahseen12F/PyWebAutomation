# Navigation control commands in Selenium
# back(), forward(). refresh(), to()

from selenium import webdriver
import time


def test_naviCommand():
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://bing.com/chat")
    time.sleep(10)  # Tells Python Interpreter to wait for 25 seconds
    driver.get("https://google.com")  # Navigate to different URL
    driver.back()
    time.sleep(5)