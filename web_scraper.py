from driver_manager import DriverManager
import pandas as pd
import matplotlib.pyplot as plt


class WebScraper():
    def __init__(self, id, pw):
        self.web = DriverManager(visible=False)
        self.driver = self.web.driver

        self.id = id
        self.pw = pw

    def __call__(self):
        self.login()
        student_info = self.get_student_info()
        subject_info = self.get_subject_info()
        self.logout()
        return student_info, subject_info
    
    def login(self):
        self.web.connect('https://intra.wku.ac.kr/WEB/SWupis/')
        self.web.frame(['FR_WUPIS_MAIN'])
        self.web.send_keys('//*[@id="userid"]', self.id)
        self.web.send_keys('//*[@id="passwd"]', self.pw)
        self.web.click('//*[@id="f_login"]/fieldset/dl/dd[3]/input')
        self.web.alert_handler()

        # 정보서비스 클릭
        self.web.frame(['FR_WUPIS_MAIN', 'MAIN', 'topFrame'])
        self.web.click('/html/body/table/tbody/tr/td[2]/a')

        # 출결조회 클릭
        self.web.frame(['FR_WUPIS_MAIN', 'MAIN', 'leftFrame'])
        self.web.click('/html/body/div/div/div/ul/li[5]/div[2]/ul/li[29]/a')
    
    def logout(self):
        self.web.frame(['FR_WUPIS_MAIN', 'MAIN', 'leftFrame'])
        self.web.click('/html/body/div/div/div/ul/li[1]/div/div/div/div/a')
        self.driver.quit()

    def get_student_info(self):
        self.web.frame(['FR_WUPIS_MAIN', 'MAIN', 'MBODY'])
        col, _ = self.web.extract_table('//*[@id="container"]/div/div/div/div/div/div/table', 'th')
        data, _ = self.web.extract_table('//*[@id="container"]/div/div/div/div/div/div/table', 'td')
        df = pd.DataFrame([data], columns=col)
        return df
    
    def get_subject_info(self):
        self.web.frame(['FR_WUPIS_MAIN', 'MAIN', 'MBODY'])
        col, _ = self.web.extract_table('//*[@id="getApplyAbsence"]/table/tbody/tr[1]', 'th')
        data, tr = self.web.extract_table('//*[@id="getApplyAbsence"]/table/tbody', 'tr')
        data = [
            self.web.extract_table(f'//*[@id="getApplyAbsence"]/table/tbody/tr[{i + 1}]', 'td')[0]
            for i in range(len(tr))
        ]
        df = pd.DataFrame(data, columns=col)
        df = df.drop(columns=[''])
        df = df.dropna()
        df = df.reset_index(drop=True)
        return df

