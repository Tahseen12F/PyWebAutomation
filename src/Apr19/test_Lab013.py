# Using Link Text to locate the element : Link-Text works only with <a> tag.
# it will do either full match or exact match with the text.
# Using Partial Link Text to locate the element : Partial link text also works with <a> tag
# It will do partial match . Mainly used to search Contains - Keyword
# using Tag-Name - We used with findElements to search out the list of Tag names.
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_usingLocator():
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # Maximise the screen
    driver.maximize_window()
    # Finding username element
    # btn = driver.find_element(By.LINK_TEXT, "Make Appointment") - using Link Text to locate the element
    # btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Appointment")  -  Using Partial link text
    # Using Partial link text , we can either give partial text or full text. Both are applicable.
    list_of_Tags = driver.find_elements(By.TAG_NAME, "a") # Using Tag Name
    # find_elements to find out the list of tags.
    btn = list_of_Tags[5]
    btn.click()
    time.sleep(10)

    driver.quit()
