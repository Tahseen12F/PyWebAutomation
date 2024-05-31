from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_vwoLogin_negativeTC():
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://app.vwo.com/")
    # Maximise the screen
    driver.maximize_window()
    # Finding username element
    user_name = driver.find_element(By.NAME, "username")
    # Input the username in the text box
    user_name.send_keys("admin")
    # Finding password element
    pswrd = driver.find_element(By.NAME, "password")
    # Input the password in the text box
    pswrd.send_keys("1234")
    time.sleep(5)
    # Click on Sign In button
    login = driver.find_element(By.ID, "js-login-btn")
    login.click()
    time.sleep(5)
    error_msg = driver.find_element(By.ID, "js-notification-box-msg")  # if login details are wrong
    assert error_msg.text == "Your email, password, IP address or location did not match"
    print(error_msg.text)
    # text is a function which will return the text whatever present
    driver.quit()
