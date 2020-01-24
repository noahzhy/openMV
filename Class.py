import configparser
from datetime import datetime


config = configparser.ConfigParser()
config.read('config.ini')

class Log:
    def __init__(self):
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        self.log = 'fall detected'
        self.status = 0
        self.position = 'class Log create'

    def set_log(self, log):
        self.log = log
        return True

    def set_position(self, position):
        self.position = position
        return True

    def get_data(self):
        # dict = {
        #     'timestamp': self.timestamp,
        #     'log': self.log,
        #     'status': self.status,
        #     'address': self.address,
        # }
        d = (self.timestamp, self.log, self.status, self.position)
        return d

    def get_log(self):
        return self.log

    def get_address():
        return '11 street'


class Config:
    def __init__(self):
        pass

    def get_db_log(self):
        return config.get('DB', 'db_log')

    def set_db_log(self, new_db_log_name):
        config.set('DB', 'db_log', new_db_log_name)
        config.write(open('config.ini', 'w'))
        return new_db_log_name

    def get_debug_mode(self):
        return config.getboolean('DEBUG', 'debug_mode')

    def set_debug_mode(self, new_debug_mode):
        config.set('DEBUG', 'debug_mode', new_debug_mode)
        config.write(open('config.ini', 'w'))
        return new_debug_mode

    def get_api_status(self):
        return config.get('API', 'api_status')

    def set_api_status(self, new_api_status):
        config.set('API', 'api_status', new_api_status)
        config.write(open('config.ini', 'w'))
        return new_api_status

    def get_first_running(self):
        return config.get('DEFAULT', 'first_running')

    def set_first_running(self, new_first_running):
        config.set('DEFAULT', 'first_running', new_first_running)
        config.write(open('config.ini', 'w'))
        return new_first_running

    db_log = property(get_db_log, set_db_log)
    debug_mode = property(get_debug_mode, set_debug_mode)
    api_status = property(get_api_status, set_api_status)
    first_running = property(get_first_running, set_first_running)


if __name__ == "__main__":
    obj = Log()
    print(obj.get_data())
    cfg = Config()
    print(cfg.first_running)

    # print(g)
    # print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))