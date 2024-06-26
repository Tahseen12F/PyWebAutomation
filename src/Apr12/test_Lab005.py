# Print title of webpage
from selenium import webdriver
import time
import pytest
import logging


@pytest.mark.smoke
def test_vwoLogin():
    # LOGGER = logging.getLogger(__name__)
    driver = webdriver.Chrome()  # Open/create the Session (POST request)
    driver.get("https://app.vwo.com")  # GET request to URL parameter
    print(driver.title)  # It will print Title
    # LOGGER.info(driver.title)
    assert driver.title == "Login - VWO"
    # time.sleep(5)
