from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
import time
import allure
from selenium.webdriver.common.by import By


def testWin():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    time.sleep(10)
    main_window_handle = driver.current_window_handle
    print(main_window_handle)
    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()
    window_handle = driver.window_handles
    print(window_handle)

    for handle in window_handle:
        driver.switch_to.window(handle)
        if "new window" in driver.page_source:
            print("Found the Text")
            break
            
