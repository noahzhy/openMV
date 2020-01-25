import os
import db
import utils
import requests
from Class import *
import messenger as msg

config = Config()

def check_version():
    sess = requests.Session()
    try:
        r = sess.get(url=config.api_version)
        if r.status_code == 200:
            server_version = r.text
            if utils.find_new_version(config.version, server_version):
                # print('find new version')
                obj = Log()
                obj.set_log('find new version')
                obj.set_position('OTA check version')
                db.add_log(obj)
                if download_files():
                    msg.load_log()
                
        else:
            print('internet connect error')
    except Exception as e:
        print(e)
        pass


def download_files():
    return True


def OTA_start():
    check_version()


if __name__ == "__main__":
    OTA_start()