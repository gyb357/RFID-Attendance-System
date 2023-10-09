from driver import Driver
from selenium.common.exceptions import WebDriverException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DriverManager():
    def __init__(self, visible):
        self.web = Driver()
        self.web(visible)
        self.driver = self.web.driver

    def connect(self, url):
        try:
            self.driver.get(url)
        except WebDriverException as e:
            print(e)
    
    def alert_handler(self):
        text = None
        try:
            WebDriverWait(self.driver, 0).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
        except (NoAlertPresentException, TimeoutException):
            pass
        return text
    
    def frame(self, frame):
        try:
            self.driver.switch_to.default_content()

            for i in frame:
                self.driver.switch_to.frame(i)
        except WebDriverException as e:
            print(e)
    
    def send_keys(self, xpath, key):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.send_keys(key)
        except WebDriverException as e:
            print(e)
    
    def click(self, xpath):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.click()
        except WebDriverException as e:
            print(e)

    def extract_table(self, xpath, tag):
        data = []
        try:
            tr = self.driver.find_element(By.XPATH, xpath)
            cells = tr.find_elements(By.TAG_NAME, tag)

            for cell in cells:
                data.append(cell.text)
        except WebDriverException as e:
            print(e)
        return data, cells

