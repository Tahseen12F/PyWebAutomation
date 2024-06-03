# SELENIUM PROJECT #1 - MINI PROJECT
# open the url - https://katalon-demo-cura.herokuapp.com/
# click on the make appointment button
# verify that url changes - assert
# time.sleep(3)
# enter the username, password
# next page verify the current url
# make appointment text on the web page.
import allure
import pytest
# from allure_commons.types import AttachmentType
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


@pytest.mark.run(order=1)
@allure.title("Verify Login")
@allure.description("TC1 - Verify that login is working")
def test_verifyLogin():
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://katalon-demo-cura.herokuapp.com/")  # Open the URL
    time.sleep(5)
    print(driver.title)  # print the title
    assert driver.title == "CURA Healthcare Service"  # verify the URL


@pytest.mark.run(order=2)
@allure.title("Verify Appointment Btn")
@allure.description("TC1 - Verify that Button is working")
def test_verifyAppointmentButton():
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    btn = driver.find_element(By.ID, "btn-make-appointment")
    btn.click()  # Click on Make appointment button and verify


@pytest.mark.run(order=3)
@allure.title("Verify URL")
@allure.description("TC1 - Verify that URL change is working")
def test_verifyURLChange():
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://katalon-demo-cura.herokuapp.com/")  # Open the URL
    btn = driver.find_element(By.ID, "btn-make-appointment")
    btn.click()  # Click on Make appointment button
    url = driver.current_url
    assert url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"  # verify the URL Change
    time.sleep(3)


@pytest.mark.run(order=4)
@allure.title("Verify Credential")
@allure.description("TC1 - Verify the correct Credential")
def test_verifyCredentialAndText():
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://katalon-demo-cura.herokuapp.com/")  # Open the URL
    btn = driver.find_element(By.ID, "btn-make-appointment")
    btn.click()  # Click on Make appointment button
    url = driver.current_url
    assert url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"  # verify the URL Change
    time.sleep(3)
    usr_element = driver.find_element(By.ID, "txt-username")
    usr_element.send_keys("John Doe")  # Input the username
    pswrd_element = driver.find_element(By.ID, "txt-password")
    pswrd_element.send_keys("ThisIsNotAPassword")  # Input the password
    login = driver.find_element(By.ID, "btn-login")
    login.click()  # Click on Login Button
    time.sleep(3)
    verify_text = driver.find_element(By.XPATH, "//div/h2")
    print(verify_text)  # Print the text
    assert verify_text.text == "Make Appointment"  # verify the Text
    # allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
