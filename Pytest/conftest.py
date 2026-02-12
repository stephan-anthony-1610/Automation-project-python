import pytest
from selenium import webdriver
from time import sleep

@pytest.fixture(autouse=True,scope="module", params=['chrome', 'firefox'])
def _driver(request):
    print("Test has started")
    browser = request.param  
    if browser.lower()=='chrome':
        driver=webdriver.Chrome()
    else:
        driver=webdriver.Firefox()
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    sleep(2)
    yield driver
    sleep(2)
    print("Test has ended")
    driver.quit()