from abc import ABCMeta, abstractmethod, abstractproperty


class BaseModel(object):
    __metaclass__ = ABCMeta

    def __init__(self, db, api_list):
        self.db = db
        self.api_list = api_list

    @abstractmethod
    def update_scores(self):
        raise NotImplementedError()

    def update_counts_db(self):
        """ Simply updates the database to the most recent view counts """
        for a in self.api_list:
            table_name = a.__class__.__name__

            # self.db.get_cursor(table_name)