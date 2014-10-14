from csvdata import CsvData


class DummyDM:
    def __init__(self):
        data_store = CsvData()
        self.data = data_store.get_data()
        print self.data

    def update_scores(self):
        pass

    def update_counts_db(self):
        """ Simply updates the database to the most recent view counts """
        pass

    def simulate(self, hours):
        pass

