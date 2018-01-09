from config.dbconfig import conn

class CashDAO:
    def __init__(self):
        self.conn = conn

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





