import pytest
from tests.ui.utils.utils import browser
from tests.ui.pages.page_debugbear import PageSpeedTest
import time


@pytest.fixture
def page(browser):
    return PageSpeedTest(browser)


#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·# RAINY PATHS #·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#

# Test with empty url value and "Desktop" device.
def test_rainy_desktop_invalid_empty_desktop(page):
    page.load_page()
    page.select_device("Desktop")
    page.input_url_invalid("")
    page.button_start()
    page.assert_msg("", "Desktop")

# Test with "." url value and "Desktop" device.
def test_rainy_desktop_invalid1_desktop(page):
    page.load_page()
    page.select_device("Desktop")
    page.input_url_invalid(".")
    page.button_start()
    page.assert_msg(".", "Desktop")

# Test with invalid url value and "Desktop" device.
def test_rainy_desktop_invalid2_desktop(page):
    page.load_page()
    page.select_device("Desktop")
    page.input_url_invalid("idoven")
    page.button_start()
    page.assert_msg("idoven", "Desktop")

# Test with empty url value and "Mobile" device.
def test_rainy_mobile_invalid_empty_mobile(page):
    page.load_page()
    page.select_device("Mobile")
    page.input_url_invalid("")
    page.button_start()
    page.assert_msg("", "Mobile")

# Test with "." url value and "Mobile" device.
def test_rainy_mobile_invalid1_mobile(page):
    page.load_page()
    page.select_device("Mobile")
    page.input_url_invalid(".")
    page.button_start()
    page.assert_msg(".", "Mobile")

# Test with invalid url value and "Mobile" device.
def test_rainy_mobile_invalid2_mobile(page):
    page.load_page()
    page.select_device("Mobile")
    page.input_url_invalid("idoven")
    page.button_start()
    page.assert_msg("idoven", "Mobile")


#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·# HAPPY PATHS #·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#·#

# Basic test to load main page and validate elements in the main page.
def test_happy_health_check(page):
    page.load_page()
    page.assert_all_main_page_elements()

# Test with idoven url without "http://" and "Desktop" device to check if it's being resolved.
def test_happy_resolve_url_desktop(page):
    page.load_page()
    page.select_device("Desktop")
    page.input_url("es.idoven.ai")
    page.button_start()
    page.assert_msg("Testing", "Desktop")

# Test with valid url and validate testing in process page for "Mobile".
def test_happy_testing_in_process_desktop(page):
    page.load_page()
    page.select_device("Desktop")
    page.input_url("https://es.idoven.ai/")
    page.button_start()
    page.assert_msg("Testing", "Desktop")

# Test with valid url and test results for "Mobile".
def test_happy_test_results_desktop(page):
    page.load_page()
    page.select_device("Desktop")
    page.input_url("https://es.idoven.ai/")
    page.button_start()
    page.assert_test_results("Desktop")

# Test with idoven url without "http://" and "Mobile" device to check if it's being resolved.
def test_happy_resolve_url_mobile(page):
    page.load_page()
    page.select_device("Mobile")
    page.input_url("es.idoven.ai")
    page.button_start()
    page.assert_msg("Testing", "Mobile")

# Test with valid url and validate testing in process page for "Mobile".
def test_happy_testing_in_process_mobile(page):
    page.load_page()
    page.select_device("Mobile")
    page.input_url("https://es.idoven.ai/")
    page.button_start()
    page.assert_msg("Testing", "Mobile")

# Test with valid url and test results for "Mobile".
def test_happy_test_results_mobile(page):
    page.load_page()
    page.select_device("Mobile")
    page.input_url("https://es.idoven.ai/")
    page.button_start()
    page.assert_test_results("Mobile")
