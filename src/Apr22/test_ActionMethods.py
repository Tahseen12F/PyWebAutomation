from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pytest
import time
import allure
from selenium.webdriver.common.by import By


def test_actionsClass():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    action = ActionChains(driver)
    click = driver.find_element(By.ID, "click")
    action.click(click).perform()
    # clickable = driver.find_element(By.ID, "clickable")
    # action.click_and_hold(clickable).key_down(Keys.SHIFT).send_keys("selenium").key_up(Keys.SHIFT).perform()
    time.sleep(20)
