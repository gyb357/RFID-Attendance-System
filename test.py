import time

from webdriver import WebDriverManager


# 아이디, 비밀번호
id = ""
pw = ""
web = WebDriverManager(visible=False)

# 로그인
web.connect("https://intra.wku.ac.kr/WEB/SWupis/")
web.frame(['FR_WUPIS_MAIN'])
web.send_keys('//*[@id="userid"]', id, "아이디")
web.send_keys('//*[@id="passwd"]', pw, "비밀번호")
web.click('//*[@id="f_login"]/fieldset/dl/dd[3]/input', "로그인")
web.alert_handler()

# 정보서비스 클릭
web.frame(["FR_WUPIS_MAIN", "MAIN", "topFrame"])
web.click('/html/body/table/tbody/tr/td[2]/a', "정보서비스")

# 수강신청조회 클릭
web.frame(["FR_WUPIS_MAIN", "MAIN", "leftFrame"])
web.click('/html/body/div/div/div/ul/li[5]/div[2]/ul/li[20]/a', "수강신청조회")

# 학생 정보 얻기
web.frame(["FR_WUPIS_MAIN", "MAIN", "MBODY"])


time.sleep(1000)

