# Selenium Mini Project #2
# Open the URL - https://www.idrive360.com/enterprise/login
# Enter the username, password respectively
# Verify that Trial is finished and current URL also
# Add a logic to add Allure Screen for the Trial end.
from allure_commons.types import AttachmentType
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
import allure


@pytest.mark.smoke
@allure.title("Verify Login Page")
@allure.description("TC1 - Verify that login is working fine and verify Trial is finished and current URL")
def test_idrive360Login():
    driver = webdriver.Chrome()
    driver.get("https://www.idrive360.com/enterprise/login")
    driver.maximize_window()
    driver.find_element(By.XPATH,"//input[@id='username']").send_keys("augtest_040823@idrive.com")
    driver.find_element(By.XPATH,"//input[@name='password']").send_keys("123456")
    driver.find_element(By.XPATH,"//button[@id='frm-btn']").click()
    time.sleep(10)
    current_url = driver.current_url
    time.sleep(15)
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Error - Invalid URL"
    header_message = driver.find_element(By.XPATH, "//h5[@class='id-card-title']").text
    print(header_message)
    assert header_message == "Your free trial has expired", "Error - Invalid message"
    allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    driver.quit()


