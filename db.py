import os
import sqlite3
import Class
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
db_log = config.get('DB', 'db_log')

def add_log(obj=Class.Log()):
    conn = sqlite3.connect(db_log)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS log (
        timestamp TEXT,
        log       TEXT,
        status    INTEGER,
        position  TEXT
    )''')

    # header = ['timestamp', 'content', 'status', 'position']
    c.execute("INSERT INTO log VALUES (?,?,?,?)", obj.get_data())
    conn.commit()
    conn.close()

    return True


if __name__ == "__main__":
    # obj = Class.Log()
    add_log()
