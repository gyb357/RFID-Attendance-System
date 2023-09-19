from web_driver import WebDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

# 웹 드라이버
web = WebDriverManager(visible=False)
driver = web.driver

# 아이디, 비밀번호
id = input("아이디: ")
pw = input("비밀번호: ")
web.connect('https://intra.wku.ac.kr/WEB/SWupis/')
web.frame(['FR_WUPIS_MAIN'])
web.send_keys('//*[@id="userid"]', id, "아이디")
web.send_keys('//*[@id="passwd"]', pw, "비밀번호")
web.click('//*[@id="f_login"]/fieldset/dl/dd[3]/input', "로그인")
web.alert_handler()

# 정보서비스 클릭
web.frame(['FR_WUPIS_MAIN', 'MAIN', 'topFrame'])
web.click('/html/body/table/tbody/tr/td[2]/a', "정보서비스")

# 수강신청조회 클릭
web.frame(['FR_WUPIS_MAIN', 'MAIN', 'leftFrame'])
web.click('/html/body/div/div/div/ul/li[5]/div[2]/ul/li[20]/a', "수강신청조회")

# 학생 정보
web.frame(['FR_WUPIS_MAIN', 'MAIN', 'MBODY'])
_, student = web.extract_table('/html/body/form/table[1]/tbody/tr', 'td')

# 시간표 정보
_, column = web.extract_table('/html/body/form/table[2]/tbody/tr[2]', 'th')
tr, _ = web.extract_table('/html/body/form/table[2]/tbody', 'tr')
timetable = []
for i in tr[2:]:
    temp = []
    td = i.find_elements(By.TAG_NAME, 'td')
    for j in td:
        temp.append(j.text)

    timetable.append(temp)

# 학생 정보 전처리
df1 = pd.DataFrame([student[i:i + 2] for i in range(0, len(student), 2)]).T
df1.columns = df1.iloc[0]
df1         = df1[1:]
print("학생 정보")
print(df1)
print()

# 시간표 정보 전처리
data2 = [column]
for i in timetable:
    data2.append(i)

df2 = pd.DataFrame(data2[1:], columns=data2[0])
df2 = df2.drop(columns=['재수강', '시험방법'])
df2 = df2.drop(7)
print("시간표 정보")
print(df2)
print()

