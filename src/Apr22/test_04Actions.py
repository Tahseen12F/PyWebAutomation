from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pytest
import time
import allure
from selenium.webdriver.common.by import By


def testAction_DragDrop():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/frame_with_nested_scrolling_frame_out_of_view.html")
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    # scroll_origin = ScrollOrigin.from_element(iframe)
    # ActionChains(driver).scroll_from_origin(scroll_origin , 0, 200).perform()
    ActionChains(driver).scroll_to_element(iframe).perform()
    time.sleep(100)
