from file_manager import FileManager
from utils import operator_elif
from selenium.webdriver import ChromeOptions, Chrome
from selenium.common.exceptions import WebDriverException


class Driver():
    def __init__(self):
        self.driver = None
        self.test = False

    def __call__(self, visible):
        config = FileManager('config.txt')
        txt = config.read()
        self.test = operator_elif(
            txt == 'false', False,
            txt == 'true', True,
            False
        )
        if self.test == False:
            self.test = self.test_driver()
        if self.test == True:
            self.driver = self.get_driver(not visible)
            config.write('true')

    def get_driver(self, headless):
        driver = None
        try:
            option = ChromeOptions()
            option.headless = headless
            driver = Chrome(options=option)
        except WebDriverException as e:
            print(e)
        return driver
    
    def test_driver(self):
        test = False
        try:
            driver = self.get_driver(True)
            driver.get('chrome://newtab/')
            driver.quit()
            test = True
        except WebDriverException as e:
            print(e)
        return test

