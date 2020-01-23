from datetime import datetime


class FallLog:
    def __init__(self):
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        self.log = 'fall detected'
        self.status = 0
        self.position = 'class falllog create'

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
        d = "'{}', '{}', {}, '{}'".format(self.timestamp, self.log, self.status, self.position)
        return d

    def get_log(self):
        return self.log

    def get_address():
        return '11 street'


if __name__ == "__main__":
    obj = FallLog()
    obj.set_log('login fall')
    print(obj.get_data())
    # print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))