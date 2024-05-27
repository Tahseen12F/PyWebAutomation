# Selenium 4
from selenium import webdriver


def test_vwoLogin():
    driver = webdriver.Edge()  # Open/create the Session (POST request)
    driver.get("https://app.vwo.com")  # GET request to URL parameter
    # Python Interpreter will optimize if there is no command. It will stop execution.
    # get() loads a webpage in the current browser session
