from data_base import DataBase
from web_scraper import WebScraper
import pandas as pd
import re
import utils


db_info = dict(
    host = 'rldjqdus05.cafe24.com',
    port = 3306,
    user = 'rldjqdus05',
    password = 'q1w2e3r4!',
    db = 'rldjqdus05',
    charset = 'utf8'
)
db = DataBase(
    host = db_info['host'],
    port = db_info['port'],
    user = db_info['user'],
    password = db_info['password'],
    db = db_info['db'],
    charset = db_info['charset']
)
#db.check_new_userinfo()


web_info = dict(
    id = 'gyb8592',
    pw = '794613852a@',
)
web = WebScraper(
    id = web_info['id'],
    pw = web_info['pw']
)
student_info, subject_info = web()
#print(student_info)
#print(subject_info)


timetable_info = []
result = []
currents = []


name = subject_info.iloc[:, 0]
time = subject_info.iloc[:, 5]
for input_str in time:
    for char in input_str:
        if re.match("[가-힣]", char):
            current = [char]
            if current:
                result.append(current)
        elif char.isdigit():
            current.append(int(char))

    timetable_info.append(result)
    result = []

timetable_info = pd.DataFrame([timetable_info], columns=name)


def remove_brackets(col):
    tmp = []
    for i in col:
        cleaned_text = re.sub(r'\([^)]*\)', '', i)
        tmp.append(cleaned_text.strip())
    return tmp


col = timetable_info.columns.tolist()
col = remove_brackets(col)
print(col)

query = '''DROP TABLE IF EXISTS timetable_info;'''
db.execute(query)


query = '''
CREATE TABLE IF NOT EXISTS timetable_info(
	인덱스 INT NOT NULL,
	FOREIGN KEY (인덱스) REFERENCES user_info(인덱스)
);
'''
db.execute(query)


# 컬럼 생성 이전 중복 체크를 위한 리스트 선언
query = '''DESC timetable_info;'''
db.execute(query)
columns = db.fetchall()
tmp = []
for i in columns:
    tmp.append(i[0])
print(tmp)


def operator_len(idx, arr, a, b):
    return utils.operator(idx == len(arr)-1, a, b)


# 컬럼 생성
for i in col:
    if i not in tmp:
        query = f'''ALTER TABLE timetable_info ADD COLUMN {i} VARCHAR(32);'''
        db.execute(query)


query = '''INSERT INTO timetable_info (인덱스, '''
for i in range(len(col)):
    query += (f'''{col[i]}''' + operator_len(i, col, '', ', '))

query += (f''') VALUES ({1}, ''')
for i in range(len(time)):
    query += (f'''{"'"+str(time[i])+"'"}''' + operator_len(i, time, '', ', '))

query += ''');'''
print(query)
db.execute(query)


# query = '''INSERT INTO timetable_info (인덱스, 컴퓨터네트워크, 데이터베이스, 영상처리, 정보보안, 스마트디바이스, 기업연계프로젝트1, 빅데이터) 
# VALUES (1, '화3목56', '월2화12', '수7목78', '수89금2', '목34금1', '금34', '화56수1');'''
# db.execute(query)


query = '''DESC timetable_info;'''
db.execute(query)
result = db.fetchall()
print(result)
