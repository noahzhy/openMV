import os
import csv
import Class
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

def add_log(obj=Class.FallLog()):
    log_file_name = config.get('log', 'log_file_name')
    file_path = os.path.join(os.getcwd(), log_file_name)
    header = ['timestamp', 'content', 'post_status', 'address']
    if not os.path.isfile(file_path):
        with open(file_path, 'w+', newline='') as f:
            write = csv.writer(f)
            write.writerow(header)

    with open(file_path, 'a+', newline='') as f:
        write = csv.DictWriter(f, obj.get_dict().keys())
        write.writerow(obj.get_dict())

    return True


if __name__ == "__main__":
    # obj = Class.FallLog()
    add_log()
