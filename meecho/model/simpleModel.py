from model import BaseModel


class SimpleModel(BaseModel):  # TODO name ?

    def __init__(self, *args, **kwargs):
        super(SimpleModel, self).__init__(*args, **kwargs)

    def update_scores(self):
        pass

    def update_counts_db(self):
        """ Simply updates the database to the most recent view counts """
        super(SimpleModel, self).update_counts_db()
