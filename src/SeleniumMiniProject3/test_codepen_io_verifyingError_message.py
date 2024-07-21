# Selenium Mini Project 3
# Open the URL - https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage
# Enter all the fields excepts the username
# Verify that the error message comes when you click on the submit button.

from allure_commons.types import AttachmentType
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
import allure


@pytest.mark.smoke
@allure.title("Verify that codepen registered page is opened successfully")
@allure.description(
    "TC#1 - Enter all fields except username and click submit button & verify the error message post click.")
def test_userloginError():
    driver = webdriver.Chrome()
    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.switch_to.frame(driver.find_element(By.ID, "result"))
    emailId = driver.find_element(By.XPATH, "//input[@id = 'email']")
    emailId.send_keys("TC1@gmail.com")
    time.sleep(2)
    pswrd = driver.find_element(By.CSS_SELECTOR, "#password")
    pswrd.send_keys("123456")
    time.sleep(2)
    confrmPaswrd = driver.find_element(By.ID, "password2")
    confrmPaswrd.send_keys("123456")
    time.sleep(2)
    btn = driver.find_element(By.XPATH, "//*[contains(text(), 'Submit')]")
    btn.click()
    time.sleep(10)
    allure.attach(driver.get_screenshot_as_png(), name="empty-username", attachment_type=AttachmentType.PNG)  # allure attach
    assert (driver.find_element(By.XPATH,
                                "//input[@id='username']/following::small").text == "Username must be at least 3 characters")
    driver.quit()
