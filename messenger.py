import csv
import os
import log
import Class
import configparser


config = configparser.ConfigParser()
config.read('config.ini')
first_running = config.getboolean('first', 'first_running')
debug_mode = config.getboolean('debug', 'debug_mode')

def read_log():
    if first_running:
        obj = Class.FallLog()
        obj.set_content('first running')
        if log.add_log(obj) and not debug_mode:
            config.set('first', 'first_running', 'False')
            config.write(open('config.ini', 'w'))


if __name__ == "__main__":
    read_log()