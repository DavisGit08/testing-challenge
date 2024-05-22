import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Some utilities.
@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

