from config.dbconfig import conn

class OrderDAO:
    def __init__(self):
        self.conn = conn

    def getAllOrders(self):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByDatePriceStatus(self,odate,oprice,ostatus):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where odate = %s and oprice = %s and ostatus = %s;"
        cursor.execute(query, ( odate, oprice, ostatus,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByDatePrice(self,odate,oprice):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where odate = %s and oprice = %s;"
        cursor.execute(query, ( odate, oprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByDateStatus(self,odate,ostatus):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where odate = %s and ostatus = %s;"
        cursor.execute(query, ( odate, ostatus,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByPriceStatus(self,oprice,ostatus):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where oprice = %s and ostatus = %s;"
        cursor.execute(query, ( oprice, ostatus,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByDate(self,odate):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where odate = %s;"
        cursor.execute(query, ( odate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByPrice(self,oprice):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where oprice = %s;"
        cursor.execute(query, ( oprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByStatus(self,ostatus):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where ostatus = %s;"
        cursor.execute(query, ( ostatus,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderById(self, oid):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where oid = %s;"
        cursor.execute(query, (oid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByIdDatePriceStatus(self,odate,oprice,ostatus, oid):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where odate = %s and oprice = %s and ostatus = %s and oid = %s;"
        cursor.execute(query, ( odate, oprice, ostatus, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByIdDatePrice(self,odate,oprice, oid):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where odate = %s and oprice = %s and oid = %s;"
        cursor.execute(query, ( odate, oprice, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByIdDateStatus(self,odate,ostatus, oid):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where odate = %s and ostatus = %s and oid = %s;"
        cursor.execute(query, ( odate, ostatus, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByIdPriceStatus(self,oprice,ostatus, oid):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where oprice = %s and ostatus = %s and oid = %s;"
        cursor.execute(query, ( oprice, ostatus, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByIdDate(self,odate, oid):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where odate = %s and oid = %s;"
        cursor.execute(query, ( odate, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByIdPrice(self,oprice, oid):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where oprice = %s and oid = %s;"
        cursor.execute(query, ( oprice, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByIdStatus(self,ostatus, oid):
        cursor = self.conn.cursor()
        query = "Select oid, odate, oprice, ostatus from Order_Info where ostatus = %s and oid = %s;"
        cursor.execute(query, ( ostatus, oid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByRequester(self, rid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join requester where rid = %s;"
        cursor.execute(query, (rid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByRequesterDatePriceStatus(self,odate,oprice,ostatus, rid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join requester where odate = %s and oprice = %s and ostatus = %s and rid = %s;"
        cursor.execute(query, ( odate, oprice, ostatus, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByRequesterDatePrice(self,odate,oprice, rid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join requester where odate = %s and oprice = %s and rid = %s;"
        cursor.execute(query, ( odate, oprice, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByRequesterDateStatus(self,odate,ostatus, rid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join requester where odate = %s and ostatus = %s and rid = %s;"
        cursor.execute(query, ( odate, ostatus, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByRequesterPriceStatus(self,oprice,ostatus, rid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join requester where oprice = %s and ostatus = %s and rid = %s"
        cursor.execute(query, ( oprice, ostatus, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByRequesterDate(self,odate, rid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join requester where odate = %s and rid = %s;"
        cursor.execute(query, ( odate, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByRequesterPrice(self,oprice, rid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join requester where oprice = %s and rid = %s;"
        cursor.execute(query, ( oprice, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByRequesterStatus(self,ostatus, rid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join requester where ostatus = %s and rid = %s;"
        cursor.execute(query, ( ostatus, rid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersBySupplier(self, sid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join supplier where sid = %s;"
        cursor.execute(query, (sid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersBySupplierDatePriceStatus(self,odate,oprice,ostatus, sid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join supplier where odate = %s and oprice = %s and ostatus = %s and sid = %s;"
        cursor.execute(query, ( odate, oprice, ostatus, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersBySupplierDatePrice(self,odate,oprice, sid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join supplier where odate = %s and oprice = %s and sid = %s;"
        cursor.execute(query, ( odate, oprice, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersBySupplierDateStatus(self,odate,ostatus, sid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join supplier where odate = %s and ostatus = %s and sid = %s;"
        cursor.execute(query, ( odate, ostatus, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersBySupplierPriceStatus(self,oprice,ostatus, sid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join supplier where oprice = %s and ostatus = %s and sid = %s"
        cursor.execute(query, ( oprice, ostatus, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersBySupplierDate(self,odate, sid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join supplier where odate = %s and sid = %s;"
        cursor.execute(query, ( odate, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersBySupplierPrice(self,oprice, sid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join supplier where oprice = %s and sid = %s;"
        cursor.execute(query, ( oprice, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersBySupplierStatus(self,ostatus, sid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction natural inner join supplier where ostatus = %s and sid = %s;"
        cursor.execute(query, ( ostatus, sid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByTransaction(self, tid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction where tid = %s;"
        cursor.execute(query, (tid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByTransactionDatePriceStatus(self,odate,oprice,ostatus, tid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction where odate = %s and oprice = %s and ostatus = %s and tid = %s;"
        cursor.execute(query, ( odate, oprice, ostatus, tid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByTransactionDatePrice(self,odate,oprice, tid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction where odate = %s and oprice = %s and tid = %s;"
        cursor.execute(query, ( odate, oprice, tid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByTransactionDateStatus(self,odate,ostatus, tid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction where odate = %s and ostatus = %s and tid = %s;"
        cursor.execute(query, ( odate, ostatus, tid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByTransactionPriceStatus(self,oprice,ostatus, tid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction where oprice = %s and ostatus = %s and tid = %s"
        cursor.execute(query, ( oprice, ostatus, tid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByTransactionDate(self,odate, tid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction where odate = %s and tid = %s;"
        cursor.execute(query, ( odate, tid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByTransactionPrice(self,oprice, tid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction where oprice = %s and tid = %s;"
        cursor.execute(query, ( oprice, tid))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOrdersByTransactionStatus(self,ostatus, tid):
        cursor = self.conn.cursor()
        query = "Select distinct oid, odate, oprice, ostatus from Order_Info natural inner join transaction where ostatus = %s and tid = %s;"
        cursor.execute(query, ( ostatus, tid))
        result = []
        for row in cursor:
            result.append(row)
        return result
