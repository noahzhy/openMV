def find_new_version(a, b='1.2.0'):
    return True if a < b else False


if __name__ == "__main__":
    a = '1.2.0'
    res = find_new_version(a)
    print(res)