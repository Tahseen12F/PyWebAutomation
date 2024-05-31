# Locators in Selenium
# ID, Name, ClassName, tag Name, Link text, PartialLink text, Xpath and CSS Selector

from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_useOfLocator():
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    Appointment_btn = driver.find_element(By.ID, "btn-make-appointment")  # It will return one element
    Appointment_btn.click()
    time.sleep(25)
    driver.quit()