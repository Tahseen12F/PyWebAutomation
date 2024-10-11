import openpyxl
from selenium import webdriver
from allure_commons.types import AttachmentType
import time
import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)
import os


# Data driven TC for the Login page
def read_credential_from_user(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    for row in sheet.rows(min_rows=2, value=True):
        username, password = row
        credentials.append({
            "username": username,
            "password": password
        })
    return credentials


file_path = os.getcwd() + "\pyTestdata.xlsx"
print(file_path)


@pytest.mark.parametrize("user_cred", read_credential_from_user(file_path))
@allure.title("Verify Invalid Login with the Excel test data")
@allure.description("TC1 - Verify that login is not working after entering incorrect username and password")
def test_vwo_login(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    vwoLogin_negativeTC(username, password)
    print(username, password)


# Invalid logins for the VWO page
def vwoLogin_negativeTC(username, password):
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://app.vwo.com/")
    # Maximise the screen
    driver.maximize_window()
    usrname = driver.find_element(By.XPATH, "//input[@name ='username']")
    pswrd = driver.find_element(By.NAME, "password")
    usrname.send_keys(username)
    pswrd.send_keys(password)
    btn = driver.find_element(By.ID, "js-login-btn")
    btn.click()
    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]  # Exceptions want to ignore ; Import It
    WebDriverWait(driver=driver, timeout=5, poll_frequency=1, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))  # Similar to EW but with interval of 1s
    )
    result = driver.current_url
    if result != "https://app.vwo.com/#dashboard":
        ignore_list = [ElementNotVisibleException,
                       ElementNotSelectableException]  # Exceptions want to ignore ; Import It
        WebDriverWait(driver=driver, timeout=5, poll_frequency=1, ignored_exceptions=ignore_list).until(
            EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))
            # Similar to EW but with interval of 1s
        )
        error_msg = driver.find_element(By.ID, "js-notification-box-msg")  # if login details are wrong
        assert error_msg.text == "Your email, password, IP address or location did not match"
    else:
        print("Valid Login")
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
