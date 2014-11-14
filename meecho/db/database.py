import MySQLdb

DB_HOST = 'localhost'
DB_USERNAME = 'root'
DB_PWD = 'fifty50'
DB_NAME = 'mdi'


class DB:
    conn = None
    insert_bet = ("INSERT INTO bets "
                  "(id, user_id, video_id, current_views_count, current_subscribers_count, created_at, updated_at) "
                  "VALUES "
                  "(NULL, %(user_id)s, %(video_id)s, %(current_views_count)s, "
                  "%(current_subscribers_count)s, %(created_at)s, %(created_at)s)")

    def __init__(self):
        self._connect()

    def _connect(self):
        try:
            self.conn = MySQLdb.connect(host=DB_HOST,
                                        user=DB_USERNAME,
                                        passwd=DB_PWD,
                                        db=DB_NAME)
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

    def query(self, sql, params):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, params)
        except (AttributeError, MySQLdb.OperationalError), e:
            print 'exception generated during sql connection: ', e
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, params)
        cursor.close()
        return cursor

    def close(self):
        try:
            if self.conn:
                self.conn.close()
                print 'Closed Database Connection: ' + self.conn
            else:
                print 'No Database Connection to Close.'
        except (AttributeError, MySQLdb.OperationalError), e:
            raise e

    def get_bets_cursor(self):
        """ Return a cursor to the `bets` table.
        :return: mysql cursor
        """
        return None

    def insert_bets(self, bets):
        """ INSERTS to the bets table
        :param bets: tuple containing the bets
        """
        cursor = self.conn.cursor()
        for bet in bets:
            cursor.execute(DB.insert_bet, bet)
            pass
        self.conn.commit()
        cursor.close()


def main():
    db = DB()

if __name__ == '__main__':
    main()