import MySQLdb

DB_HOST = 'localhost'
DB_USERNAME = ''
DB_PWD = ''
DB_NAME = ''


class DB:
    conn = None

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

    def get_cursor(self, api_name):
        """
        Return a cursor to the table containing the entries of a given api.
        :param api_name: Name of api's table requested
        :return: mysql cursor
        """
        return None