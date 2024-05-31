# Navigation control commands in Selenium
# back(), forward(). refresh(), to()

from selenium import webdriver
import time


def test_naviCommand():
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://bing.com/chat")
    time.sleep(10)  # Tells Python Interpreter to wait for 10 seconds
    driver.refresh()  # Refresh the page
    time.sleep(5)
    driver.get("https://google.com")  # Navigate to different URL
    driver.back()  # Navigate back to prev page
    time.sleep(5)
