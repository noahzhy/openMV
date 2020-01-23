import Class
import configparser
import db
import requests
import sqlite3


config = configparser.ConfigParser()
config.read('config.ini')
first_running = config.getboolean('first', 'first_running')
debug_mode = config.getboolean('debug', 'debug_mode')
db_log = config.get('db', 'db_log')

def read_log():
    if first_running or debug_mode:
        # if not debug_mode:
        obj = Class.FallLog()
        obj.set_log('first running')
        obj.set_position('messenger first running')
        db.add_log(obj)
        config.set('first', 'first_running', 'False')
        config.write(open('config.ini', 'w'))

    try:
        conn = sqlite3.connect(db_log)
        cursor = conn.cursor()
        values = cursor.execute('select * from log where status=?', (0,)).fetchall()

        for v in values:
            post_log(conn, v)

        conn.commit()
        cursor.close()
        conn.close()
        
    except Exception as e:
        # 数据库连接，操作异常
        print(e)
        pass

    return True


def post_log(conn, v):
    cursor = conn.cursor()
    timestamp, log, status, position = v
    cursor.execute("UPDATE log SET status = 1 WHERE timestamp = '{}'".format(timestamp))
    return True


if __name__ == "__main__":
    read_log()