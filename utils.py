def find_new_version(current_version, server_version):
    return True if current_version < server_version else False


def ensure_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


if __name__ == "__main__":
    server_version = '2.1.20'
    a = '2.1.20'
    res = find_new_version(a, server_version)
    print(res)