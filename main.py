from sql import SQLManager
from web import WebAutomation
import pandas as pd


sql = SQLManager(
    host = 'rldjqdus05.cafe24.com',
    port = 3306,
    user = 'rldjqdus05',
    password = 'q1w2e3r4!',
    db = 'rldjqdus05',
    charset = 'utf8'
)


monitoring = sql.monitoring(table='user_info', dt=0.5)


while True:
    user_info = next(monitoring)
    
    if user_info is not None:
        web = WebAutomation(visible=False)
        id = user_info[0][1]
        pw = user_info[0][2]

        login = web.login(
            url = 'https://intra.wku.ac.kr/WEB/SWupis/',
            frame = ['FR_WUPIS_MAIN'],
            keys = ['//*[@id="userid"]', '//*[@id="passwd"]'],
            id = id,
            pw = pw,
            click = '//*[@id="f_login"]/fieldset/dl/dd[3]/input'
        )
        if login == False:
            sql.delete_row('user_info', 'user_id', id, 'user_id')
        else:
            dupe = sql.is_duplicated('user_info', 'user_id', id)
            print(dupe, type(dupe))
            
            if dupe >= 2:
                sql.delete_row('user_info', 'user_id', id, 'idx')

