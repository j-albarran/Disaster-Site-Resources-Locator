from config.dbconfig import conn
import psycopg2


class TransactionDAO:
    def __init__(self):
        self.conn = conn

    def getTransactionById(self, tid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tid = %s"
        cursor.execute(query, (tid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactions(self):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tprice = %s and tqty = %s and tdate = %s and tstatus = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPriceQtyDate(self, tprice, tqty, tdate):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tprice = %s and tqty = %s and tdate = %s;"
        cursor.execute(query, (tprice, tqty, tdate))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPriceQtyStatus(self, tprice, tqty, tstatus):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tprice = %s and tqty = %s and tstatus = %s;"
        cursor.execute(query, (tprice, tqty, tstatus))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPriceDateStatus(self, tprice, tdate, tstatus):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tprice = %s and tdate = %s and tstatus = %s;"
        cursor.execute(query, (tprice, tdate, tstatus))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByQtyDateStatus(self, tqty, tdate, tstatus):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tqty = %s and tdate = %s and tstatus = %s;"
        cursor.execute(query, (tqty, tdate, tstatus))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPriceQty(self, tprice, tqty):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tprice = %s and tqty = %s;"
        cursor.execute(query, (tprice, tqty))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPriceDate(self, tprice, tdate):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tprice = %s and tdate = %s;"
        cursor.execute(query, (tprice, tdate))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPriceStatus(self, tprice, tstatus):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tprice = %s and tstatus = %s;"
        cursor.execute(query, (tprice, tstatus))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByQtyDate(self, tqty, tdate):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tqty = %s and tdate = %s;"
        cursor.execute(query, (tqty, tdate))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByQtyStatus(self, tqty, tstatus):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tqty = %s and tstatus = %s;"
        cursor.execute(query, (tqty, tstatus))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByDateStatus(self, tdate, tstatus):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tdate = %s and tstatus = %s;"
        cursor.execute(query, (tdate, tstatus))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPrice(self, tprice):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tprice = %s;"
        cursor.execute(query, (tprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByQty(self, tqty):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tqty = %s;"
        cursor.execute(query, (tqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByDate(self, tdate):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tdate = %s;"
        cursor.execute(query, (tdate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByStatus(self, tstatus):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction where tstatus = %s;"
        cursor.execute(query, (tstatus,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegion(self, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionPriceQtyDate(self, tprice, tqty, tdate, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionPriceQtyStatus(self, tprice, tqty, tstatus, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionPriceDateStatus(self, tprice, tdate, tstatus, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionQtyDateStatus(self, tqty, tdate, tstatus, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionPriceQty(self, tprice, tqty, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s;"
        cursor.execute(query, (tprice, tqty, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionPriceDate(self, tprice, tdate, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s;"
        cursor.execute(query, (tprice, tdate, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionPriceStatus(self, tprice, tstatus, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s;"
        cursor.execute(query, (tprice, tstatus, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionQtyDate(self, tqty, tdate, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s;"
        cursor.execute(query, (tqty, tdate, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionQtyStatus(self, tqty, tstatus, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s;"
        cursor.execute(query, (tqty, tstatus, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionDateStatus(self, tdate, tstatus, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s;"
        cursor.execute(query, (tdate, tstatus, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionPrice(self, tprice, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s;"
        cursor.execute(query, (tprice, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionQty(self, tqty, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s;"
        cursor.execute(query, (tqty, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionDate(self, tdate, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s;"
        cursor.execute(query, (tdate, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionStatus(self, tstatus, rname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s;"
        cursor.execute(query, (tstatus, rname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCity(self, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s"
        cursor.execute(query, (cname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityPriceQtyDate(self, tprice, tqty, tdate, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityPriceQtyStatus(self, tprice, tqty, tstatus, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityPriceDateStatus(self, tprice, tdate, tstatus, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityQtyDateStatus(self, tqty, tdate, tstatus, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityPriceQty(self, tprice, tqty, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s;"
        cursor.execute(query, (tprice, tqty, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityPriceDate(self, tprice, tdate, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s;"
        cursor.execute(query, (tprice, tdate, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityPriceStatus(self, tprice, tstatus, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s;"
        cursor.execute(query, (tprice, tstatus, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityQtyDate(self, tqty, tdate, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s;"
        cursor.execute(query, (tqty, tdate, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityQtyStatus(self, tqty, tstatus, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s;"
        cursor.execute(query, (tqty, tstatus, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityDateStatus(self, tdate, tstatus, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s;"
        cursor.execute(query, (tdate, tstatus, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityPrice(self, tprice, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s;"
        cursor.execute(query, (tprice, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityQty(self, tqty, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s;"
        cursor.execute(query, (tqty, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityDate(self, tdate, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s;"
        cursor.execute(query, (tdate, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityStatus(self, tstatus, cname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s;"
        cursor.execute(query, (tstatus, cname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplier(self, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierPriceQtyDate(self, tprice, tqty, tdate, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tprice = %s and tqty = %s and tdate = %s and sid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierPriceQtyStatus(self, tprice, tqty, tstatus, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tprice = %s and tqty = %s and tstatus = %s and sid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierPriceDateStatus(self, tprice, tdate, tstatus, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tprice = %s and tdate = %s and tstatus = %s and sid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierQtyDateStatus(self, tqty, tdate, tstatus, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tqty = %s and tdate = %s and tstatus = %s and sid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierPriceQty(self, tprice, tqty, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tprice = %s and tqty = %s and sid = %s;"
        cursor.execute(query, (tprice, tqty, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierPriceDate(self, tprice, tdate, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tprice = %s and tdate = %s and sid = %s;"
        cursor.execute(query, (tprice, tdate, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierPriceStatus(self, tprice, tstatus, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tprice = %s and tstatus = %s and sid = %s;"
        cursor.execute(query, (tprice, tstatus, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierQtyDate(self, tqty, tdate, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tqty = %s and tdate = %s and sid = %s;"
        cursor.execute(query, (tqty, tdate, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierQtyStatus(self, tqty, tstatus, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tqty = %s and tstatus = %s and sid = %s;"
        cursor.execute(query, (tqty, tstatus, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierDateStatus(self, tdate, tstatus, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tdate = %s and tstatus = %s and sid = %s;"
        cursor.execute(query, (tdate, tstatus, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierPrice(self, tprice, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tprice = %s and sid = %s;"
        cursor.execute(query, (tprice, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierQty(self, tqty, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tqty = %s and sid = %s;"
        cursor.execute(query, (tqty, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierDate(self, tdate, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tdate = %s and sid = %s;"
        cursor.execute(query, (tdate, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierStatus(self, tstatus, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier where tstatus = %s and sid = %s;"
        cursor.execute(query, (tstatus, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRequester(self, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterPriceQtyDate(self, tprice, tqty, tdate, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tprice = %s and tqty = %s and tdate = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterPriceQtyStatus(self, tprice, tqty, tstatus, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tprice = %s and tqty = %s and tstatus = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterPriceDateStatus(self, tprice, tdate, tstatus, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tprice = %s and tdate = %s and tstatus = %s and rid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterQtyDateStatus(self, tqty, tdate, tstatus, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tqty = %s and tdate = %s and tstatus = %s and rid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterPriceQty(self, tprice, tqty, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tprice = %s and tqty = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterPriceDate(self, tprice, tdate, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tprice = %s and tdate = %s and rid = %s;"
        cursor.execute(query, (tprice, tdate, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterPriceStatus(self, tprice, tstatus, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tprice = %s and tstatus = %s and rid = %s;"
        cursor.execute(query, (tprice, tstatus, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterQtyDate(self, tqty, tdate, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tqty = %s and tdate = %s and rid = %s;"
        cursor.execute(query, (tqty, tdate, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterQtyStatus(self, tqty, tstatus, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tqty = %s and tstatus = %s and rid = %s;"
        cursor.execute(query, (tqty, tstatus, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterDateStatus(self, tdate, tstatus, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tdate = %s and tstatus = %s and rid = %s;"
        cursor.execute(query, (tdate, tstatus, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterPrice(self, tprice, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tprice = %s and rid = %s;"
        cursor.execute(query, (tprice, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterQty(self, tqty, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tqty = %s and rid = %s;"
        cursor.execute(query, (tqty, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterDate(self, tdate, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tdate = %s and rid = %s;"
        cursor.execute(query, (tdate, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterStatus(self, tstatus, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester where tstatus = %s and rid = %s;"
        cursor.execute(query, (tstatus, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByResource(self, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where rsid = %s;"
        cursor.execute(query, (rsid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourcePriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourcePriceQtyDate(self, tprice, tqty, tdate, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tprice = %s and tqty = %s and tdate = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourcePriceQtyStatus(self, tprice, tqty, tstatus, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tprice = %s and tqty = %s and tstatus = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourcePriceDateStatus(self, tprice, tdate, tstatus, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tprice = %s and tdate = %s and tstatus = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceQtyDateStatus(self, tqty, tdate, tstatus, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tqty = %s and tdate = %s and tstatus = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourcePriceQty(self, tprice, tqty, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tprice = %s and tqty = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourcePriceDate(self, tprice, tdate, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tprice = %s and tdate = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourcePriceStatus(self, tprice, tstatus, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tprice = %s and tstatus = %s and rsid = %s;"
        cursor.execute(query, (tprice, tstatus, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceQtyDate(self, tqty, tdate, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tqty = %s and tdate = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceQtyStatus(self, tqty, tstatus, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tqty = %s and tstatus = %s and rsid = %s;"
        cursor.execute(query, (tqty, tstatus, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceDateStatus(self, tdate, tstatus, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tdate = %s and tstatus = %s and rsid = %s;"
        cursor.execute(query, (tdate, tstatus, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourcePrice(self, tprice, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tprice = %s and rsid = %s;"
        cursor.execute(query, (tprice, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceQty(self, tqty, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tqty = %s and rsid = %s;"
        cursor.execute(query, (tqty, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceDate(self, tdate, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tdate = %s and rsid = %s;"
        cursor.execute(query, (tdate, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceStatus(self, tstatus, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier where tstatus = %s and rsid = %s;"
        cursor.execute(query, (tstatus, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByKeyword(self, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where kid = %s;"
        cursor.execute(query, (kid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordPriceQtyDate(self, tprice, tqty, tdate, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordPriceQtyStatus(self, tprice, tqty, tstatus, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tstatus = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordPriceDateStatus(self, tprice, tdate, tstatus, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and tstatus = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordQtyDateStatus(self, tqty, tdate, tstatus, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and tstatus = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordPriceQty(self, tprice, tqty, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordPriceDate(self, tprice, tdate, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordPriceStatus(self, tprice, tstatus, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tstatus = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordQtyDate(self, tqty, tdate, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordQtyStatus(self, tqty, tstatus, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tstatus = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordDateStatus(self, tdate, tstatus, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and tstatus = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordPrice(self, tprice, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and kid = %s;"
        cursor.execute(query, (tprice, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordQty(self, tqty, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and kid = %s;"
        cursor.execute(query, (tqty, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordDate(self, tdate, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and kid = %s;"
        cursor.execute(query, (tdate, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordStatus(self, tstatus, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword where tstatus = %s and kid = %s;"
        cursor.execute(query, (tstatus, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCategory(self, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryPriceQtyDate(self, tprice, tqty, tdate, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tprice = %s and tqty = %s and tdate = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryPriceQtyStatus(self, tprice, tqty, tstatus, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tprice = %s and tqty = %s and tstatus = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryPriceDateStatus(self, tprice, tdate, tstatus, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tprice = %s and tdate = %s and tstatus = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryQtyDateStatus(self, tqty, tdate, tstatus, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tqty = %s and tdate = %s and tstatus = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryPriceQty(self, tprice, tqty, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tprice = %s and tqty = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryPriceDate(self, tprice, tdate, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tprice = %s and tdate = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryPriceStatus(self, tprice, tstatus, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tprice = %s and tstatus = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryQtyDate(self, tqty, tdate, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tqty = %s and tdate = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryQtyStatus(self, tqty, tstatus, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tqty = %s and tstatus = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryDateStatus(self, tdate, tstatus, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tdate = %s and tstatus = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryPrice(self, tprice, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tprice = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryQty(self, tqty, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tqty = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryDate(self, tdate, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tdate = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryStatus(self, tstatus, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category where tstatus = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByOrder(self, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where oid = %s;"
        cursor.execute(query, (oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderPriceQtyDate(self, tprice, tqty, tdate, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tprice = %s and tqty = %s and tdate = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderPriceQtyStatus(self, tprice, tqty, tstatus, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tprice = %s and tqty = %s and tstatus = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderPriceDateStatus(self, tprice, tdate, tstatus, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tprice = %s and tdate = %s and tstatus = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderQtyDateStatus(self, tqty, tdate, tstatus, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tqty = %s and tdate = %s and tstatus = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderPriceQty(self, tprice, tqty, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tprice = %s and tqty = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderPriceDate(self, tprice, tdate, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tprice = %s and tdate = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderPriceStatus(self, tprice, tstatus, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tprice = %s and tstatus = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderQtyDate(self, tqty, tdate, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tqty = %s and tdate = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderQtyStatus(self, tqty, tstatus, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tqty = %s and tstatus = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderDateStatus(self, tdate, tstatus, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tdate = %s and tstatus = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderPrice(self, tprice, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tprice = %s and oid = %s;"
        cursor.execute(query, (tprice, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderQty(self, tqty, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tqty = %s and oid = %s;"
        cursor.execute(query, (tqty, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderDate(self, tdate, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tdate = %s and oid = %s;"
        cursor.execute(query, (tdate, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByOrderStatus(self, tstatus, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info where tstatus = %s and oid = %s;"
        cursor.execute(query, (tstatus, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCreditCard(self, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where cid = %s;"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardPriceQtyDate(self, tprice, tqty, tdate, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tprice = %s and tqty = %s and tdate = %s and cid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardPriceQtyStatus(self, tprice, tqty, tstatus, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tprice = %s and tqty = %s and tstatus = %s and cid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardPriceDateStatus(self, tprice, tdate, tstatus, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tprice = %s and tdate = %s and tstatus = %s and cid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardQtyDateStatus(self, tqty, tdate, tstatus, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tqty = %s and tdate = %s and tstatus = %s and cid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardPriceQty(self, tprice, tqty, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tprice = %s and tqty = %s and cid = %s;"
        cursor.execute(query, (tprice, tqty, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardPriceDate(self, tprice, tdate, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tprice = %s and tdate = %s and cid = %s;"
        cursor.execute(query, (tprice, tdate, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardPriceStatus(self, tprice, tstatus, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tprice = %s and tstatus = %s and cid = %s;"
        cursor.execute(query, (tprice, tstatus, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardQtyDate(self, tqty, tdate, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tqty = %s and tdate = %s and cid = %s;"
        cursor.execute(query, (tqty, tdate, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardQtyStatus(self, tqty, tstatus, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tqty = %s and tstatus = %s and cid = %s;"
        cursor.execute(query, (tqty, tstatus, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardDateStatus(self, tdate, tstatus, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tdate = %s and tstatus = %s and cid = %s;"
        cursor.execute(query, (tdate, tstatus, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardPrice(self, tprice, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tprice = %s and cid = %s;"
        cursor.execute(query, (tprice, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardQty(self, tqty, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tqty = %s and cid = %s;"
        cursor.execute(query, (tqty, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardDate(self, tdate, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tdate = %s and cid = %s;"
        cursor.execute(query, (tdate, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCreditCardStatus(self, tstatus, cid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from (transaction natural inner join Order_Info natural inner join Payment) inner join Credit_Card on payid = cid where tstatus = %s and cid = %s;"
        cursor.execute(query, (tstatus, cid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByPayment(self, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where payid = %s;"
        cursor.execute(query, (payid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and payid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentPriceQtyDate(self, tprice, tqty, tdate, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tprice = %s and tqty = %s and tdate = %s and payid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentPriceQtyStatus(self, tprice, tqty, tstatus, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tprice = %s and tqty = %s and tstatus = %s and payid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentPriceDateStatus(self, tprice, tdate, tstatus, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tprice = %s and tdate = %s and tstatus = %s and payid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentQtyDateStatus(self, tqty, tdate, tstatus, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tqty = %s and tdate = %s and tstatus = %s and payid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentPriceQty(self, tprice, tqty, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tprice = %s and tqty = %s and payid = %s;"
        cursor.execute(query, (tprice, tqty, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentPriceDate(self, tprice, tdate, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tprice = %s and tdate = %s and payid = %s;"
        cursor.execute(query, (tprice, tdate, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentPriceStatus(self, tprice, tstatus, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tprice = %s and tstatus = %s and payid = %s;"
        cursor.execute(query, (tprice, tstatus, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentQtyDate(self, tqty, tdate, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tqty = %s and tdate = %s and payid = %s;"
        cursor.execute(query, (tqty, tdate, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentQtyStatus(self, tqty, tstatus, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tqty = %s and tstatus = %s and payid = %s;"
        cursor.execute(query, (tqty, tstatus, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentDateStatus(self, tdate, tstatus, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tdate = %s and tstatus = %s and payid = %s;"
        cursor.execute(query, (tdate, tstatus, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentPrice(self, tprice, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tprice = %s and payid = %s;"
        cursor.execute(query, (tprice, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentQty(self, tqty, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tqty = %s and payid = %s;"
        cursor.execute(query, (tqty, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentDate(self, tdate, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tdate = %s and payid = %s;"
        cursor.execute(query, (tdate, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByPaymentStatus(self, tstatus, payid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join Payment where tstatus = %s and payid = %s;"
        cursor.execute(query, (tstatus, payid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionSupplier(self, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and sid = %s;"
        cursor.execute(query, (rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierPriceQtyDate(self, tprice, tqty, tdate, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierPriceQtyStatus(self, tprice, tqty, tstatus, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierPriceDateStatus(self, tprice, tdate, tstatus, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierQtyDateStatus(self, tqty, tdate, tstatus, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierPriceQty(self, tprice, tqty, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tprice, tqty, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierPriceDate(self, tprice, tdate, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tprice, tdate, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierPriceStatus(self, tprice, tstatus, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierQtyDate(self, tqty, tdate, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tqty, tdate, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierQtyStatus(self, tqty, tstatus, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierDateStatus(self, tdate, tstatus, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierPrice(self, tprice, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tprice, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierQty(self, tqty, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tqty, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierDate(self, tdate, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tdate, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierStatus(self, tstatus, rname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and sid = %s;"
        cursor.execute(query, (tstatus, rname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionRequester(self, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and rid = %s"
        cursor.execute(query, (rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterPriceQtyDate(self, tprice, tqty, tdate, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and rid = %s"
        cursor.execute(query, (tprice, tqty, tdate, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterPriceQtyStatus(self, tprice, tqty, tstatus, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and rid = %s"
        cursor.execute(query, (tprice, tqty, tstatus, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterPriceDateStatus(self, tprice, tdate, tstatus, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s"
        cursor.execute(query, (tprice, tdate, tstatus, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterQtyDateStatus(self, tqty, tdate, tstatus, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s"
        cursor.execute(query, (tqty, tdate, tstatus, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterPriceQty(self, tprice, tqty, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and rid = %s"
        cursor.execute(query, (tprice, tqty, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterPriceDate(self, tprice, tdate, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and rid = %s"
        cursor.execute(query, (tprice, tdate, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterPriceStatus(self, tprice, tstatus, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and rid = %s"
        cursor.execute(query, (tprice, tstatus, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterQtyDate(self, tqty, tdate, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and rid = %s"
        cursor.execute(query, (tqty, tdate, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterQtyStatus(self, tqty, tstatus, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and rid = %s"
        cursor.execute(query, (tqty, tstatus, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterDateStatus(self, tdate, tstatus, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and rid = %s"
        cursor.execute(query, (tdate, tstatus, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterPrice(self, tprice, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and rid = %s"
        cursor.execute(query, (tprice, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterQty(self, tqty, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and rid = %s"
        cursor.execute(query, (tqty, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterDate(self, tdate, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and rid = %s"
        cursor.execute(query, (tdate, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterStatus(self, tstatus, rname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and rid = %s"
        cursor.execute(query, (tstatus, rname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionResource(self, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and rsid = %s;"
        cursor.execute(query, (rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourcePriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourcePriceQtyDate(self, tprice, tqty, tdate, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourcePriceQtyStatus(self, tprice, tqty, tstatus, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourcePriceDateStatus(self, tprice, tdate, tstatus, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceQtyDateStatus(self, tqty, tdate, tstatus, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourcePriceQty(self, tprice, tqty, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourcePriceDate(self, tprice, tdate, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourcePriceStatus(self, tprice, tstatus, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceQtyDate(self, tqty, tdate, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceQtyStatus(self, tqty, tstatus, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceDateStatus(self, tdate, tstatus, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourcePrice(self, tprice, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tprice, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceQty(self, tqty, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tqty, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceDate(self, tdate, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tdate, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceStatus(self, tstatus, rname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and rsid = %s;"
        cursor.execute(query, (tstatus, rname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionKeyword(self, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and kid = %s;"
        cursor.execute(query, (rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordPriceQtyDate(self, tprice, tqty, tdate, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordPriceQtyStatus(self, tprice, tqty, tstatus, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordPriceDateStatus(self, tprice, tdate, tstatus, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordQtyDateStatus(self, tqty, tdate, tstatus, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordPriceQty(self, tprice, tqty, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordPriceDate(self, tprice, tdate, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordPriceStatus(self, tprice, tstatus, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordQtyDate(self, tqty, tdate, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordQtyStatus(self, tqty, tstatus, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordDateStatus(self, tdate, tstatus, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordPrice(self, tprice, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tprice, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordQty(self, tqty, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tqty, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordDate(self, tdate, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tdate, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordStatus(self, tstatus, rname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and kid = %s;"
        cursor.execute(query, (tstatus, rname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionCategory(self, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, cat_name,
                                                             cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryPriceQtyDate(self, tprice, tqty, tdate, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryPriceQtyStatus(self, tprice, tqty, tstatus, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryPriceDateStatus(self, tprice, tdate, tstatus, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryQtyDateStatus(self, tqty, tdate, tstatus, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryPriceQty(self, tprice, tqty, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryPriceDate(self, tprice, tdate, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryPriceStatus(self, tprice, tstatus, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryQtyDate(self, tqty, tdate, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryQtyStatus(self, tqty, tstatus, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryDateStatus(self, tdate, tstatus, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryPrice(self, tprice, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryQty(self, tqty, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryDate(self, tdate, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryStatus(self, tstatus, rname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, rname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionOrder(self, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and oid = %s;"
        cursor.execute(query, (rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionOrderPriceQtyDate(self, tprice, tqty, tdate, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionOrderPriceQtyStatus(self, tprice, tqty, tstatus, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionOrderPriceDateStatus(self, tprice, tdate, tstatus, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionOrderQtyDateStatus(self, tqty, tdate, tstatus, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionOrderPriceQty(self, tprice, tqty, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionOrderPriceDate(self, tprice, tdate, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionOrderPriceStatus(self, tprice, tstatus, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionOrderQtyDate(self, tqty, tdate, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionOrderQtyStatus(self, tqty, tstatus, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionOrderDateStatus(self, tdate, tstatus, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionOrderPrice(self, tprice, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and oid = %s;"
        cursor.execute(query, (tprice, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionOrderQty(self, tqty, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and oid = %s;"
        print("Aqui estoy")
        print(tqty)
        cursor.execute(query, (tqty, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
            print(row)
        return result

    def getAllTransactionsByRegionOrderDate(self, tdate, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and oid = %s;"
        cursor.execute(query, (tdate, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionOrderStatus(self, tstatus, rname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and oid = %s;"
        cursor.execute(query, (tstatus, rname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCitySupplier(self, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and sid = %s;"
        cursor.execute(query, (cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierPriceQtyDate(self, tprice, tqty, tdate, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierPriceQtyStatus(self, tprice, tqty, tstatus, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierPriceDateStatus(self, tprice, tdate, tstatus, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierQtyDateStatus(self, tqty, tdate, tstatus, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierPriceQty(self, tprice, tqty, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tprice, tqty, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierPriceDate(self, tprice, tdate, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tprice, tdate, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierPriceStatus(self, tprice, tstatus, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierQtyDate(self, tqty, tdate, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tqty, tdate, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierQtyStatus(self, tqty, tstatus, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierDateStatus(self, tdate, tstatus, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierPrice(self, tprice, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tprice, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierQty(self, tqty, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tqty, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierDate(self, tdate, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tdate, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierStatus(self, tstatus, cname, sid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and sid = %s;"
        cursor.execute(query, (tstatus, cname, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCityRequester(self, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and rid = %s"
        cursor.execute(query, (cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterPriceQtyDate(self, tprice, tqty, tdate, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and rid = %s"
        cursor.execute(query, (tprice, tqty, tdate, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterPriceQtyStatus(self, tprice, tqty, tstatus, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and rid = %s"
        cursor.execute(query, (tprice, tqty, tstatus, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterPriceDateStatus(self, tprice, tdate, tstatus, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s"
        cursor.execute(query, (tprice, tdate, tstatus, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterQtyDateStatus(self, tqty, tdate, tstatus, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s"
        cursor.execute(query, (tqty, tdate, tstatus, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterPriceQty(self, tprice, tqty, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and rid = %s"
        cursor.execute(query, (tprice, tqty, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterPriceDate(self, tprice, tdate, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and rid = %s"
        cursor.execute(query, (tprice, tdate, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterPriceStatus(self, tprice, tstatus, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and rid = %s"
        cursor.execute(query, (tprice, tstatus, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterQtyDate(self, tqty, tdate, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and rid = %s"
        cursor.execute(query, (tqty, tdate, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterQtyStatus(self, tqty, tstatus, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and rid = %s"
        cursor.execute(query, (tqty, tstatus, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterDateStatus(self, tdate, tstatus, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and rid = %s"
        cursor.execute(query, (tdate, tstatus, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterPrice(self, tprice, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and rid = %s"
        cursor.execute(query, (tprice, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterQty(self, tqty, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and rid = %s"
        cursor.execute(query, (tqty, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterDate(self, tdate, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and rid = %s"
        cursor.execute(query, (tdate, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterStatus(self, tstatus, cname, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and rid = %s"
        cursor.execute(query, (tstatus, cname, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCityResource(self, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and rsid = %s;"
        cursor.execute(query, (cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourcePriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourcePriceQtyDate(self, tprice, tqty, tdate, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourcePriceQtyStatus(self, tprice, tqty, tstatus, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourcePriceDateStatus(self, tprice, tdate, tstatus, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceQtyDateStatus(self, tqty, tdate, tstatus, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourcePriceQty(self, tprice, tqty, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourcePriceDate(self, tprice, tdate, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourcePriceStatus(self, tprice, tstatus, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceQtyDate(self, tqty, tdate, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceQtyStatus(self, tqty, tstatus, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceDateStatus(self, tdate, tstatus, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourcePrice(self, tprice, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tprice, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceQty(self, tqty, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tqty, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceDate(self, tdate, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tdate, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceStatus(self, tstatus, cname, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and rsid = %s;"
        cursor.execute(query, (tstatus, cname, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCityKeyword(self, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and kid = %s;"
        cursor.execute(query, (cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordPriceQtyDate(self, tprice, tqty, tdate, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordPriceQtyStatus(self, tprice, tqty, tstatus, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordPriceDateStatus(self, tprice, tdate, tstatus, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordQtyDateStatus(self, tqty, tdate, tstatus, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordPriceQty(self, tprice, tqty, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordPriceDate(self, tprice, tdate, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordPriceStatus(self, tprice, tstatus, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordQtyDate(self, tqty, tdate, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordQtyStatus(self, tqty, tstatus, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordDateStatus(self, tdate, tstatus, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordPrice(self, tprice, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tprice, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordQty(self, tqty, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tqty, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordDate(self, tdate, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tdate, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordStatus(self, tstatus, cname, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and kid = %s;"
        cursor.execute(query, (tstatus, cname, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCityCategory(self, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, cat_name,
                                                           cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryPriceQtyDate(self, tprice, tqty, tdate, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryPriceQtyStatus(self, tprice, tqty, tstatus, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryPriceDateStatus(self, tprice, tdate, tstatus, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryQtyDateStatus(self, tqty, tdate, tstatus, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryPriceQty(self, tprice, tqty, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryPriceDate(self, tprice, tdate, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryPriceStatus(self, tprice, tstatus, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryQtyDate(self, tqty, tdate, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryQtyStatus(self, tqty, tstatus, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryDateStatus(self, tdate, tstatus, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryPrice(self, tprice, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryQty(self, tqty, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryDate(self, tdate, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryStatus(self, tstatus, cname, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, cname, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCityOrder(self, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and oid = %s;"
        cursor.execute(query, (cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderPriceQtyDate(self, tprice, tqty, tdate, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderPriceQtyStatus(self, tprice, tqty, tstatus, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderPriceDateStatus(self, tprice, tdate, tstatus, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderQtyDateStatus(self, tqty, tdate, tstatus, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderPriceQty(self, tprice, tqty, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderPriceDate(self, tprice, tdate, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderPriceStatus(self, tprice, tstatus, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderQtyDate(self, tqty, tdate, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderQtyStatus(self, tqty, tstatus, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderDateStatus(self, tdate, tstatus, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderPrice(self, tprice, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tprice, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderQty(self, tqty, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tqty, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderDate(self, tdate, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tdate, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityOrderStatus(self, tstatus, cname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Order_Info) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and oid = %s;"
        cursor.execute(query, (tstatus, cname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierRequester(self, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where sid = %s and rid = %s;"
        cursor.execute(query, (sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterPriceQtyDate(self, tprice, tqty, tdate, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tprice = %s and tqty = %s and tdate = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterPriceQtyStatus(self, tprice, tqty, tstatus, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tprice = %s and tqty = %s and tstatus = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterPriceDateStatus(self, tprice, tdate, tstatus, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tprice = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterQtyDateStatus(self, tqty, tdate, tstatus, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tqty = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterPriceQty(self, tprice, tqty, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tprice = %s and tqty = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterPriceDate(self, tprice, tdate, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tprice = %s and tdate = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tdate, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterPriceStatus(self, tprice, tstatus, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tprice = %s and tstatus = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tstatus, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterQtyDate(self, tqty, tdate, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tqty = %s and tdate = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tqty, tdate, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterQtyStatus(self, tqty, tstatus, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tqty = %s and tstatus = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tqty, tstatus, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterDateStatus(self, tdate, tstatus, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tdate = %s and tstatus = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tdate, tstatus, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterPrice(self, tprice, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tprice = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterQty(self, tqty, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tqty = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tqty, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterDate(self, tdate, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tdate = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tdate, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterStatus(self, tstatus, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester where tstatus = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tstatus, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierResource(self, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where sid = %s and rsid = %s;"
        cursor.execute(query, (sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourcePriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourcePriceQtyDate(self, tprice, tqty, tdate, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tprice = %s and tqty = %s and tdate = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourcePriceQtyStatus(self, tprice, tqty, tstatus, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tprice = %s and tqty = %s and tstatus = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourcePriceDateStatus(self, tprice, tdate, tstatus, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tprice = %s and tdate = %s and tstatus = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceQtyDateStatus(self, tqty, tdate, tstatus, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tqty = %s and tdate = %s and tstatus = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourcePriceQty(self, tprice, tqty, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tprice = %s and tqty = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourcePriceDate(self, tprice, tdate, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tprice = %s and tdate = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourcePriceStatus(self, tprice, tstatus, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tprice = %s and tstatus = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tstatus, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceQtyDate(self, tqty, tdate, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tqty = %s and tdate = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceQtyStatus(self, tqty, tstatus, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tqty = %s and tstatus = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tstatus, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceDateStatus(self, tdate, tstatus, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tdate = %s and tstatus = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tdate, tstatus, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourcePrice(self, tprice, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tprice = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceQty(self, tqty, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tqty = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tqty, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceDate(self, tdate, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tdate = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tdate, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceStatus(self, tstatus, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource where tstatus = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tstatus, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierKeyword(self, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where sid = %s and kid = %s;"
        cursor.execute(query, (sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordPriceQtyDate(self, tprice, tqty, tdate, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordPriceQtyStatus(self, tprice, tqty, tstatus, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tstatus = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordPriceDateStatus(self, tprice, tdate, tstatus, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and tstatus = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordQtyDateStatus(self, tqty, tdate, tstatus, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and tstatus = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordPriceQty(self, tprice, tqty, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordPriceDate(self, tprice, tdate, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordPriceStatus(self, tprice, tstatus, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tstatus = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordQtyDate(self, tqty, tdate, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordQtyStatus(self, tqty, tstatus, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tstatus = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordDateStatus(self, tdate, tstatus, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and tstatus = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordPrice(self, tprice, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordQty(self, tqty, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tqty, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordDate(self, tdate, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tdate, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordStatus(self, tstatus, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tstatus = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tstatus, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierCategory(self, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid, cat_name,
                                                               cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryPriceQtyDate(self, tprice, tqty, tdate, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tprice = %s and tqty = %s and tdate = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryPriceQtyStatus(self, tprice, tqty, tstatus, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tprice = %s and tqty = %s and tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryPriceDateStatus(self, tprice, tdate, tstatus, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tprice = %s and tdate = %s and tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryQtyDateStatus(self, tqty, tdate, tstatus, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tqty = %s and tdate = %s and tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryPriceQty(self, tprice, tqty, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tprice = %s and tqty = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryPriceDate(self, tprice, tdate, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tprice = %s and tdate = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryPriceStatus(self, tprice, tstatus, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tprice = %s and tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryQtyDate(self, tqty, tdate, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tqty = %s and tdate = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryQtyStatus(self, tqty, tstatus, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tqty = %s and tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryDateStatus(self, tdate, tstatus, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tdate = %s and tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryPrice(self, tprice, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tprice = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryQty(self, tqty, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tqty = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryDate(self, tdate, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tdate = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryStatus(self, tstatus, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category where tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierOrder(self, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where sid = %s and oid = %s;"
        cursor.execute(query, (sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderPriceQtyDate(self, tprice, tqty, tdate, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tprice = %s and tqty = %s and tdate = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderPriceQtyStatus(self, tprice, tqty, tstatus, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tprice = %s and tqty = %s and tstatus = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderPriceDateStatus(self, tprice, tdate, tstatus, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tprice = %s and tdate = %s and tstatus = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderQtyDateStatus(self, tqty, tdate, tstatus, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tqty = %s and tdate = %s and tstatus = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderPriceQty(self, tprice, tqty, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tprice = %s and tqty = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderPriceDate(self, tprice, tdate, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tprice = %s and tdate = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderPriceStatus(self, tprice, tstatus, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tprice = %s and tstatus = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderQtyDate(self, tqty, tdate, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tqty = %s and tdate = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderQtyStatus(self, tqty, tstatus, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tqty = %s and tstatus = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderDateStatus(self, tdate, tstatus, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tdate = %s and tstatus = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderPrice(self, tprice, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tprice = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderQty(self, tqty, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tqty = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tqty, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderDate(self, tdate, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tdate = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tdate, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierOrderStatus(self, tstatus, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join Order_Info where tstatus = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tstatus, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRequesterResource(self, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where rid = %s and rsid = %s;"
        cursor.execute(query, (rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourcePriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourcePriceQtyDate(self, tprice, tqty, tdate, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and tqty = %s and tdate = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourcePriceQtyStatus(self, tprice, tqty, tstatus, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and tqty = %s and tstatus = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourcePriceDateStatus(self, tprice, tdate, tstatus, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and tdate = %s and tstatus = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceQtyDateStatus(self, tqty, tdate, tstatus, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tqty = %s and tdate = %s and tstatus = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourcePriceQty(self, tprice, tqty, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and tqty = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourcePriceDate(self, tprice, tdate, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and tdate = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourcePriceStatus(self, tprice, tstatus, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and tstatus = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tstatus, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceQtyDate(self, tqty, tdate, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tqty = %s and tdate = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceQtyStatus(self, tqty, tstatus, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tqty = %s and tstatus = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tstatus, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceDateStatus(self, tdate, tstatus, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tdate = %s and tstatus = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tdate, tstatus, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourcePrice(self, tprice, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceQty(self, tqty, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tqty = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceDate(self, tdate, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tdate = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tdate, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceStatus(self, tstatus, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource where tstatus = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tstatus, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRequesterKeyword(self, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where rid = %s and kid = %s;"
        cursor.execute(query, (rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordPriceQtyDate(self, tprice, tqty, tdate, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordPriceQtyStatus(self, tprice, tqty, tstatus, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tstatus = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordPriceDateStatus(self, tprice, tdate, tstatus, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and tstatus = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordQtyDateStatus(self, tqty, tdate, tstatus, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and tstatus = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordPriceQty(self, tprice, tqty, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordPriceDate(self, tprice, tdate, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordPriceStatus(self, tprice, tstatus, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tstatus = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordQtyDate(self, tqty, tdate, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordQtyStatus(self, tqty, tstatus, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tstatus = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordDateStatus(self, tdate, tstatus, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and tstatus = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordPrice(self, tprice, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordQty(self, tqty, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordDate(self, tdate, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tdate, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordStatus(self, tstatus, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tstatus = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tstatus, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRequesterCategory(self, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rid, cat_name,
                                                                cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryPriceQtyDate(self, tprice, tqty, tdate, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and tqty = %s and tdate = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryPriceQtyStatus(self, tprice, tqty, tstatus, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and tqty = %s and tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryPriceDateStatus(self, tprice, tdate, tstatus, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and tdate = %s and tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryQtyDateStatus(self, tqty, tdate, tstatus, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tqty = %s and tdate = %s and tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryPriceQty(self, tprice, tqty, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and tqty = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryPriceDate(self, tprice, tdate, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and tdate = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryPriceStatus(self, tprice, tstatus, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryQtyDate(self, tqty, tdate, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tqty = %s and tdate = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryQtyStatus(self, tqty, tstatus, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tqty = %s and tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryDateStatus(self, tdate, tstatus, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tdate = %s and tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryPrice(self, tprice, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryQty(self, tqty, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tqty = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryDate(self, tdate, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tdate = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryStatus(self, tstatus, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRequesterOrder(self, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where rid = %s and oid = %s;"
        cursor.execute(query, (rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderPriceQtyDate(self, tprice, tqty, tdate, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tprice = %s and tqty = %s and tdate = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderPriceQtyStatus(self, tprice, tqty, tstatus, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tprice = %s and tqty = %s and tstatus = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderPriceDateStatus(self, tprice, tdate, tstatus, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tprice = %s and tdate = %s and tstatus = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderQtyDateStatus(self, tqty, tdate, tstatus, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tqty = %s and tdate = %s and tstatus = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderPriceQty(self, tprice, tqty, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tprice = %s and tqty = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderPriceDate(self, tprice, tdate, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tprice = %s and tdate = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderPriceStatus(self, tprice, tstatus, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tprice = %s and tstatus = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderQtyDate(self, tqty, tdate, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tqty = %s and tdate = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderQtyStatus(self, tqty, tstatus, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tqty = %s and tstatus = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderDateStatus(self, tdate, tstatus, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tdate = %s and tstatus = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderPrice(self, tprice, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tprice = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderQty(self, tqty, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tqty = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderDate(self, tdate, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tdate = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tdate, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterOrderStatus(self, tstatus, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join requester natural inner join Order_Info where tstatus = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tstatus, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByResourceKeyword(self, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where rsid = %s and kid = %s;"
        cursor.execute(query, (rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordPriceQtyDate(self, tprice, tqty, tdate, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordPriceQtyStatus(self, tprice, tqty, tstatus, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tstatus = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordPriceDateStatus(self, tprice, tdate, tstatus, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and tstatus = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordQtyDateStatus(self, tqty, tdate, tstatus, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and tstatus = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordPriceQty(self, tprice, tqty, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordPriceDate(self, tprice, tdate, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordPriceStatus(self, tprice, tstatus, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tstatus = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordQtyDate(self, tqty, tdate, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordQtyStatus(self, tqty, tstatus, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tstatus = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordDateStatus(self, tdate, tstatus, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and tstatus = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordPrice(self, tprice, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordQty(self, tqty, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordDate(self, tdate, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tdate, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordStatus(self, tstatus, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tstatus = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tstatus, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByResourceOrder(self, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where rsid = %s and oid = %s;"
        cursor.execute(query, (rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderPriceQtyDate(self, tprice, tqty, tdate, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tprice = %s and tqty = %s and tdate = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderPriceQtyStatus(self, tprice, tqty, tstatus, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tprice = %s and tqty = %s and tstatus = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderPriceDateStatus(self, tprice, tdate, tstatus, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tprice = %s and tdate = %s and tstatus = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderQtyDateStatus(self, tqty, tdate, tstatus, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tqty = %s and tdate = %s and tstatus = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderPriceQty(self, tprice, tqty, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tprice = %s and tqty = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderPriceDate(self, tprice, tdate, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tprice = %s and tdate = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderPriceStatus(self, tprice, tstatus, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tprice = %s and tstatus = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderQtyDate(self, tqty, tdate, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tqty = %s and tdate = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderQtyStatus(self, tqty, tstatus, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tqty = %s and tstatus = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderDateStatus(self, tdate, tstatus, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tdate = %s and tstatus = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderPrice(self, tprice, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tprice = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderQty(self, tqty, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tqty = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderDate(self, tdate, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tdate = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tdate, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceOrderStatus(self, tstatus, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join Order_Info where tstatus = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tstatus, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByKeywordCategory(self, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, kid, cat_name,
                                                              cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryPriceQtyDate(self, tprice, tqty, tdate, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and tqty = %s and tdate = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryPriceQtyStatus(self, tprice, tqty, tstatus, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and tqty = %s and tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryPriceDateStatus(self, tprice, tdate, tstatus, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and tdate = %s and tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryQtyDateStatus(self, tqty, tdate, tstatus, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tqty = %s and tdate = %s and tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryPriceQty(self, tprice, tqty, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and tqty = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryPriceDate(self, tprice, tdate, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and tdate = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryPriceStatus(self, tprice, tstatus, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryQtyDate(self, tqty, tdate, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tqty = %s and tdate = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryQtyStatus(self, tqty, tstatus, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tqty = %s and tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryDateStatus(self, tdate, tstatus, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tdate = %s and tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryPrice(self, tprice, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryQty(self, tqty, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tqty = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryDate(self, tdate, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tdate = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryStatus(self, tstatus, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByKeywordOrder(self, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where kid = %s and oid = %s;"
        cursor.execute(query, (kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderPriceQtyDate(self, tprice, tqty, tdate, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tprice = %s and tqty = %s and tdate = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderPriceQtyStatus(self, tprice, tqty, tstatus, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tprice = %s and tqty = %s and tstatus = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderPriceDateStatus(self, tprice, tdate, tstatus, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tprice = %s and tdate = %s and tstatus = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderQtyDateStatus(self, tqty, tdate, tstatus, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tqty = %s and tdate = %s and tstatus = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderPriceQty(self, tprice, tqty, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tprice = %s and tqty = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderPriceDate(self, tprice, tdate, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tprice = %s and tdate = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderPriceStatus(self, tprice, tstatus, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tprice = %s and tstatus = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderQtyDate(self, tqty, tdate, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tqty = %s and tdate = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderQtyStatus(self, tqty, tstatus, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tqty = %s and tstatus = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderDateStatus(self, tdate, tstatus, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tdate = %s and tstatus = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderPrice(self, tprice, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tprice = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderQty(self, tqty, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tqty = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderDate(self, tdate, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tdate = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tdate, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordOrderStatus(self, tstatus, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join Order_Info where tstatus = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tstatus, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCategoryOrder(self, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cat_name, cat_pname,
                                                            oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderPriceQtyDate(self, tprice, tqty, tdate, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tprice = %s and tqty = %s and tdate = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderPriceQtyStatus(self, tprice, tqty, tstatus, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tprice = %s and tqty = %s and tstatus = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderPriceDateStatus(self, tprice, tdate, tstatus, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tprice = %s and tdate = %s and tstatus = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderQtyDateStatus(self, tqty, tdate, tstatus, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tqty = %s and tdate = %s and tstatus = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderPriceQty(self, tprice, tqty, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tprice = %s and tqty = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderPriceDate(self, tprice, tdate, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tprice = %s and tdate = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tdate, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderPriceStatus(self, tprice, tstatus, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tprice = %s and tstatus = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tstatus, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderQtyDate(self, tqty, tdate, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tqty = %s and tdate = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tdate, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderQtyStatus(self, tqty, tstatus, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tqty = %s and tstatus = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tstatus, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderDateStatus(self, tdate, tstatus, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tdate = %s and tstatus = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tdate, tstatus, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderPrice(self, tprice, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tprice = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderQty(self, tqty, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tqty = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderDate(self, tdate, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tdate = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tdate, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCategoryOrderStatus(self, tstatus, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join resource natural inner join supplier natural inner join category natural inner join Order_Info where tstatus = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tstatus, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionSupplierRequester(self, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, sid,
                                                                      rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterPriceQtyDate(self, tprice, tqty, tdate, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterPriceQtyStatus(self, tprice, tqty, tstatus, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterPriceDateStatus(self, tprice, tdate, tstatus, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterQtyDateStatus(self, tqty, tdate, tstatus, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterPriceQty(self, tprice, tqty, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterPriceDate(self, tprice, tdate, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tdate, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterPriceStatus(self, tprice, tstatus, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterQtyDate(self, tqty, tdate, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tqty, tdate, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterQtyStatus(self, tqty, tstatus, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterDateStatus(self, tdate, tstatus, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterPrice(self, tprice, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterQty(self, tqty, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tqty, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterDate(self, tdate, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tdate, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierRequesterStatus(self, tstatus, rname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tstatus, rname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionSupplierResource(self, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourcePriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, sid,
                                                                     rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourcePriceQtyDate(self, tprice, tqty, tdate, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourcePriceQtyStatus(self, tprice, tqty, tstatus, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourcePriceDateStatus(self, tprice, tdate, tstatus, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourceQtyDateStatus(self, tqty, tdate, tstatus, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourcePriceQty(self, tprice, tqty, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourcePriceDate(self, tprice, tdate, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourcePriceStatus(self, tprice, tstatus, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourceQtyDate(self, tqty, tdate, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourceQtyStatus(self, tqty, tstatus, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourceDateStatus(self, tdate, tstatus, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourcePrice(self, tprice, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourceQty(self, tqty, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tqty, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourceDate(self, tdate, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tdate, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierResourceStatus(self, tstatus, rname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tstatus, rname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionSupplierKeyword(self, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, sid,
                                                                    kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordPriceQtyDate(self, tprice, tqty, tdate, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordPriceQtyStatus(self, tprice, tqty, tstatus, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordPriceDateStatus(self, tprice, tdate, tstatus, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordQtyDateStatus(self, tqty, tdate, tstatus, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordPriceQty(self, tprice, tqty, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordPriceDate(self, tprice, tdate, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordPriceStatus(self, tprice, tstatus, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordQtyDate(self, tqty, tdate, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordQtyStatus(self, tqty, tstatus, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordDateStatus(self, tdate, tstatus, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordPrice(self, tprice, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordQty(self, tqty, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tqty, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordDate(self, tdate, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tdate, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierKeywordStatus(self, tstatus, rname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tstatus, rname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionSupplierCategory(self, rname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, sid,
                                                                     cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryPriceQtyDate(self, tprice, tqty, tdate, rname, sid, cat_name,
                                                               cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryPriceQtyStatus(self, tprice, tqty, tstatus, rname, sid, cat_name,
                                                                 cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryPriceDateStatus(self, tprice, tdate, tstatus, rname, sid, cat_name,
                                                                  cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryQtyDateStatus(self, tqty, tdate, tstatus, rname, sid, cat_name,
                                                                cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryPriceQty(self, tprice, tqty, rname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryPriceDate(self, tprice, tdate, rname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryPriceStatus(self, tprice, tstatus, rname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryQtyDate(self, tqty, tdate, rname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryQtyStatus(self, tqty, tstatus, rname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryDateStatus(self, tdate, tstatus, rname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryPrice(self, tprice, rname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryQty(self, tqty, rname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryDate(self, tdate, rname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierCategoryStatus(self, tstatus, rname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, rname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionSupplierOrder(self, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderPriceQtyDate(self, tprice, tqty, tdate, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderPriceQtyStatus(self, tprice, tqty, tstatus, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderPriceDateStatus(self, tprice, tdate, tstatus, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderQtyDateStatus(self, tqty, tdate, tstatus, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderPriceQty(self, tprice, tqty, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderPriceDate(self, tprice, tdate, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderPriceStatus(self, tprice, tstatus, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderQtyDate(self, tqty, tdate, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderQtyStatus(self, tqty, tstatus, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderDateStatus(self, tdate, tstatus, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderPrice(self, tprice, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderQty(self, tqty, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tqty, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderDate(self, tdate, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tdate, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionSupplierOrderStatus(self, tstatus, rname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tstatus, rname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionRequesterResource(self, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourcePriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, rid,
                                                                      rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourcePriceQtyDate(self, tprice, tqty, tdate, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourcePriceQtyStatus(self, tprice, tqty, tstatus, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourcePriceDateStatus(self, tprice, tdate, tstatus, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourceQtyDateStatus(self, tqty, tdate, tstatus, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourcePriceQty(self, tprice, tqty, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourcePriceDate(self, tprice, tdate, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourcePriceStatus(self, tprice, tstatus, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourceQtyDate(self, tqty, tdate, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourceQtyStatus(self, tqty, tstatus, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourceDateStatus(self, tdate, tstatus, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourcePrice(self, tprice, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourceQty(self, tqty, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourceDate(self, tdate, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tdate, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterResourceStatus(self, tstatus, rname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tstatus, rname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionRequesterKeyword(self, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, rid,
                                                                     kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordPriceQtyDate(self, tprice, tqty, tdate, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordPriceQtyStatus(self, tprice, tqty, tstatus, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordPriceDateStatus(self, tprice, tdate, tstatus, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordQtyDateStatus(self, tqty, tdate, tstatus, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordPriceQty(self, tprice, tqty, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordPriceDate(self, tprice, tdate, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordPriceStatus(self, tprice, tstatus, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordQtyDate(self, tqty, tdate, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordQtyStatus(self, tqty, tstatus, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordDateStatus(self, tdate, tstatus, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordPrice(self, tprice, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordQty(self, tqty, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordDate(self, tdate, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tdate, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterKeywordStatus(self, tstatus, rname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tstatus, rname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionRequesterCategory(self, rname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, rid,
                                                                      cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryPriceQtyDate(self, tprice, tqty, tdate, rname, rid, cat_name,
                                                                cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryPriceQtyStatus(self, tprice, tqty, tstatus, rname, rid, cat_name,
                                                                  cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryPriceDateStatus(self, tprice, tdate, tstatus, rname, rid, cat_name,
                                                                   cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryQtyDateStatus(self, tqty, tdate, tstatus, rname, rid, cat_name,
                                                                 cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryPriceQty(self, tprice, tqty, rname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryPriceDate(self, tprice, tdate, rname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryPriceStatus(self, tprice, tstatus, rname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryQtyDate(self, tqty, tdate, rname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryQtyStatus(self, tqty, tstatus, rname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryDateStatus(self, tdate, tstatus, rname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryPrice(self, tprice, rname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryQty(self, tqty, rname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryDate(self, tdate, rname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterCategoryStatus(self, tstatus, rname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, rname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionRequesterOrder(self, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderPriceQtyDate(self, tprice, tqty, tdate, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderPriceQtyStatus(self, tprice, tqty, tstatus, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderPriceDateStatus(self, tprice, tdate, tstatus, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderQtyDateStatus(self, tqty, tdate, tstatus, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderPriceQty(self, tprice, tqty, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderPriceDate(self, tprice, tdate, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderPriceStatus(self, tprice, tstatus, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderQtyDate(self, tqty, tdate, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderQtyStatus(self, tqty, tstatus, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderDateStatus(self, tdate, tstatus, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderPrice(self, tprice, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderQty(self, tqty, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderDate(self, tdate, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tdate, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionRequesterOrderStatus(self, tstatus, rname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tstatus, rname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionResourceKeyword(self, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, rsid,
                                                                    kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordPriceQtyDate(self, tprice, tqty, tdate, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordPriceQtyStatus(self, tprice, tqty, tstatus, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordPriceDateStatus(self, tprice, tdate, tstatus, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordQtyDateStatus(self, tqty, tdate, tstatus, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordPriceQty(self, tprice, tqty, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordPriceDate(self, tprice, tdate, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordPriceStatus(self, tprice, tstatus, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordQtyDate(self, tqty, tdate, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordQtyStatus(self, tqty, tstatus, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordDateStatus(self, tdate, tstatus, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordPrice(self, tprice, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordQty(self, tqty, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordDate(self, tdate, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tdate, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceKeywordStatus(self, tstatus, rname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tstatus, rname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionResourceOrder(self, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderPriceQtyDate(self, tprice, tqty, tdate, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderPriceQtyStatus(self, tprice, tqty, tstatus, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderPriceDateStatus(self, tprice, tdate, tstatus, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderQtyDateStatus(self, tqty, tdate, tstatus, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderPriceQty(self, tprice, tqty, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderPriceDate(self, tprice, tdate, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderPriceStatus(self, tprice, tstatus, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderQtyDate(self, tqty, tdate, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderQtyStatus(self, tqty, tstatus, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderDateStatus(self, tdate, tstatus, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderPrice(self, tprice, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderQty(self, tqty, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderDate(self, tdate, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tdate, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionResourceOrderStatus(self, tstatus, rname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tstatus, rname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionKeywordCategory(self, rname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, kid,
                                                                    cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryPriceQtyDate(self, tprice, tqty, tdate, rname, kid, cat_name,
                                                              cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryPriceQtyStatus(self, tprice, tqty, tstatus, rname, kid, cat_name,
                                                                cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryPriceDateStatus(self, tprice, tdate, tstatus, rname, kid, cat_name,
                                                                 cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryQtyDateStatus(self, tqty, tdate, tstatus, rname, kid, cat_name,
                                                               cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryPriceQty(self, tprice, tqty, rname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryPriceDate(self, tprice, tdate, rname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryPriceStatus(self, tprice, tstatus, rname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryQtyDate(self, tqty, tdate, rname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryQtyStatus(self, tqty, tstatus, rname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryDateStatus(self, tdate, tstatus, rname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryPrice(self, tprice, rname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryQty(self, tqty, rname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryDate(self, tdate, rname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordCategoryStatus(self, tstatus, rname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, rname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionKeywordOrder(self, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderPriceQtyDate(self, tprice, tqty, tdate, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderPriceQtyStatus(self, tprice, tqty, tstatus, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderPriceDateStatus(self, tprice, tdate, tstatus, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderQtyDateStatus(self, tqty, tdate, tstatus, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderPriceQty(self, tprice, tqty, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderPriceDate(self, tprice, tdate, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderPriceStatus(self, tprice, tstatus, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderQtyDate(self, tqty, tdate, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderQtyStatus(self, tqty, tstatus, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderDateStatus(self, tdate, tstatus, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderPrice(self, tprice, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderQty(self, tqty, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderDate(self, tdate, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tdate, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionKeywordOrderStatus(self, tstatus, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tstatus, rname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRegionCategoryOrder(self, rname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rname, cat_name,
                                                                  cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderPriceQtyDate(self, tprice, tqty, tdate, rname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tdate = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderPriceQtyStatus(self, tprice, tqty, tstatus, rname, cat_name, cat_pname,
                                                              oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderPriceDateStatus(self, tprice, tdate, tstatus, rname, cat_name, cat_pname,
                                                               oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderQtyDateStatus(self, tqty, tdate, tstatus, rname, cat_name, cat_pname,
                                                             oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderPriceQty(self, tprice, tqty, rname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tqty = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderPriceDate(self, tprice, tdate, rname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tdate = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tdate, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderPriceStatus(self, tprice, tstatus, rname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tstatus, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderQtyDate(self, tqty, tdate, rname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tdate = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tdate, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderQtyStatus(self, tqty, tstatus, rname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tstatus, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderDateStatus(self, tdate, tstatus, rname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tdate, tstatus, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderPrice(self, tprice, rname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tprice = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderQty(self, tqty, rname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tqty = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderDate(self, tdate, rname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tdate = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tdate, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRegionCategoryOrderStatus(self, tstatus, rname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city natural inner join region where tstatus = %s and rname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tstatus, rname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCitySupplierRequester(self, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, sid,
                                                                    rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterPriceQtyDate(self, tprice, tqty, tdate, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterPriceQtyStatus(self, tprice, tqty, tstatus, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterPriceDateStatus(self, tprice, tdate, tstatus, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterQtyDateStatus(self, tqty, tdate, tstatus, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterPriceQty(self, tprice, tqty, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tqty, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterPriceDate(self, tprice, tdate, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tdate, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterPriceStatus(self, tprice, tstatus, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterQtyDate(self, tqty, tdate, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tqty, tdate, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterQtyStatus(self, tqty, tstatus, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterDateStatus(self, tdate, tstatus, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterPrice(self, tprice, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tprice, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterQty(self, tqty, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tqty, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterDate(self, tdate, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tdate, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierRequesterStatus(self, tstatus, cname, sid, rid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join requester natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and sid = %s and rid = %s;"
        cursor.execute(query, (tstatus, cname, sid, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCitySupplierResource(self, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourcePriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, sid,
                                                                   rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourcePriceQtyDate(self, tprice, tqty, tdate, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourcePriceQtyStatus(self, tprice, tqty, tstatus, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourcePriceDateStatus(self, tprice, tdate, tstatus, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourceQtyDateStatus(self, tqty, tdate, tstatus, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourcePriceQty(self, tprice, tqty, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourcePriceDate(self, tprice, tdate, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourcePriceStatus(self, tprice, tstatus, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourceQtyDate(self, tqty, tdate, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourceQtyStatus(self, tqty, tstatus, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourceDateStatus(self, tdate, tstatus, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourcePrice(self, tprice, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tprice, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourceQty(self, tqty, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tqty, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourceDate(self, tdate, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tdate, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierResourceStatus(self, tstatus, cname, sid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and sid = %s and rsid = %s;"
        cursor.execute(query, (tstatus, cname, sid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCitySupplierKeyword(self, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordPriceQtyDate(self, tprice, tqty, tdate, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordPriceQtyStatus(self, tprice, tqty, tstatus, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordPriceDateStatus(self, tprice, tdate, tstatus, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordQtyDateStatus(self, tqty, tdate, tstatus, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordPriceQty(self, tprice, tqty, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordPriceDate(self, tprice, tdate, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordPriceStatus(self, tprice, tstatus, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordQtyDate(self, tqty, tdate, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordQtyStatus(self, tqty, tstatus, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordDateStatus(self, tdate, tstatus, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordPrice(self, tprice, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tprice, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordQty(self, tqty, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tqty, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordDate(self, tdate, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tdate, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierKeywordStatus(self, tstatus, cname, sid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and sid = %s and kid = %s;"
        cursor.execute(query, (tstatus, cname, sid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCitySupplierCategory(self, cname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, sid,
                                                                   cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryPriceQtyDate(self, tprice, tqty, tdate, cname, sid, cat_name,
                                                             cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryPriceQtyStatus(self, tprice, tqty, tstatus, cname, sid, cat_name,
                                                               cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryPriceDateStatus(self, tprice, tdate, tstatus, cname, sid, cat_name,
                                                                cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryQtyDateStatus(self, tqty, tdate, tstatus, cname, sid, cat_name,
                                                              cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryPriceQty(self, tprice, tqty, cname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryPriceDate(self, tprice, tdate, cname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryPriceStatus(self, tprice, tstatus, cname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryQtyDate(self, tqty, tdate, cname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryQtyStatus(self, tqty, tstatus, cname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryDateStatus(self, tdate, tstatus, cname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryPrice(self, tprice, cname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryQty(self, tqty, cname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryDate(self, tdate, cname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierCategoryStatus(self, tstatus, cname, sid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and sid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, cname, sid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCitySupplierOrder(self, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderPriceQtyDate(self, tprice, tqty, tdate, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderPriceQtyStatus(self, tprice, tqty, tstatus, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderPriceDateStatus(self, tprice, tdate, tstatus, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderQtyDateStatus(self, tqty, tdate, tstatus, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderPriceQty(self, tprice, tqty, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderPriceDate(self, tprice, tdate, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderPriceStatus(self, tprice, tstatus, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderQtyDate(self, tqty, tdate, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderQtyStatus(self, tqty, tstatus, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderDateStatus(self, tdate, tstatus, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderPrice(self, tprice, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tprice, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderQty(self, tqty, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tqty, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderDate(self, tdate, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tdate, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCitySupplierOrderStatus(self, tstatus, cname, sid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and sid = %s and oid = %s;"
        cursor.execute(query, (tstatus, cname, sid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCityRequesterResource(self, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourcePriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, rid,
                                                                    rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourcePriceQtyDate(self, tprice, tqty, tdate, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourcePriceQtyStatus(self, tprice, tqty, tstatus, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourcePriceDateStatus(self, tprice, tdate, tstatus, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourceQtyDateStatus(self, tqty, tdate, tstatus, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourcePriceQty(self, tprice, tqty, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourcePriceDate(self, tprice, tdate, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourcePriceStatus(self, tprice, tstatus, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourceQtyDate(self, tqty, tdate, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourceQtyStatus(self, tqty, tstatus, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourceDateStatus(self, tdate, tstatus, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourcePrice(self, tprice, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourceQty(self, tqty, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourceDate(self, tdate, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tdate, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterResourceStatus(self, tstatus, cname, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tstatus, cname, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCityRequesterKeyword(self, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordPriceQtyDate(self, tprice, tqty, tdate, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordPriceQtyStatus(self, tprice, tqty, tstatus, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordPriceDateStatus(self, tprice, tdate, tstatus, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordQtyDateStatus(self, tqty, tdate, tstatus, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordPriceQty(self, tprice, tqty, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordPriceDate(self, tprice, tdate, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordPriceStatus(self, tprice, tstatus, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordQtyDate(self, tqty, tdate, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordQtyStatus(self, tqty, tstatus, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordDateStatus(self, tdate, tstatus, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordPrice(self, tprice, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordQty(self, tqty, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordDate(self, tdate, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tdate, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterKeywordStatus(self, tstatus, cname, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tstatus, cname, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCityRequesterCategory(self, cname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, rid,
                                                                    cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryPriceQtyDate(self, tprice, tqty, tdate, cname, rid, cat_name,
                                                              cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryPriceQtyStatus(self, tprice, tqty, tstatus, cname, rid, cat_name,
                                                                cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryPriceDateStatus(self, tprice, tdate, tstatus, cname, rid, cat_name,
                                                                 cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryQtyDateStatus(self, tqty, tdate, tstatus, cname, rid, cat_name,
                                                               cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryPriceQty(self, tprice, tqty, cname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryPriceDate(self, tprice, tdate, cname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryPriceStatus(self, tprice, tstatus, cname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryQtyDate(self, tqty, tdate, cname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryQtyStatus(self, tqty, tstatus, cname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryDateStatus(self, tdate, tstatus, cname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryPrice(self, tprice, cname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryQty(self, tqty, cname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryDate(self, tdate, cname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterCategoryStatus(self, tstatus, cname, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, cname, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCityRequesterOrder(self, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderPriceQtyDate(self, tprice, tqty, tdate, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderPriceQtyStatus(self, tprice, tqty, tstatus, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderPriceDateStatus(self, tprice, tdate, tstatus, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderQtyDateStatus(self, tqty, tdate, tstatus, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderPriceQty(self, tprice, tqty, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderPriceDate(self, tprice, tdate, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderPriceStatus(self, tprice, tstatus, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderQtyDate(self, tqty, tdate, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderQtyStatus(self, tqty, tstatus, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderDateStatus(self, tdate, tstatus, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderPrice(self, tprice, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderQty(self, tqty, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderDate(self, tdate, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tdate, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityRequesterOrderStatus(self, tstatus, cname, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join requester) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tstatus, cname, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCityResourceKeyword(self, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordPriceQtyDate(self, tprice, tqty, tdate, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordPriceQtyStatus(self, tprice, tqty, tstatus, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordPriceDateStatus(self, tprice, tdate, tstatus, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordQtyDateStatus(self, tqty, tdate, tstatus, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordPriceQty(self, tprice, tqty, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordPriceDate(self, tprice, tdate, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordPriceStatus(self, tprice, tstatus, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordQtyDate(self, tqty, tdate, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordQtyStatus(self, tqty, tstatus, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordDateStatus(self, tdate, tstatus, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordPrice(self, tprice, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordQty(self, tqty, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordDate(self, tdate, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tdate, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceKeywordStatus(self, tstatus, cname, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tstatus, cname, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCityResourceOrder(self, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderPriceQtyDate(self, tprice, tqty, tdate, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderPriceQtyStatus(self, tprice, tqty, tstatus, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderPriceDateStatus(self, tprice, tdate, tstatus, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderQtyDateStatus(self, tqty, tdate, tstatus, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderPriceQty(self, tprice, tqty, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderPriceDate(self, tprice, tdate, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderPriceStatus(self, tprice, tstatus, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderQtyDate(self, tqty, tdate, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderQtyStatus(self, tqty, tstatus, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderDateStatus(self, tdate, tstatus, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderPrice(self, tprice, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderQty(self, tqty, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderDate(self, tdate, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tdate, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityResourceOrderStatus(self, tstatus, cname, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tstatus, cname, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCityKeywordCategory(self, cname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, kid,
                                                                  cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryPriceQtyDate(self, tprice, tqty, tdate, cname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryPriceQtyStatus(self, tprice, tqty, tstatus, cname, kid, cat_name,
                                                              cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryPriceDateStatus(self, tprice, tdate, tstatus, cname, kid, cat_name,
                                                               cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryQtyDateStatus(self, tqty, tdate, tstatus, cname, kid, cat_name,
                                                             cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryPriceQty(self, tprice, tqty, cname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryPriceDate(self, tprice, tdate, cname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryPriceStatus(self, tprice, tstatus, cname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryQtyDate(self, tqty, tdate, cname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryQtyStatus(self, tqty, tstatus, cname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryDateStatus(self, tdate, tstatus, cname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryPrice(self, tprice, cname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryQty(self, tqty, cname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryDate(self, tdate, cname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordCategoryStatus(self, tstatus, cname, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join supplier natural inner join resource natural inner join Category natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, cname, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCityKeywordOrder(self, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderPriceQtyDate(self, tprice, tqty, tdate, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderPriceQtyStatus(self, tprice, tqty, tstatus, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderPriceDateStatus(self, tprice, tdate, tstatus, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderQtyDateStatus(self, tqty, tdate, tstatus, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderPriceQty(self, tprice, tqty, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderPriceDate(self, tprice, tdate, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderPriceStatus(self, tprice, tstatus, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderQtyDate(self, tqty, tdate, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderQtyStatus(self, tqty, tstatus, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderDateStatus(self, tdate, tstatus, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderPrice(self, tprice, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderQty(self, tqty, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderDate(self, tdate, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tdate, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityKeywordOrderStatus(self, tstatus, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join Keyword) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tstatus, cname, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByCityCategoryOrder(self, cname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, cname, cat_name,
                                                                cat_pname,
                                                                oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderPriceQtyDate(self, tprice, tqty, tdate, cname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tdate = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderPriceQtyStatus(self, tprice, tqty, tstatus, cname, cat_name, cat_pname,
                                                            oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderPriceDateStatus(self, tprice, tdate, tstatus, cname, cat_name, cat_pname,
                                                             oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderQtyDateStatus(self, tqty, tdate, tstatus, cname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderPriceQty(self, tprice, tqty, cname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tqty = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderPriceDate(self, tprice, tdate, cname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tdate = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tdate, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderPriceStatus(self, tprice, tstatus, cname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tstatus, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderQtyDate(self, tqty, tdate, cname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tdate = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tdate, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderQtyStatus(self, tqty, tstatus, cname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tstatus, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderDateStatus(self, tdate, tstatus, cname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tdate, tstatus, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderPrice(self, tprice, cname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tprice = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderQty(self, tqty, cname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tqty = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderDate(self, tdate, cname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tdate = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tdate, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByCityCategoryOrderStatus(self, tstatus, cname, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from ((transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category) inner join account on sid = aid) natural inner join address natural inner join city where tstatus = %s and cname = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tstatus, cname, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierRequesterResource(self, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourcePriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid, rid,
                                                                        rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourcePriceQtyDate(self, tprice, tqty, tdate, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tprice = %s and tqty = %s and tdate = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourcePriceQtyStatus(self, tprice, tqty, tstatus, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tprice = %s and tqty = %s and tstatus = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourcePriceDateStatus(self, tprice, tdate, tstatus, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tprice = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourceQtyDateStatus(self, tqty, tdate, tstatus, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tqty = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourcePriceQty(self, tprice, tqty, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tprice = %s and tqty = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tqty, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourcePriceDate(self, tprice, tdate, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tprice = %s and tdate = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tdate, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourcePriceStatus(self, tprice, tstatus, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tprice = %s and tstatus = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, tstatus, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourceQtyDate(self, tqty, tdate, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tqty = %s and tdate = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tdate, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourceQtyStatus(self, tqty, tstatus, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tqty = %s and tstatus = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, tstatus, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourceDateStatus(self, tdate, tstatus, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tdate = %s and tstatus = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tdate, tstatus, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourcePrice(self, tprice, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tprice = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tprice, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourceQty(self, tqty, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tqty = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tqty, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourceDate(self, tdate, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tdate = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tdate, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterResourceStatus(self, tstatus, sid, rid, rsid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join requester where tstatus = %s and sid = %s and rid = %s and rsid = %s;"
        cursor.execute(query, (tstatus, sid, rid, rsid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierRequesterKeyword(self, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid, rid,
                                                                       kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordPriceQtyDate(self, tprice, tqty, tdate, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tprice = %s and tqty = %s and tdate = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordPriceQtyStatus(self, tprice, tqty, tstatus, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tprice = %s and tqty = %s and tstatus = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordPriceDateStatus(self, tprice, tdate, tstatus, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tprice = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordQtyDateStatus(self, tqty, tdate, tstatus, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tqty = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordPriceQty(self, tprice, tqty, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tprice = %s and tqty = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordPriceDate(self, tprice, tdate, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tprice = %s and tdate = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordPriceStatus(self, tprice, tstatus, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tprice = %s and tstatus = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordQtyDate(self, tqty, tdate, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tqty = %s and tdate = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordQtyStatus(self, tqty, tstatus, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tqty = %s and tstatus = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordDateStatus(self, tdate, tstatus, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tdate = %s and tstatus = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordPrice(self, tprice, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tprice = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tprice, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordQty(self, tqty, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tqty = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tqty, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordDate(self, tdate, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tdate = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tdate, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterKeywordStatus(self, tstatus, sid, rid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword natural inner join requester where tstatus = %s and sid = %s and rid = %s and kid = %s;"
        cursor.execute(query, (tstatus, sid, rid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierRequesterCategory(self, sid, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid, rid,
                                                                        cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryPriceQtyDate(self, tprice, tqty, tdate, sid, rid, cat_name,
                                                                  cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tprice = %s and tqty = %s and tdate = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryPriceQtyStatus(self, tprice, tqty, tstatus, sid, rid, cat_name,
                                                                    cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tprice = %s and tqty = %s and tstatus = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryPriceDateStatus(self, tprice, tdate, tstatus, sid, rid, cat_name,
                                                                     cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tprice = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryQtyDateStatus(self, tqty, tdate, tstatus, sid, rid, cat_name,
                                                                   cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tqty = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryPriceQty(self, tprice, tqty, sid, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tprice = %s and tqty = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryPriceDate(self, tprice, tdate, sid, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tprice = %s and tdate = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryPriceStatus(self, tprice, tstatus, sid, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tprice = %s and tstatus = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryQtyDate(self, tqty, tdate, sid, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tqty = %s and tdate = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryQtyStatus(self, tqty, tstatus, sid, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tqty = %s and tstatus = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryDateStatus(self, tdate, tstatus, sid, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tdate = %s and tstatus = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryPrice(self, tprice, sid, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tprice = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryQty(self, tqty, sid, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tqty = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryDate(self, tdate, sid, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tdate = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterCategoryStatus(self, tstatus, sid, rid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join requester where tstatus = %s and sid = %s and rid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, sid, rid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierRequesterOrder(self, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderPriceQtyDate(self, tprice, tqty, tdate, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tprice = %s and tqty = %s and tdate = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderPriceQtyStatus(self, tprice, tqty, tstatus, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tprice = %s and tqty = %s and tstatus = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderPriceDateStatus(self, tprice, tdate, tstatus, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tprice = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderQtyDateStatus(self, tqty, tdate, tstatus, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tqty = %s and tdate = %s and tstatus = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderPriceQty(self, tprice, tqty, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tprice = %s and tqty = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderPriceDate(self, tprice, tdate, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tprice = %s and tdate = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderPriceStatus(self, tprice, tstatus, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tprice = %s and tstatus = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderQtyDate(self, tqty, tdate, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tqty = %s and tdate = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderQtyStatus(self, tqty, tstatus, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tqty = %s and tstatus = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderDateStatus(self, tdate, tstatus, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tdate = %s and tstatus = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderPrice(self, tprice, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tprice = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tprice, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderQty(self, tqty, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tqty = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tqty, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderDate(self, tdate, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tdate = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tdate, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierRequesterOrderStatus(self, tstatus, sid, rid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester where tstatus = %s and sid = %s and rid = %s and oid = %s;"
        cursor.execute(query, (tstatus, sid, rid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierResourceKeyword(self, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid, rsid,
                                                                      kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordPriceQtyDate(self, tprice, tqty, tdate, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordPriceQtyStatus(self, tprice, tqty, tstatus, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tstatus = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordPriceDateStatus(self, tprice, tdate, tstatus, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and tstatus = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordQtyDateStatus(self, tqty, tdate, tstatus, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and tstatus = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordPriceQty(self, tprice, tqty, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordPriceDate(self, tprice, tdate, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordPriceStatus(self, tprice, tstatus, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tstatus = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordQtyDate(self, tqty, tdate, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordQtyStatus(self, tqty, tstatus, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tstatus = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordDateStatus(self, tdate, tstatus, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and tstatus = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordPrice(self, tprice, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordQty(self, tqty, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordDate(self, tdate, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tdate, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceKeywordStatus(self, tstatus, sid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tstatus = %s and sid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tstatus, sid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierResourceOrder(self, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderPriceQtyDate(self, tprice, tqty, tdate, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tprice = %s and tqty = %s and tdate = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderPriceQtyStatus(self, tprice, tqty, tstatus, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tprice = %s and tqty = %s and tstatus = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderPriceDateStatus(self, tprice, tdate, tstatus, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tprice = %s and tdate = %s and tstatus = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderQtyDateStatus(self, tqty, tdate, tstatus, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tqty = %s and tdate = %s and tstatus = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderPriceQty(self, tprice, tqty, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tprice = %s and tqty = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderPriceDate(self, tprice, tdate, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tprice = %s and tdate = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderPriceStatus(self, tprice, tstatus, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tprice = %s and tstatus = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderQtyDate(self, tqty, tdate, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tqty = %s and tdate = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderQtyStatus(self, tqty, tstatus, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tqty = %s and tstatus = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderDateStatus(self, tdate, tstatus, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tdate = %s and tstatus = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderPrice(self, tprice, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tprice = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderQty(self, tqty, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tqty = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderDate(self, tdate, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tdate = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tdate, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierResourceOrderStatus(self, tstatus, sid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource where tstatus = %s and sid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tstatus, sid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierKeywordCategory(self, sid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid, kid,
                                                                      cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryPriceQtyDate(self, tprice, tqty, tdate, sid, kid, cat_name,
                                                                cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryPriceQtyStatus(self, tprice, tqty, tstatus, sid, kid, cat_name,
                                                                  cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tstatus = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryPriceDateStatus(self, tprice, tdate, tstatus, sid, kid, cat_name,
                                                                   cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and tstatus = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryQtyDateStatus(self, tqty, tdate, tstatus, sid, kid, cat_name,
                                                                 cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and tstatus = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryPriceQty(self, tprice, tqty, sid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryPriceDate(self, tprice, tdate, sid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryPriceStatus(self, tprice, tstatus, sid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tstatus = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryQtyDate(self, tqty, tdate, sid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryQtyStatus(self, tqty, tstatus, sid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tstatus = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryDateStatus(self, tdate, tstatus, sid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and tstatus = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryPrice(self, tprice, sid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryQty(self, tqty, sid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryDate(self, tdate, sid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordCategoryStatus(self, tstatus, sid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tstatus = %s and sid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, sid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierKeywordOrder(self, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderPriceQtyDate(self, tprice, tqty, tdate, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderPriceQtyStatus(self, tprice, tqty, tstatus, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tstatus = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderPriceDateStatus(self, tprice, tdate, tstatus, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and tstatus = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderQtyDateStatus(self, tqty, tdate, tstatus, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and tstatus = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderPriceQty(self, tprice, tqty, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderPriceDate(self, tprice, tdate, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderPriceStatus(self, tprice, tstatus, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tstatus = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderQtyDate(self, tqty, tdate, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderQtyStatus(self, tqty, tstatus, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tstatus = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderDateStatus(self, tdate, tstatus, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and tstatus = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderPrice(self, tprice, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderQty(self, tqty, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderDate(self, tdate, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tdate, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierKeywordOrderStatus(self, tstatus, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tstatus = %s and sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tstatus, sid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierCategoryOrder(self, sid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, sid, cat_name,
                                                                    cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderPriceQtyDate(self, tprice, tqty, tdate, sid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tprice = %s and tqty = %s and tdate = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderPriceQtyStatus(self, tprice, tqty, tstatus, sid, cat_name, cat_pname,
                                                                oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tprice = %s and tqty = %s and tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderPriceDateStatus(self, tprice, tdate, tstatus, sid, cat_name, cat_pname,
                                                                 oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tprice = %s and tdate = %s and tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderQtyDateStatus(self, tqty, tdate, tstatus, sid, cat_name, cat_pname,
                                                               oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tqty = %s and tdate = %s and tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderPriceQty(self, tprice, tqty, sid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tprice = %s and tqty = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderPriceDate(self, tprice, tdate, sid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tprice = %s and tdate = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tdate, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderPriceStatus(self, tprice, tstatus, sid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tprice = %s and tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tstatus, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderQtyDate(self, tqty, tdate, sid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tqty = %s and tdate = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tdate, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderQtyStatus(self, tqty, tstatus, sid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tqty = %s and tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tstatus, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderDateStatus(self, tdate, tstatus, sid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tdate = %s and tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tdate, tstatus, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderPrice(self, tprice, sid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tprice = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderQty(self, tqty, sid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tqty = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderDate(self, tdate, sid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tdate = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tdate, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsBySupplierCategoryOrderStatus(self, tstatus, sid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join category where tstatus = %s and sid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tstatus, sid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRequesterResourceKeyword(self, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rid, rsid,
                                                                       kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordPriceQtyDate(self, tprice, tqty, tdate, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordPriceQtyStatus(self, tprice, tqty, tstatus, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tstatus = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordPriceDateStatus(self, tprice, tdate, tstatus, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and tstatus = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordQtyDateStatus(self, tqty, tdate, tstatus, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and tstatus = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordPriceQty(self, tprice, tqty, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tqty, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordPriceDate(self, tprice, tdate, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tdate, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordPriceStatus(self, tprice, tstatus, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tstatus = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, tstatus, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordQtyDate(self, tqty, tdate, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tdate, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordQtyStatus(self, tqty, tstatus, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tstatus = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, tstatus, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordDateStatus(self, tdate, tstatus, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and tstatus = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tdate, tstatus, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordPrice(self, tprice, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tprice, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordQty(self, tqty, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tqty, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordDate(self, tdate, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tdate, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceKeywordStatus(self, tstatus, rid, rsid, kid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tstatus = %s and rid = %s and rsid = %s and kid = %s;"
        cursor.execute(query, (tstatus, rid, rsid, kid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRequesterResourceOrder(self, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rid, rsid,
                                                                     oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderPriceQtyDate(self, tprice, tqty, tdate, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and tqty = %s and tdate = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderPriceQtyStatus(self, tprice, tqty, tstatus, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and tqty = %s and tstatus = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderPriceDateStatus(self, tprice, tdate, tstatus, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and tdate = %s and tstatus = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderQtyDateStatus(self, tqty, tdate, tstatus, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tqty = %s and tdate = %s and tstatus = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderPriceQty(self, tprice, tqty, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and tqty = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderPriceDate(self, tprice, tdate, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and tdate = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderPriceStatus(self, tprice, tstatus, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and tstatus = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderQtyDate(self, tqty, tdate, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tqty = %s and tdate = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderQtyStatus(self, tqty, tstatus, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tqty = %s and tstatus = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderDateStatus(self, tdate, tstatus, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tdate = %s and tstatus = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderPrice(self, tprice, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tprice = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tprice, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderQty(self, tqty, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tqty = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tqty, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderDate(self, tdate, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tdate = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tdate, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterResourceOrderStatus(self, tstatus, rid, rsid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource where tstatus = %s and rid = %s and rsid = %s and oid = %s;"
        cursor.execute(query, (tstatus, rid, rsid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRequesterKeywordCategory(self, rid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rid, kid,
                                                                       cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryPriceQtyDate(self, tprice, tqty, tdate, rid, kid, cat_name,
                                                                 cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryPriceQtyStatus(self, tprice, tqty, tstatus, rid, kid, cat_name,
                                                                   cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tstatus = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryPriceDateStatus(self, tprice, tdate, tstatus, rid, kid, cat_name,
                                                                    cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and tstatus = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryQtyDateStatus(self, tqty, tdate, tstatus, rid, kid, cat_name,
                                                                  cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and tstatus = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryPriceQty(self, tprice, tqty, rid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryPriceDate(self, tprice, tdate, rid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryPriceStatus(self, tprice, tstatus, rid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tstatus = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryQtyDate(self, tqty, tdate, rid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryQtyStatus(self, tqty, tstatus, rid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tstatus = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryDateStatus(self, tdate, tstatus, rid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and tstatus = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryPrice(self, tprice, rid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryQty(self, tqty, rid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryDate(self, tdate, rid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordCategoryStatus(self, tstatus, rid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join requester natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tstatus = %s and rid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, rid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRequesterKeywordOrder(self, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderPriceQtyDate(self, tprice, tqty, tdate, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderPriceQtyStatus(self, tprice, tqty, tstatus, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tstatus = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderPriceDateStatus(self, tprice, tdate, tstatus, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and tstatus = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderQtyDateStatus(self, tqty, tdate, tstatus, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and tstatus = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderPriceQty(self, tprice, tqty, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tqty, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderPriceDate(self, tprice, tdate, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tdate, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderPriceStatus(self, tprice, tstatus, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tstatus = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, tstatus, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderQtyDate(self, tqty, tdate, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tdate, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderQtyStatus(self, tqty, tstatus, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tstatus = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, tstatus, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderDateStatus(self, tdate, tstatus, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and tstatus = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tdate, tstatus, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderPrice(self, tprice, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tprice, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderQty(self, tqty, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tqty, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderDate(self, tdate, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tdate, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterKeywordOrderStatus(self, tstatus, rid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tstatus = %s and rid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (tstatus, rid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByRequesterCategoryOrder(self, rid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rid, cat_name,
                                                                     cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderPriceQtyDate(self, tprice, tqty, tdate, rid, cat_name, cat_pname,
                                                               oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and tqty = %s and tdate = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderPriceQtyStatus(self, tprice, tqty, tstatus, rid, cat_name, cat_pname,
                                                                 oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and tqty = %s and tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderPriceDateStatus(self, tprice, tdate, tstatus, rid, cat_name,
                                                                  cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and tdate = %s and tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderQtyDateStatus(self, tqty, tdate, tstatus, rid, cat_name, cat_pname,
                                                                oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tqty = %s and tdate = %s and tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderPriceQty(self, tprice, tqty, rid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and tqty = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderPriceDate(self, tprice, tdate, rid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and tdate = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tdate, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderPriceStatus(self, tprice, tstatus, rid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tstatus, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderQtyDate(self, tqty, tdate, rid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tqty = %s and tdate = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tdate, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderQtyStatus(self, tqty, tstatus, rid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tqty = %s and tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tstatus, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderDateStatus(self, tdate, tstatus, rid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tdate = %s and tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tdate, tstatus, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderPrice(self, tprice, rid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tprice = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderQty(self, tqty, rid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tqty = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderDate(self, tdate, rid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tdate = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tdate, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByRequesterCategoryOrderStatus(self, tstatus, rid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join requester natural inner join resource natural inner join category where tstatus = %s and rid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tstatus, rid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByResourceKeywordCategory(self, rsid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rsid, kid,
                                                                      cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryPriceQtyDate(self, tprice, tqty, tdate, rsid, kid, cat_name,
                                                                cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tdate, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryPriceQtyStatus(self, tprice, tqty, tstatus, rsid, kid, cat_name,
                                                                  cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tstatus = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, tstatus, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryPriceDateStatus(self, tprice, tdate, tstatus, rsid, kid, cat_name,
                                                                   cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and tstatus = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, tstatus, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryQtyDateStatus(self, tqty, tdate, tstatus, rsid, kid, cat_name,
                                                                 cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and tstatus = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, tstatus, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryPriceQty(self, tprice, tqty, rsid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tqty, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryPriceDate(self, tprice, tdate, rsid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tdate, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryPriceStatus(self, tprice, tstatus, rsid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tstatus = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, tstatus, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryQtyDate(self, tqty, tdate, rsid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tdate, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryQtyStatus(self, tqty, tstatus, rsid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tstatus = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, tstatus, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryDateStatus(self, tdate, tstatus, rsid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and tstatus = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, tstatus, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryPrice(self, tprice, rsid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tprice, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryQty(self, tqty, rsid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tqty, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryDate(self, tdate, rsid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tdate, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordCategoryStatus(self, tstatus, rsid, kid, cat_name, cat_pname):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join supplier natural inner join resource natural inner join category natural inner join ResourceHasKeyword natural inner join keyword where tstatus = %s and rsid = %s and kid = %s and (cat_name = %s or cat_pname = %s);"
        cursor.execute(query, (tstatus, rsid, kid, cat_name, cat_pname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByResourceKeywordOrder(self, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderPriceQtyDate(self, tprice, tqty, tdate, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tdate = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tprice, tqty, tdate, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderPriceQtyStatus(self, tprice, tqty, tstatus, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and tstatus = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tprice, tqty, tstatus, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderPriceDateStatus(self, tprice, tdate, tstatus, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and tstatus = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tprice, tdate, tstatus, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderQtyDateStatus(self, tqty, tdate, tstatus, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and tstatus = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tqty, tdate, tstatus, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderPriceQty(self, tprice, tqty, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tqty = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tprice, tqty, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderPriceDate(self, tprice, tdate, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tdate = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tprice, tdate, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderPriceStatus(self, tprice, tstatus, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and tstatus = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tprice, tstatus, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderQtyDate(self, tqty, tdate, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tdate = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tqty, tdate, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderQtyStatus(self, tqty, tstatus, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and tstatus = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tqty, tstatus, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderDateStatus(self, tdate, tstatus, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and tstatus = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tdate, tstatus, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderPrice(self, tprice, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tprice = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tprice, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderQty(self, tqty, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tqty = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tqty, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderDate(self, tdate, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tdate = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tdate, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByResourceKeywordOrderStatus(self, tstatus, rsid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join supplier natural inner join resource natural inner join ResourceHasKeyword natural inner join keyword where tstatus = %s and rsid = %s and kid = %s and oid =%s;"
        cursor.execute(query, (tstatus, rsid, kid, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByKeywordCategoryOrder(self, kid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderPriceQtyDateStatus(self, tprice, tqty, tdate, tstatus, kid, cat_name,
                                                                   cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and tqty = %s and tdate = %s and tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, tstatus, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderPriceQtyDate(self, tprice, tqty, tdate, kid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and tqty = %s and tdate = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tdate, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderPriceQtyStatus(self, tprice, tqty, tstatus, kid, cat_name, cat_pname,
                                                               oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and tqty = %s and tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, tstatus, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderPriceDateStatus(self, tprice, tdate, tstatus, kid, cat_name, cat_pname,
                                                                oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and tdate = %s and tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tdate, tstatus, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderQtyDateStatus(self, tqty, tdate, tstatus, kid, cat_name, cat_pname,
                                                              oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tqty = %s and tdate = %s and tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tdate, tstatus, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderPriceQty(self, tprice, tqty, kid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and tqty = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tqty, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderPriceDate(self, tprice, tdate, kid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and tdate = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tdate, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderPriceStatus(self, tprice, tstatus, kid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, tstatus, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderQtyDate(self, tqty, tdate, kid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tqty = %s and tdate = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tdate, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderQtyStatus(self, tqty, tstatus, kid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tqty = %s and tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, tstatus, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderDateStatus(self, tdate, tstatus, kid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tdate = %s and tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tdate, tstatus, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderPrice(self, tprice, kid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tprice = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tprice, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderQty(self, tqty, kid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tqty = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tqty, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderDate(self, tdate, kid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tdate = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tdate, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTransactionsByKeywordCategoryOrderStatus(self, tstatus, kid, cat_name, cat_pname, oid):
        cursor = self.conn.cursor()
        query = "Select tid, tprice, tqty, tdate, tstatus from transaction natural inner join Order_Info natural inner join resource natural inner join supplier natural inner join ResourceHasKeyword natural inner join keyword natural inner join category where tstatus = %s and kid = %s and (cat_name = %s or cat_pname = %s) and oid = %s;"
        cursor.execute(query, (tstatus, kid, cat_name, cat_pname, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

















