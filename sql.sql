# 데이터 베이스 출력
SHOW DATABASES;

# 데이터 베이스 생성
DROP DATABASE IF exists rldjqdus05;
CREATE DATABASE IF NOT EXISTS rldjqdus05;

# 데이터 베이스 사용
USE rldjqdus05;

# 사용자 정보 테이블
DROP TABLE IF EXISTS user_info;
CREATE TABLE IF NOT EXISTS user_info (
	idx INT PRIMARY KEY AUTO_INCREMENT,	# 외래키
	user_id VARCHAR(32) NOT NULL,		# 웹정보서비스 아이디
	user_pw VARCHAR(32) NOT NULL,		# 웹정보서비스 비밀번호
	user_phone VARCHAR(32) NOT NULL,	# 휴대폰 번호
    user_status VARCHAR(32) NOT NULL	# 상태 정보
);

# 학생 정보 테이블
DROP TABLE IF EXISTS student_info;
CREATE TABLE IF NOT EXISTS student_info (
	idx INT NOT NULL,							# 외래키
    student_college VARCHAR(32) NOT NULL,		# 대학명
    student_department VARCHAR(32) NOT NULL,	# 학과
    student_id VARCHAR(32) NOT NULL,			# 학번
    student_grade VARCHAR(32) NOT NULL,			# 학년
    student_name VARCHAR(32) NOT NULL,			# 이름
    FOREIGN KEY (idx) REFERENCES user_info(idx)
);

# 시간표 정보 테이블
DROP TABLE IF EXISTS timetable_info;
CREATE TABLE IF NOT EXISTS timetable_info (
	idx INT NOT NULL,			# 외래키
	mon VARCHAR(32) NOT NULL,	# 월요일
    tue VARCHAR(32) NOT NULL,	# 화요일
    wen VARCHAR(32) NOT NULL,	# 수요일
    thu VARCHAR(32) NOT NULL,	# 목요일
    fri VARCHAR(32) NOT NULL,	# 금요일
    FOREIGN KEY (idx) REFERENCES user_info(idx)
);

# 테이블 확인
SHOW TABLES;

# 테이블 컬럼 확인
DESC user_info;
DESC student_info;
DESC timetable_info;

# 테이블 내용 확인
SELECT * FROM user_info;
SELECT * FROM student_info;
SELECT * FROM timetable_info;

