import pymysql
from com.settings import db_params

class DBConnectionManager:

    @staticmethod
    def getDicCursor(conn):
        return conn.cursor(pymysql.cursors.DictCursor)

    @staticmethod
    def getConnection(autocommit=True):
        host = 'localhost'
        conn = pymysql.connect(host=host, port=db_params['port'], user=db_params['username'], passwd=db_params['password'], db=db_params['dbname'],autocommit=autocommit,charset='utf8')
        return conn

    @staticmethod
    def add_row(cursor, tablename, rowdict):
        try:
            cursor.execute("describe %s" % tablename)
            allowed_keys = set(row[0] for row in cursor.fetchall())
            keys = allowed_keys.intersection(rowdict)
            columns = ", ".join(keys)
            values_template = ", ".join(["%s"] * len(keys))
            sql = "insert into %s (%s) values (%s)" % (tablename, columns, values_template)
            values = tuple(rowdict[key] for key in keys)
            cursor.execute(sql, values)
        except Exception as e:
            raise

