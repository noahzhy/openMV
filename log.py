import os
import sqlite3
import Class
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

def add_log(obj=Class.FallLog()):
    log_file_name = config.get('db', 'db_log')
    conn = sqlite3.connect(log_file_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE log(
                    timestamp text, 
                    log text, 
                    status integer, 
                    address text)''')

    # header = ['timestamp', 'content', 'status', 'address']
    c.execute("INSERT INTO log VALUES ({})".format(obj.get_data()))
    conn.commit()
    conn.close()

    return True


if __name__ == "__main__":
    # obj = Class.FallLog()
    add_log()
