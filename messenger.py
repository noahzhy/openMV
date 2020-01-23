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
        obj = Class.FallLog()
        obj.set_log('first running')
        obj.set_position('messenger first running')
        db.add_log(obj)
        if not debug_mode:
            config.set('first', 'first_running', 'False')
            config.write(open('config.ini', 'w'))

    conn = sqlite3.connect(db_log)
    cursor = conn.cursor()
    cursor.execute('select * from log where status=?', (0,))
    values = cursor.fetchall()

    for v in values:
        post_log(v)

    cursor.close()
    conn.close()

    return True


def post_log(v):
    timestamp, log, status, position = v
    print(timestamp)
    conn = sqlite3.connect(db_log)
    cursor = conn.cursor()
    cursor.execute("UPDATE log SET status = 1 WHERE timestamp = '{}'".format(timestamp))
    # print(log_dict)
    return True


if __name__ == "__main__":
    read_log()