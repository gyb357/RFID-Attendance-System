from color import Colors
import pymysql
from pymysql import err
import time
from utils import operator


class SQL(Colors):
    def __init__(self, host, port, user, password, db, charset):
        super().__init__()
        self.sql = self.connect(host, port, user, password, db, charset)
        self.cur = self.sql.cursor()
        
    def connect(self, host, port, user, password, db, charset):
        try:
            connect = pymysql.connect(
                host = host,
                port = port,
                user = user,
                password = password,
                db = db,
                charset = charset,
                autocommit = True
            )
            self.print('green', f'connect(): {host}')
            return connect
        except err.OperationalError as e:
            self.print('red', f'connect(): {host}', e)
            raise


class SQLManager(SQL):
    def __init__(self, host, port, user, password, db, charset):
        super().__init__(host, port, user, password, db, charset)

    def monitoring(self, table, dt):
        try:
            prev = self.row_count(table)
            while True:
                current = self.row_count(table)

                if current > prev:
                    idx = current - prev
                    row = self.row_data(table, prev, idx)
                    self.print('magenta', f'    monitoring(): {row}')
                    yield row
                
                prev = current
                time.sleep(dt)
        finally:
            self.sql.close()
    
    def row_count(self, table):
        self.cur.execute(f'SELECT COUNT(*) FROM {table}')
        return self.cur.fetchone()[0]
    
    def row_data(self, table, prev, idx):
        self.cur.execute(f'SELECT * FROM {table} LIMIT {prev}, {idx}')
        return self.cur.fetchall()
    
    def is_duplicated(self, table, col, var):
        self.cur.execute(f"SELECT {col}, COUNT({col}) as count FROM {table} WHERE {col} = '{var}' HAVING count > 1;")
        result = self.cur.fetchone()
        
        if result is None:
            return 0
        else:
            return result[1]
    
    def delete_row(self, table, col, var, order):
        self.cur.execute(f"DELETE FROM {table} WHERE {col} = '{var}' ORDER BY {order} DESC LIMIT 1;")

