from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time


# Encapsulates page objects. It's the pages layer.
class PageSpeedTest:

    ### Page Objects ###

    # URLs
    URL = "https://www.debugbear.com/test/website-speed"
    #Input fields
    INPUT_URL = (By.NAME, "url")
    # Buttons
    BUTTON_START = (By.XPATH, "//button[text()='Start Test']")
    # Sections
    SECTION_METRICS = (By.CLASS_NAME, "metrics-section")
    # Messages on screen
    MSG_TITLE_MAIN = (By.XPATH, "//h1[contains(text(), 'Website Speed Test')]")
    MSG_TITLE_INFO = (By.XPATH, "//*[(text()='Enter a website URL to test page speed and see how to make it faster.')]")
    MSG_TESTING = (By.XPATH, "//div[contains(text(), 'Testing')]")
    MSG_TESTING_LOC = (By.XPATH, "//span[contains(text(), 'US East')]")
    MSG_TESTING_BANDWIDTH = (By.XPATH, "//span[contains(text(), 'Bandwidth')]")
    MSG_TESTING_LATENCY = (By.XPATH, "//span[contains(text(), 'Latency')]")
    MSG_TESTING_TROT = (By.XPATH, "//span[contains(text(), 'Throttling')]")
    MSG_TESTING_SPAN = ["US East", "Bandwidth", "Latency", "Throttling"]
    MSG_TESTING_MESSAGE = (By.XPATH, "//div[(text()='Waiting In Queue')]")
    MSG_TESTING_INFO = (By.XPATH, "//div[(text()='It usually takes just under a minute to finish the test.')]")
    MSG_INVALID_URL1 = (By.XPATH, "//div[(text()='Invalid URL')]") # Used when search for i.e: "."
    MSG_INVALID_URL2 = (By.XPATH, "//div[contains(text(), 'URL must include')]") # Used when search for i.e: "Google"
    MSG_INVALID_URL_EMPTY = (By.XPATH, "//div[(text()='Enter a website URL to start the performance test')]") # Used when search for empty value
    MSG_METRIC_OVERVIEW = (By.ID, "metric-overview")
    MSG_LIST_METRICS = ["Full TTFB", "First Contentful Paint", "Largest Contentful Paint", "Speed Index", "CPU Time", "Total Blocking Time", "Page Weight"]
    MSG_PAGE_SPEED_REPORT = (By.XPATH, "//h2[contains(text(), 'Page Speed Report')]")
    MSG_LIST_PAGE_SPEED_REPORT = ["US East", "Bandwidth", "Latency", "Throttling", "Chrome", "Lighthouse"]
    MSG_REAL_USER_SCORE = (By.XPATH, "//div[contains(text(), 'Real User Score')]")
    MSG_LAB_SCORE = (By.XPATH, "//div[contains(text(), 'Lab Score')]")
    MSG_TEST_RESULT = (By.ID, "test-result")
    MSG_RECOMENDATIONS = (By.ID, "recommendations")
    MSG_TIMELINE = (By.CLASS_NAME, "timeline-with-options")
    # Tables
    TABLE_RECOMENDATIONS = (By.CSS_SELECTOR, ".result-table result-table--has-details result-table--no-details-padding")
    TABLE_RECOMMENDATIONS_ROWS = (By.CLASS_NAME, "result-table__overview-row")
    # List
    SELECT_DEVICE = (By.NAME, "device")
    # Other elements
    STATUS_BAR_PROGRESS = (By.CLASS_NAME, "css-re4smq")


    ### Page Actions ###

    # Init browser
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    # Actions
    def load_page(self):
        self.browser.get(self.URL)
        assert WebDriverWait(self.browser, 20).until(EC.visibility_of_element_located(self.MSG_TITLE_MAIN)).is_displayed()
    
    def input_url(self, url):
        url_input = self.browser.find_element(*self.INPUT_URL)
        url_input.send_keys(url)
    
    def input_url_invalid(self, text):
        self.browser.find_element(*self.INPUT_URL).send_keys(text)
    
    def button_start(self):
        start_button = self.browser.find_element(*self.BUTTON_START)
        start_button.click()

    def select_device(self, device):
        assert WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.SELECT_DEVICE)).is_displayed()
        if (device == "Mobile"): val = 0
        if (device == "Desktop"): val = 1
        Select(self.browser.find_element(*self.SELECT_DEVICE)).select_by_index(0)
        Select(self.browser.find_element(*self.SELECT_DEVICE)).select_by_index(1)
        Select(self.browser.find_element(*self.SELECT_DEVICE)).select_by_index(val)
        self.assert_device(device)

    def assert_device(self, device):
        current_url = self.browser.current_url
        assert "device="+device.lower() in current_url

    def assert_all_main_page_elements(self):
        assert self.browser.find_element(*self.MSG_TITLE_MAIN).is_displayed()
        assert self.browser.find_element(*self.MSG_TITLE_INFO).is_displayed()
        assert self.browser.find_element(*self.BUTTON_START).is_displayed()

    def assert_msg(self, text, device):
        if text == "":
            assert WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.MSG_INVALID_URL_EMPTY)).is_displayed()
        elif text == ".":
            assert WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.MSG_INVALID_URL1)).is_displayed()
        elif text == "Testing":
            assert WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.MSG_TESTING)).is_displayed()
            assert self.browser.find_element(By.XPATH, "//span[contains(text(), '"+device+"')]").is_displayed()
            assert self.browser.find_element(*self.MSG_TESTING_BANDWIDTH).is_displayed()
            assert self.browser.find_element(*self.MSG_TESTING_LATENCY).is_displayed()
            assert self.browser.find_element(*self.MSG_TESTING_TROT).is_displayed()
            assert self.browser.find_element(*self.MSG_TESTING_MESSAGE).is_displayed()
            assert self.browser.find_element(*self.MSG_TESTING_INFO).is_displayed()
            assert self.browser.find_element(*self.MSG_TESTING_LOC).is_displayed()
            assert self.browser.find_element(*self.STATUS_BAR_PROGRESS).is_displayed()
        else:
            assert self.browser.find_element(*self.MSG_INVALID_URL2).is_displayed()

    def assert_page_speed_report(self, device):
        msg = WebDriverWait(self.browser, 500).until(EC.visibility_of_element_located(self.MSG_PAGE_SPEED_REPORT))
        assert msg.is_displayed()
        assert self.browser.find_element(By.XPATH, "//span[contains(text(), '"+device+"')]").is_displayed()
        reports = self.MSG_LIST_PAGE_SPEED_REPORT
        for report in reports:
            if not self.browser.find_element(By.XPATH, f"//span[contains(text(),'{report}')]").is_displayed():
                return False
        return True

    def assert_metric_overview(self):
        assert self.browser.find_element(*self.MSG_METRIC_OVERVIEW).is_displayed()
        metrics = self.MSG_LIST_METRICS
        for metric in metrics:
            if not self.browser.find_element(By.XPATH, f"//span[text()='{metric}']").is_displayed():
                return False
        return True
        # Here we could also add validations for metrics (the numbers)...

    def assert_test_result(self):
        assert self.browser.find_element(*self.MSG_TEST_RESULT).is_displayed()
        assert self.browser.find_element(*self.MSG_TIMELINE).is_displayed()
        # Here we can add much more validations, like videos recorded and images are displayed on screen...
    
    def assert_recommendations(self):
        self.browser.find_element(*self.MSG_RECOMENDATIONS).is_displayed()
        self.browser.find_element(*self.TABLE_RECOMMENDATIONS_ROWS).is_displayed()
        rows = self.browser.find_elements(*self.TABLE_RECOMMENDATIONS_ROWS)
        assert len(rows) > 3
    
    def assert_test_results(self, device):
        self.assert_page_speed_report(device)
        self.assert_metric_overview()
        self.assert_test_result()
        self.assert_recommendations()
    