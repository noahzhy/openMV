from datetime import datetime


class FallLog:
    def __init__(self):
        self.address = get_address()
        self.content = get_content()
        self.post_status = False
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def get_dict(self):
        dict = {
            'timestamp': self.timestamp,
            'content': self.content,
            'post_status': self.post_status,
            'address': self.address,
        }
        return dict


def get_address():
    return '11 street'


def get_content():
    return 'fall detected'


if __name__ == "__main__":
    obj = FallLog()
    print(obj.get_dict())
    # print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))