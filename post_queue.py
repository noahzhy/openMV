import os
import csv
import Class


def add_queue(obj=Class.FallLog()):
    queue_file_name = 'post_queue.csv'
    file_path = os.path.join(os.getcwd(), queue_file_name)
    header = ['timestamp', 'content', 'post_status', 'address']
    if not os.path.isfile(file_path):
        with open(file_path, 'w+', newline='') as f:
            write = csv.writer(f)
            write.writerow(header)

    with open(file_path, 'a+', newline='') as f:
        write = csv.DictWriter(f, obj.get_dict().keys())
        write.writerow(obj.get_dict())


if __name__ == "__main__":
    # init_queue()
    # obj = Class.FallLog()
    add_queue()
    # main()
