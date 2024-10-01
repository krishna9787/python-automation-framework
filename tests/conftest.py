import pytest
from selenium import webdriver
# from ..config import IMPLICIT_WAIT, BROWSER, TEST_URL     
        
@pytest.fixture()
def setup_and_teardown():
    global driver
    driver=webdriver.Chrome()
    driver.get("https://www.amazon.ca/")
    driver.maximize_window()
    yield
    driver.quit()