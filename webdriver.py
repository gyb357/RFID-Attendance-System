import utils

from utils import Colors
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebDriver(Colors):
    def __init__(self):
        super().__init__()
        self.driver = None
        self.test = False

    def __call__(self, visible):
        if self.test == False:
            self.test = self.test_webdriver()

        if self.test == True:
            headless = utils.operator(visible==True, False, True)
            self.driver = self.get_webdriver(headless)

    def get_webdriver(self, headless):
        try:
            option = webdriver.ChromeOptions()
            option.headless = headless
            driver = webdriver.Chrome(options=option)
            self.print_color('green', "get_webdriver(): Success")
        except WebDriverException as e:
            driver = None
            self.print_color('red', "get_webdriver(): Failed", e)
        finally:
            return driver

    def test_webdriver(self):
        try:
            self.print_color('magenta', "test_webdriver(): Started")
            driver = self.get_webdriver(True)
            driver.get("chrome://newtab/")
            driver.quit()
            test = True
            self.print_color('green', "test_webdriver(): Complete")
        except WebDriverException as e:
            test = False
            self.print_color('red', "test_webdriver(): Failed", e)
        finally:
            return test


class WebDriverManager(WebDriver):
    def __init__(self, visible):
        super().__init__()
        self.web = WebDriver()
        self.web(visible)
        self.driver = self.web.driver

    def valid(self):
        return utils.operator(self.driver==None, False, True)
    
    def connect(self, url):
        if not self.valid():
            raise ValueError("connect(): Web driver not found")
        try:
            self.driver.get(url)
            self.print_color('green', f"connect(): {url}")
        except WebDriverException as e:
            self.print_color('red', f"connect(): {url}", e)

    def alert_handler(self):
        if not self.valid():
            raise ValueError("alert_handler(): Web driver not found")
        try:
            WebDriverWait(self.driver, 0).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            self.print_color('yellow', f"alert_handler(): {text}")
        except (NoAlertPresentException, TimeoutException):
            text = None
            self.print_color('green', "alert_handler(): Alert window not found")
        finally:
            return text
        
    def frame(self, frame):
        if not self.valid():
            raise ValueError("frame(): Web driver not found")
        try:
            self.driver.switch_to.default_content()
            path = " > ".join(frame)

            for i in frame:
                self.driver.switch_to.frame(i)
            
            self.print_color('green', f"frame(): {path}")
        except WebDriverException as e:
            self.print_color('red', "frame(): No such frame found", e)

    def send_keys(self, xpath, key, description):
        if not self.valid():
            raise ValueError("send_keys(): Web driver not found")
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.send_keys(key)
            self.print_color('cyan', f" -> Send '{key}' to {description}")
        except WebDriverException as e:
            self.print_color('red', "send_keys(): No such xpath found", e)

    def click(self, xpath, description):
        if not self.valid():
            raise ValueError("click(): Web driver not found")
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.click()
            self.print_color('cyan', f" -> Click {description}")
        except WebDriverException as e:
            self.print_color('red', "click(): No such xpath found", e)

