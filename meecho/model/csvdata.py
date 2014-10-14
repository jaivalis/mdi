import csv
import time


class CsvData():
    def __init__(self):
        self.data = []
        with open('dummy_data.csv', 'rb') as f:
            reader = csv.reader(f)

            tags = []
            for row in reader:
                if not tags:
                    tags = row
                    continue
                if not row:
                    continue
                # row is a list of strings
                # use string.join to put them together
                tmp = {}
                for i, _e in enumerate(row):
                    e = _e.strip()
                    item = time.strptime(e, "%a %d %b %Y %H:%M:%S") if i == 1 else e

                    tmp[tags[i]] = item
                self.data.append(tmp)

    def get_data(self):
        return self.data