from color import Colors
from selenium.webdriver import ChromeOptions, Chrome
from file import FileManager
from selenium.common.exceptions import WebDriverException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class WebDriver(Colors):
    def __init__(self, visible):
        super().__init__()
        self.visible = not visible

    def get_driver(self):
        try:
            option = ChromeOptions()
            option.headless = self.visible
            driver = Chrome(options=option)
            config = FileManager('config.txt')

            if config.read() == 'false':
                self.test_driver(driver, config)

            self.print('green', 'get(): Success')
            return driver
        except WebDriverException as e:
            self.print('red', 'get(): Fail', e)
            raise
    
    def test_driver(self, driver, config):
        try:
            driver.get('chrome://newtab/')
            driver.quit()
            config.write('true')
            self.print('green', 'test(): Success')
        except WebDriverException as e:
            self.print('red', 'test(): Fail', e)
            raise


class WebDriverManager(WebDriver):
    def __init__(self, visible):
        super().__init__(visible)
        self.driver = self.get_driver()

    def connect(self, url):
        try:
            self.driver.get(url)
            self.print('green', f'connect(): {url}')
        except WebDriverException as e:
            self.print('red', f'connect(): {url}', e)
            raise
    
    def alert_handler(self):
        try:
            WebDriverWait(self.driver, 0).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            self.print('yellow', f'alert_handler(): {text}')
            return text
        except (NoAlertPresentException, TimeoutException):
            pass
    
    def frame(self, frame):
        try:
            self.driver.switch_to.default_content()
            
            for f in frame:
                self.driver.switch_to.frame(f)

            path = ' > '.join(frame)
            self.print('green', f'frame(): {path}')
        except WebDriverException as e:
            self.print('red', f'frame(): {path}', e)
            raise

    def send(self, xpath, key):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.send_keys(key)
            self.print('cyan', f'    send(): {key}')
        except WebDriverException as e:
            self.print('red', f'    send(): {xpath}, {key}', e)
            raise

    def click(self, xpath):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            element.click()
            self.print('cyan', f'    click(): {xpath}')
        except WebDriverException as e:
            self.print('red', f'    click(): {xpath}', e)
            raise
    
    def extract_table(self, xpath, tag):
        try:
            element = self.driver.find_element(By.XPATH, xpath)
            tags = element.find_elements(By.TAG_NAME, tag)

            tmp = []
            for tag in tags:
                tmp.append(tag.text)
            return tmp, tag
        except WebDriverException as e:
            self.print('red', f'extract_table(): {xpath}, {tag}', e)
            raise


class WebAutomation(WebDriverManager):
    def __init__(self, visible):
        super().__init__(visible)

    def login(self, url, frame, keys, id, pw, click):
        self.connect(url)
        self.frame(frame)
        self.send(keys[0], id)
        self.send(keys[1], pw)
        self.click(click)
        return self.login_handler(self.alert_handler())

    def login_handler(self, alert):
        str = '올바른 아이디나 패스워드가 아닙니다.'
        if alert is not None:
            if str in alert:
                self.print('red', 'login_handler(): Fail')
                return False
        
        self.print('green', 'login_handler(): Success')
        return True

    def get_student(self, frame, xpath, tag):
        col, data, _, _ = self.get_table(frame, xpath, tag)
        return col, data

    def get_timetable(self, frame, xpath, tag):
        col, _, _, tag2 = self.get_table(frame, xpath, tag)
        data = []
        for i in range(len(tag2)):
            data.append(self.extract_table(f'//*[@id="getApplyAbsence"]/table/tbody/tr[{i + 1}]', 'td')[0])
        return col, data
    
    def get_table(self, frame, xpath, tag):
        self.frame(frame)
        col, tag1 = self.extract_table(xpath[0], tag[0])
        data, tag2 = self.extract_table(xpath[1], tag[1])
        return col, data, tag1, tag2

