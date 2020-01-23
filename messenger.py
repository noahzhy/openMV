import csv
import os
import log
import Class
import configparser
import utils


config = configparser.ConfigParser()
config.read('config.ini')
first_running = config.getboolean('first', 'first_running')
debug_mode = config.getboolean('debug', 'debug_mode')
log_file_name = config.get('log', 'log_file_name')
file_path = os.path.join(os.getcwd(), log_file_name)

def read_log():
    # false_status_logs = []
    if first_running:
        obj = Class.FallLog()
        obj.set_content('first running')
        if log.add_log(obj) and not debug_mode:
            config.set('first', 'first_running', 'False')
            config.write(open('config.ini', 'w'))


    # 初始化行数计数器, 默认包含 header
    counter = 1
    items = utils.csvDictReader(file_path)
    for i in items:
        counter += 1
        if i['status'] == 'False':
            if post_log(i):
                i['status'] == 'True'
    # items
                    


    
    # print(false_status_logs)
    return True


def post_log(log_dict):
    print(log_dict)
    return True


if __name__ == "__main__":
    read_log()