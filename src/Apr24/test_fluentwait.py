from allure_commons.types import AttachmentType
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


@pytest.mark.smoke
@allure.title("Verify Login")
@allure.description("TC1 - Verify that login is not working after entering incorrect username and password")
def test_vwoLoginNegative():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    username = driver.find_element(By.XPATH, "//input[@name ='username']")
    pswrd = driver.find_element(By.NAME, "password")
    username.send_keys("admin@gmail.com")
    pswrd.send_keys("admin")
    btn = driver.find_element(By.ID, "js-login-btn")
    btn.click()
    # Explicit wait
    # WebDriverWait(driver=driver, timeout=5).until(
    # EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))
    # )
    # "Your email, password, IP address or location did not match"

    # Fluent Wait
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]  # Exceptions want to ignore ; Import It
    WebDriverWait(driver=driver, timeout=5, poll_frequency=1, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))  # Similar to EW but with interval of 1s
    )

    error_msg = driver.find_element(By.ID, "js-notification-box-msg")  # if login details are wrong
    assert error_msg.text == "Your email, password, IP address or location did not match"
    print(error_msg.text)
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
