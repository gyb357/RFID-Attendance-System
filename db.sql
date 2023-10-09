# 데이터 베이스 출력
SHOW DATABASES;

# 데이터 베이스 생성
DROP DATABASE IF exists mydb;
CREATE DATABASE IF NOT EXISTS mydb;

# 데이터 베이스 사용
USE mydb;

# 사용자 정보 테이블
DROP TABLE IF EXISTS user_info;
CREATE TABLE IF NOT EXISTS user_info (
	# 사용자를 구분하기 위한 인덱스
	인덱스 INT PRIMARY KEY AUTO_INCREMENT,
	# 원광대학교 웹정보서비스
	아이디 VARCHAR(32) NOT NULL,
	비밀번호 VARCHAR(32) NOT NULL,
	# 휴대폰 고유번호
	고유번호 INT NOT NULL
);

# 학생 정보 테이블
DROP TABLE IF EXISTS student_info;
CREATE TABLE IF NOT EXISTS student_info (
	# 부모 테이블로부터 인덱스를 받아 상속을 구현
	인덱스 INT NOT NULL,
	FOREIGN KEY (인덱스) REFERENCES user_info(인덱스),
	# 학생 정보 요소
	학번 INT NOT NULL,
	성명 VARCHAR(32) NOT NULL,
	년도 INT NOT NULL,
	학기 INT NOT NULL
);

# 시간표 정보 테이블
DROP TABLE IF EXISTS timetable_info;
CREATE TABLE IF NOT EXISTS timetable_info (
	# 부모 테이블로부터 인덱스를 받아 상속을 구현
	인덱스 INT NOT NULL,
	FOREIGN KEY (인덱스) REFERENCES user_info(인덱스),
	# 시간표 테이블 요소
	구분 VARCHAR(32) NOT NULL,
	학수번호 INT NOT NULL,
	교과목명 VARCHAR(32) NOT NULL,
	분반 INT NOT NULL,
	학점 FLOAT NOT NULL,
	요일교시 VARCHAR(32) NOT NULL,
	담당교수 VARCHAR(32) NOT NULL,
	수강인원 INT NOT NULL,
	강의방식 VARCHAR(32) NOT NULL,
	강의실 VARCHAR(32) NOT NULL
);

# 사용자 추가
INSERT INTO user_info (아이디, 비밀번호, 고유번호) VALUES ('아이디', '비밀번호', 0);
SELECT * FROM user_info;

# 테이블 출력
SHOW TABLES;
DESC user_info;
DESC student_info;
DESC time_table;