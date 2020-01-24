import os
import sqlite3
from Class import *


config = Config()

def add_log(obj=Log()):
    conn = sqlite3.connect(config.db_log)
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
