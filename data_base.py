import pymysql
import time


class DataBase():
    def __init__(self, host, port, user, password, db, charset):
        self.db = pymysql.connect(
            host = host,
            port = port,
            user = user,
            password = password,
            db = db,
            charset = charset,
            autocommit = True
        )
        self.cursor = self.db.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)

    def fetchall(self):
        return self.cursor.fetchall()
