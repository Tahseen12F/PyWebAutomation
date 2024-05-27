# Selenium - Used to Automate browsers
# Selenium 3 uses Json wire protocol
# Selenium 4 uses W3C protocol + selenium manager
# Note :- If pip install selenium 4.x (Then you don't need to set up browser drivers)

# SELENIUM 3

from selenium import webdriver


def test_open_website():
    pass
    # driver path = 'user/tf/download/edge/msedgedriver'
    # driver = webdriver.EdgeService(executable_path = driver_path)
    # driver.get("http://app.vwo.com")
