import csv


def csvDictReader(path):
    with open(path) as rf:
        reader = csv.DictReader(rf)
        items = list(reader)
    return items