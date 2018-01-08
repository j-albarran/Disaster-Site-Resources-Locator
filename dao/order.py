from config.dbconfig import pg_config
import psycopg2

class OrderDAO:
    def __init__(self):

        connection_url = "dbname=%s host=%s port=%s user=%s password=%s sslmode=%s" % (
        pg_config['dbname'], pg_config['host'],
        pg_config['port'], pg_config['user'],
        pg_config['password'], pg_config['sslmode'])

        self.conn = psycopg2._connect(connection_url)

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

