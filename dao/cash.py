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

    def insertCash(self, rid):
        cursor = self.conn.cursor()
        query = "insert into payment(rid) values (%s) returning payid;"
        cursor.execute(query, (rid,))
        payid = cursor.fetchone()[0]
        query = "insert into cash(cashid) values (%s) returning cashid;"
        cursor.execute(query, (payid,))
        cashid = cursor.fetchone()[0]
        self.conn.commit()
        return cashid

    def deleteCash(self, cashid):
        cursor = self.conn.cursor()
        query = "delete from Cash where cashid = %s;"
        cursor.execute(query, (cashid,))
        query = "delete from Payment where payid = %s;"
        cursor.execute(query, (cashid,))
        self.conn.commit()
        return





