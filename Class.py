from datetime import datetime


class FallLog:
    def __init__(self):
        self.address = get_address()
        self.content = 'fall detected'
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

    def get_content(self):
        return self.content

    def set_content(self, content):
        self.content = content
        return True


def get_address():
    return '11 street'


if __name__ == "__main__":
    obj = FallLog()
    obj.set_content('login fall')
    print(obj.get_dict())
    # print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))