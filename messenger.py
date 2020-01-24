from Class import *
import db
import requests
import sqlite3


config = Config()

def load_log():
    if config.first_running=='True' or config.debug_mode:
        # if not debug_mode:
        obj = Log()
        obj.set_log('first running')
        obj.set_position('messenger first running')
        db.add_log(obj)
        config.first_running = 'False'

    try:
        conn = sqlite3.connect(config.db_log)
        cursor = conn.cursor()
        values = cursor.execute('select * from log where status=?', (0,)).fetchall()

        for v in values:
            if post_log(v):
                timestamp = v[0]
                # print(timestamp)
                cursor.execute("UPDATE log SET status = 1 WHERE timestamp = '{}'".format(timestamp))
                conn.commit()

        cursor.close()
        conn.close()
        
    except Exception as e:
        # 数据库连接，操作异常
        print(e)
        pass

    return True


def post_log(v):
    sess = requests.Session()
    url = config.api_status
    data = {

    }
    # sess.post(url=url, data=data)
    return True


if __name__ == "__main__":
    load_log()