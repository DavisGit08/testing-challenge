from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



# Encapsulates common logic to be used be all pages. It's the behavior layer. Not being used cause it's not necessary to apply this layer of logic. Not removed because could be used (maybe) in the future :)
class PageBehavior:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 20)

    def find_element(self, by, value):
        return self.browser.find_element(by, value)
    
    def assert_element(self):
        return self.browser.is_displayed()
    
    # Try to click, if not try to click by coordenates

    # etc.