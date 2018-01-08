from config.dbconfig import pg_config
import psycopg2

class CashDAO:
    def __init__(self):

        connection_url = "dbname=%s host=%s port=%s user=%s password=%s sslmode=%s" % (
        pg_config['dbname'], pg_config['host'],
        pg_config['port'], pg_config['user'],
        pg_config['password'], pg_config['sslmode'])

        self.conn = psycopg2._connect(connection_url)

    def getAllCashes(self):
        cursor = self.conn.cursor()
        query = "Select cashid from Cash;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCashById(self, cashid):
        cursor = self.conn.cursor()
        query = "Select cashid from Cash where cashid = %s;"
        cursor.execute(query, (cashid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCashesByTransaction(self, tid):
        cursor = self.conn.cursor()
        query = "Select cashid from (Cash inner join payment on payid = cashid) natural inner join order_info natural inner join transaction where tid = %s;"
        cursor.execute(query, (tid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCashesByRequester(self, rid):
        cursor = self.conn.cursor()
        query = "Select cashid from (Cash inner join payment on payid = cashid) natural inner join requester where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCashesByOrder(self, oid):
        cursor = self.conn.cursor()
        query = "Select cashid from (Cash inner join payment on payid = cashid) natural inner join order_info where oid = %s;"
        cursor.execute(query, (oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result





