# Actions Class : It's an ability provided by selenium for handling keyboard and Mouse events.

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import pytest
import time
import allure
from selenium.webdriver.common.by import By


def test_actionsClass():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    time.sleep(5)
    first_name = driver.find_element(By.NAME, "firstname")

    # To use Action class, we need to create an object of Action Chains class
    actions = ActionChains(driver)
    # Send Keys but with the shift
    actions.key_down(Keys.SHIFT)\
        .send_keys_to_element(first_name, "tahseen")\
        .key_up(Keys.SHIFT).perform()
    actions.context_click(driver.find_element(By.XPATH,"//a[text() = 'Click here to Download File']")).perform()
    time.sleep(15)

