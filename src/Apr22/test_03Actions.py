from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pytest
import time
import allure
from selenium.webdriver.common.by import By


def testAction_DragDrop():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    drag = driver.find_element(By.ID, "draggable")
    drop = driver.find_element(By.ID, "droppable")
    ActionChains(driver).drag_and_drop(drag,drop).perform()
    time.sleep(10)
    driver.quit()
