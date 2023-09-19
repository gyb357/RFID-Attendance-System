import pymysql


class DataBase():
    def __init__(self, host, port, user, password, db, charset):
        self.db = pymysql.connect(
            host = host,
            port = port,
            user = user,
            password = password,
            db = db,
            charset = charset
        )
        self.cursor = self.db.cursor()

