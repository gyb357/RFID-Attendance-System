import utils as utils

from utils import Colors
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


color = Colors()


class WebDriver():
    def __init__(self):
        self.driver = None
        self.test = False
        self.config = ""

    def __call__(self, visible):
        self.config = utils.read_file('web\config.txt')
        if self.config == "":
            raise ValueError("Problem reading config.txt")
        else:
            self.test = utils.operator_elif(
                self.config == 'false', False,
                self.config == 'true', True,
                False
            )
        
        if self.test == False:
            self.test = self.test_driver()
        if self.test == True:
            self.driver = self.get_driver(utils.operator(visible is True, False, True))
            utils.write_file('web\config.txt', 'true')

    def get_driver(self, headless):
        try:
            option = webdriver.ChromeOptions()
            option.headless = headless
            driver = webdriver.Chrome(options=option)
            color.print_color('green', "get_driver(): Success")
        except WebDriverException as e:
            color.print_color('red', "get_driver(): Failed", e)
        return driver
    
    def test_driver(self):
        try:
            driver = self.get_driver(True)
            driver.get('chrome://newtab/')
            driver.quit()
            test = True
            color.print_color('green', "test_driver(): Success")
        except WebDriverException as e:
            color.print_color('red', "test_driver(): Failed", e)
        return test


class WebDriverManager():
    def __init__(self, visible):
        self.web = WebDriver()
        self.web(visible)
        self.driver = self.web.driver

        if not self.valid():
            raise ValueError("Web driver not found")

    def valid(self):
        return utils.operator(self.driver is None, False, True)
    
    def connect(self, url):
        try:
            self.driver.get(url)
            color.print_color('green', f"connect(): {url}")
        except WebDriverException as e:
            color.print_color('red', f"connect(): {url}", e)
    
    def alert_handler(self):
        text = None
        try:
            WebDriverWait(self.driver, 0).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            color.print_color('yellow', f"alert_handler(): {text}")
        except (NoAlertPresentException, TimeoutException):
            color.print_color('green', "alert_handler(): No such alert window found")
        return text
    
    def frame(self, frame):
        try:
            self.driver.switch_to.default_content()
            path = " > ".join(frame)

            for i in frame:
                self.driver.switch_to.frame(i)

            color.print_color('green', f"frame(): {path}")
        except WebDriverException as e:
            color.print_color('red', "frame(): No such frame found", e)

    def send_keys(self, xpath, key, description):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.send_keys(key)
            color.print_color('cyan', f" -> Send '{key}' to {description}")
        except WebDriverException as e:
            color.print_color('red', "send_keys(): No such xpath found", e)

    def click(self, xpath, description):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.click()
            color.print_color('cyan', f" -> Click {description}")
        except WebDriverException as e:
            color.print_color('red', "click(): No such xpath found", e)
    
    def extract_table(self, xpath, tag_name):
        data = []
        try:
            tr = self.driver.find_element(By.XPATH, xpath)
            td = tr.find_elements(By.TAG_NAME, tag_name)

            for i in td:
                data.append(i.text)
            
            color.print_color('green', f"extract_table(): {data}")
        except WebDriverException as e:
            color.print_color('red', "extract_table(): No such table found", e)
        return td, data

