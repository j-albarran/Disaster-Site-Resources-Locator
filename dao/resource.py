from config.dbconfig import pg_config
import psycopg2

class ResourceDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (self, pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(self, connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNameChangedDateQtyPriceSupplyDate(self, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNameChangedDateQtyPrice(self, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNameChangedDateQtySupplyDate(self, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNameChangedDatePriceSupplyDate(self, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNameQtyPriceSupplyDate(self, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByChangedDateQtyPriceSupplyDate(self, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNameChangedDateQty(self, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNameChangedDatePrice(self, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNameChangedDateSupplyDate(self, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNameQtyPrice(self, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNameQtySupplyDate(self, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNamePriceSupplyDate(self, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByChangedDateQtyPrice(self, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByChangedDateQtySupplyDate(self, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByChangedDatePriceSupplyDate(self, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByQtyPriceSupplyDate(self, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNameChangedDate(self, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNameQty(self, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and rqty = %s;"
        cursor.execute(query, (rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNamePrice(self, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and rprice = %s;"
        cursor.execute(query, (rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByNameSupplyDate(self, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByChangedDateQty(self, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByChangedDatePrice(self, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByChangedDateSupplyDate(self, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByQtyPrice(self, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rqty = %s and rprice = %s;"
        cursor.execute(query, (rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByQtySupplyDate(self, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByPriceSupplyDate(self, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByName(self, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rsname = %s;"
        cursor.execute(query, (rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByChangedDate(self, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where r_changed_date = %s;"
        cursor.execute(query, (r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByQty(self, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rqty = %s;"
        cursor.execute(query, (rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByPrice(self, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where rprice = %s;"
        cursor.execute(query, (rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceBySupplyDate(self, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource where r_supply_date = %s;"
        cursor.execute(query, (r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceById(self, rsid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource;"
        cursor.execute(query, (rsid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "insert into Resource(rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date) values (%s, %s, %s, %s, %s, %s) returning rsid;"
        cursor.execute(query, (rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date,))
        rsid = cursor.fetchone()[0]
        self.conn.commit()
        return rsid

    def update(self, rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "update Resource set rsname = %s rdescription = %s r_changed_date = %s rqty = %s where rsid = %s;"
        cursor.execute(query, (rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date, rsid,))
        self.conn.commit()
        return rsid

    def delete(self, rsid):
        cursor = self.conn.cursor()
        query = "delete from Resource where rsid = %s;"
        cursor.execute(query, (rsid,))
        self.conn.commit()
        return rsid

    def getResourcesByCityName(self, cname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s;"
        cursor.execute(query, (cname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNameChangedDateQtyPriceSupplyDate(self, cname, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNameChangedDateQtyPrice(self, cname, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNameChangedDateQtySupplyDate(self, cname, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNameChangedDatePriceSupplyDate(self, cname, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNameQtyPriceSupplyDate(self, cname, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByChangedDateQtyPriceSupplyDate(self, cname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNameChangedDateQty(self, cname, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cname, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNameChangedDatePrice(self, cname, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cname, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNameChangedDateSupplyDate(self, cname, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNameQtyPrice(self, cname, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNameQtySupplyDate(self, cname, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNamePriceSupplyDate(self, cname, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByChangedDateQtyPrice(self, cname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByChangedDateQtySupplyDate(self, cname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByChangedDatePriceSupplyDate(self, cname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByQtyPriceSupplyDate(self, cname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNameChangedDate(self, cname, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (cname, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNameQty(self, cname, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (cname, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNamePrice(self, cname, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (cname, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByNameSupplyDate(self, cname, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByChangedDateQty(self, cname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByChangedDatePrice(self, cname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByChangedDateSupplyDate(self, cname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByQtyPrice(self, cname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByQtySupplyDate(self, cname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByPriceSupplyDate(self, cname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByName(self, cname, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rsname = %s;"
        cursor.execute(query, (cname, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByChangedDate(self, cname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and r_changed_date = %s;"
        cursor.execute(query, (cname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByQty(self, cname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rqty = %s;"
        cursor.execute(query, (cname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameByPrice(self, cname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and rprice = %s;"
        cursor.execute(query, (cname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityNameBySupplyDate(self, cname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address where cname = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionName(self, rname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNameChangedDateQtyPriceSupplyDate(self, rname, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNameChangedDateQtyPrice(self, rname, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNameChangedDateQtySupplyDate(self, rname, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNameChangedDatePriceSupplyDate(self, rname, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNameQtyPriceSupplyDate(self, rname, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByChangedDateQtyPriceSupplyDate(self, rname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNameChangedDateQty(self, rname, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (rname, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNameChangedDatePrice(self, rname, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (rname, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNameChangedDateSupplyDate(self, rname, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNameQtyPrice(self, rname, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNameQtySupplyDate(self, rname, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNamePriceSupplyDate(self, rname, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByChangedDateQtyPrice(self, rname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByChangedDateQtySupplyDate(self, rname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByChangedDatePriceSupplyDate(self, rname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByQtyPriceSupplyDate(self, rname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNameChangedDate(self, rname, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (rname, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNameQty(self, rname, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (rname, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNamePrice(self, rname, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (rname, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByNameSupplyDate(self, rname, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByChangedDateQty(self, rname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (rname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByChangedDatePrice(self, rname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (rname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByChangedDateSupplyDate(self, rname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByQtyPrice(self, rname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByQtySupplyDate(self, rname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByPriceSupplyDate(self, rname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByName(self, rname, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rsname = %s;"
        cursor.execute(query, (rname, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByChangedDate(self, rname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and r_changed_date = %s;"
        cursor.execute(query, (rname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByQty(self, rname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rqty = %s;"
        cursor.execute(query, (rname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameByPrice(self, rname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and rprice = %s;"
        cursor.execute(query, (rname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionNameBySupplyDate(self, rname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City where rname = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNameChangedDateQtyPriceSupplyDate(self, sid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNameChangedDateQtyPrice(self, sid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNameChangedDateQtySupplyDate(self, sid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNameChangedDatePriceSupplyDate(self, sid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNameQtyPriceSupplyDate(self, sid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByChangedDateQtyPriceSupplyDate(self, sid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNameChangedDateQty(self, sid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (sid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNameChangedDatePrice(self, sid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (sid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNameChangedDateSupplyDate(self, sid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNameQtyPrice(self, sid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNameQtySupplyDate(self, sid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNamePriceSupplyDate(self, sid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByChangedDateQtyPrice(self, sid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByChangedDateQtySupplyDate(self, sid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByChangedDatePriceSupplyDate(self, sid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByQtyPriceSupplyDate(self, sid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNameChangedDate(self, sid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (sid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNameQty(self, sid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (sid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNamePrice(self, sid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (sid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByNameSupplyDate(self, sid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByChangedDateQty(self, sid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (sid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByChangedDatePrice(self, sid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (sid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByChangedDateSupplyDate(self, sid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByQtyPrice(self, sid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByQtySupplyDate(self, sid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByPriceSupplyDate(self, sid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByName(self, sid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rsname = %s;"
        cursor.execute(query, (sid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByChangedDate(self, sid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and r_changed_date = %s;"
        cursor.execute(query, (sid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByQty(self, sid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rqty = %s;"
        cursor.execute(query, (sid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdByPrice(self, sid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and rprice = %s;"
        cursor.execute(query, (sid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierIdBySupplyDate(self, sid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier where sid = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordId(self, kid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s;"
        cursor.execute(query, (kid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNameChangedDateQtyPriceSupplyDate(self, kid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNameChangedDateQtyPrice(self, kid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNameChangedDateQtySupplyDate(self, kid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNameChangedDatePriceSupplyDate(self, kid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNameQtyPriceSupplyDate(self, kid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByChangedDateQtyPriceSupplyDate(self, kid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNameChangedDateQty(self, kid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (kid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNameChangedDatePrice(self, kid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (kid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNameChangedDateSupplyDate(self, kid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNameQtyPrice(self, kid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNameQtySupplyDate(self, kid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNamePriceSupplyDate(self, kid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByChangedDateQtyPrice(self, kid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByChangedDateQtySupplyDate(self, kid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByChangedDatePriceSupplyDate(self, kid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByQtyPriceSupplyDate(self, kid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNameChangedDate(self, kid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (kid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNameQty(self, kid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (kid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNamePrice(self, kid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (kid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByNameSupplyDate(self, kid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByChangedDateQty(self, kid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (kid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByChangedDatePrice(self, kid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (kid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByChangedDateSupplyDate(self, kid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByQtyPrice(self, kid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByQtySupplyDate(self, kid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByPriceSupplyDate(self, kid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByName(self, kid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rsname = %s;"
        cursor.execute(query, (kid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByChangedDate(self, kid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and r_changed_date = %s;"
        cursor.execute(query, (kid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByQty(self, kid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rqty = %s;"
        cursor.execute(query, (kid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdByPrice(self, kid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and rprice = %s;"
        cursor.execute(query, (kid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordIdBySupplyDate(self, kid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword where kid = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryName(self, cat_name):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s;"
        cursor.execute(query, (cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNameChangedDateQtyPriceSupplyDate(self, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNameChangedDateQtyPrice(self, cat_name, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cat_name, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNameChangedDateQtySupplyDate(self, cat_name, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNameChangedDatePriceSupplyDate(self, cat_name, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNameQtyPriceSupplyDate(self, cat_name, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByChangedDateQtyPriceSupplyDate(self, cat_name, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNameChangedDateQty(self, cat_name, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cat_name, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNameChangedDatePrice(self, cat_name, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cat_name, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNameChangedDateSupplyDate(self, cat_name, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNameQtyPrice(self, cat_name, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cat_name, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNameQtySupplyDate(self, cat_name, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNamePriceSupplyDate(self, cat_name, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByChangedDateQtyPrice(self, cat_name, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cat_name, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByChangedDateQtySupplyDate(self, cat_name, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByChangedDatePriceSupplyDate(self, cat_name, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByQtyPriceSupplyDate(self, cat_name, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNameChangedDate(self, cat_name, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (cat_name, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNameQty(self, cat_name, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (cat_name, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNamePrice(self, cat_name, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (cat_name, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByNameSupplyDate(self, cat_name, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByChangedDateQty(self, cat_name, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cat_name, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByChangedDatePrice(self, cat_name, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cat_name, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByChangedDateSupplyDate(self, cat_name, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByQtyPrice(self, cat_name, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cat_name, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByQtySupplyDate(self, cat_name, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByPriceSupplyDate(self, cat_name, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByName(self, cat_name, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rsname = %s;"
        cursor.execute(query, (cat_name, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByChangedDate(self, cat_name, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and r_changed_date = %s;"
        cursor.execute(query, (cat_name, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByQty(self, cat_name, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rqty = %s;"
        cursor.execute(query, (cat_name, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameByPrice(self, cat_name, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and rprice = %s;"
        cursor.execute(query, (cat_name, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryNameBySupplyDate(self, cat_name, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category where cat_name = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionId(self, tid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s;"
        cursor.execute(query, (tid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNameChangedDateQtyPriceSupplyDate(self, tid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNameChangedDateQtyPrice(self, tid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (tid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNameChangedDateQtySupplyDate(self, tid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNameChangedDatePriceSupplyDate(self, tid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNameQtyPriceSupplyDate(self, tid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByChangedDateQtyPriceSupplyDate(self, tid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNameChangedDateQty(self, tid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (tid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNameChangedDatePrice(self, tid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (tid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNameChangedDateSupplyDate(self, tid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNameQtyPrice(self, tid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (tid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNameQtySupplyDate(self, tid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNamePriceSupplyDate(self, tid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByChangedDateQtyPrice(self, tid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (tid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByChangedDateQtySupplyDate(self, tid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByChangedDatePriceSupplyDate(self, tid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByQtyPriceSupplyDate(self, tid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNameChangedDate(self, tid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (tid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNameQty(self, tid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (tid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNamePrice(self, tid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (tid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByNameSupplyDate(self, tid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByChangedDateQty(self, tid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (tid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByChangedDatePrice(self, tid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (tid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByChangedDateSupplyDate(self, tid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByQtyPrice(self, tid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (tid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByQtySupplyDate(self, tid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByPriceSupplyDate(self, tid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByName(self, tid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rsname = %s;"
        cursor.execute(query, (tid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByChangedDate(self, tid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and r_changed_date = %s;"
        cursor.execute(query, (tid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByQty(self, tid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rqty = %s;"
        cursor.execute(query, (tid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdByPrice(self, tid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and rprice = %s;"
        cursor.execute(query, (tid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionIdBySupplyDate(self, tid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderId(self, oid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s;"
        cursor.execute(query, (oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNameChangedDateQtyPriceSupplyDate(self, oid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNameChangedDateQtyPrice(self, oid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (oid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNameChangedDateQtySupplyDate(self, oid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNameChangedDatePriceSupplyDate(self, oid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNameQtyPriceSupplyDate(self, oid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByChangedDateQtyPriceSupplyDate(self, oid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNameChangedDateQty(self, oid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (oid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNameChangedDatePrice(self, oid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (oid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNameChangedDateSupplyDate(self, oid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNameQtyPrice(self, oid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (oid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNameQtySupplyDate(self, oid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNamePriceSupplyDate(self, oid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByChangedDateQtyPrice(self, oid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (oid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByChangedDateQtySupplyDate(self, oid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByChangedDatePriceSupplyDate(self, oid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByQtyPriceSupplyDate(self, oid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNameChangedDate(self, oid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (oid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNameQty(self, oid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (oid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNamePrice(self, oid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (oid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByNameSupplyDate(self, oid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByChangedDateQty(self, oid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (oid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByChangedDatePrice(self, oid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (oid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByChangedDateSupplyDate(self, oid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByQtyPrice(self, oid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (oid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByQtySupplyDate(self, oid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByPriceSupplyDate(self, oid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByName(self, oid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rsname = %s;"
        cursor.execute(query, (oid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByChangedDate(self, oid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and r_changed_date = %s;"
        cursor.execute(query, (oid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByQty(self, oid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rqty = %s;"
        cursor.execute(query, (oid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdByPrice(self, oid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and rprice = %s;"
        cursor.execute(query, (oid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByOrderIdBySupplyDate(self, oid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where oid = %s and r_supply_date = %s;"
        cursor.execute(query, (oid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeyword(self, cname, kid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s;"
        cursor.execute(query, (cname, kid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNameChangedDateQtyPriceSupplyDate(self, cname, kid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNameChangedDateQtyPrice(self, cname, kid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNameChangedDateQtySupplyDate(self, cname, kid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNameChangedDatePriceSupplyDate(self, cname, kid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNameQtyPriceSupplyDate(self, cname, kid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByChangedDateQtyPriceSupplyDate(self, cname, kid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNameChangedDateQty(self, cname, kid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cname, kid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNameChangedDatePrice(self, cname, kid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNameChangedDateSupplyDate(self, cname, kid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNameQtyPrice(self, cname, kid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNameQtySupplyDate(self, cname, kid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNamePriceSupplyDate(self, cname, kid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByChangedDateQtyPrice(self, cname, kid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByChangedDateQtySupplyDate(self, cname, kid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByChangedDatePriceSupplyDate(self, cname, kid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByQtyPriceSupplyDate(self, cname, kid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNameChangedDate(self, cname, kid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (cname, kid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNameQty(self, cname, kid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (cname, kid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNamePrice(self, cname, kid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByNameSupplyDate(self, cname, kid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByChangedDateQty(self, cname, kid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cname, kid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByChangedDatePrice(self, cname, kid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByChangedDateSupplyDate(self, cname, kid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByQtyPrice(self, cname, kid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByQtySupplyDate(self, cname, kid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByPriceSupplyDate(self, cname, kid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByName(self, cname, kid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rsname = %s;"
        cursor.execute(query, (cname, kid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByChangedDate(self, cname, kid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and r_changed_date = %s;"
        cursor.execute(query, (cname, kid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByQty(self, cname, kid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rqty = %s;"
        cursor.execute(query, (cname, kid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordByPrice(self, cname, kid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordBySupplyDate(self, cname, kid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword where cname = %s and kid = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategory(self, cname, cat_name):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s;"
        cursor.execute(query, (cname, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNameChangedDateQtyPriceSupplyDate(self, cname, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNameChangedDateQtyPrice(self, cname, cat_name, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNameChangedDateQtySupplyDate(self, cname, cat_name, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNameChangedDatePriceSupplyDate(self, cname, cat_name, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNameQtyPriceSupplyDate(self, cname, cat_name, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByChangedDateQtyPriceSupplyDate(self, cname, cat_name, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNameChangedDateQty(self, cname, cat_name, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cname, cat_name, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNameChangedDatePrice(self, cname, cat_name, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNameChangedDateSupplyDate(self, cname, cat_name, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNameQtyPrice(self, cname, cat_name, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNameQtySupplyDate(self, cname, cat_name, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNamePriceSupplyDate(self, cname, cat_name, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByChangedDateQtyPrice(self, cname, cat_name, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByChangedDateQtySupplyDate(self, cname, cat_name, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByChangedDatePriceSupplyDate(self, cname, cat_name, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByQtyPriceSupplyDate(self, cname, cat_name, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNameChangedDate(self, cname, cat_name, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (cname, cat_name, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNameQty(self, cname, cat_name, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (cname, cat_name, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNamePrice(self, cname, cat_name, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByNameSupplyDate(self, cname, cat_name, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByChangedDateQty(self, cname, cat_name, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cname, cat_name, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByChangedDatePrice(self, cname, cat_name, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByChangedDateSupplyDate(self, cname, cat_name, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByQtyPrice(self, cname, cat_name, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByQtySupplyDate(self, cname, cat_name, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByPriceSupplyDate(self, cname, cat_name, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByName(self, cname, cat_name, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rsname = %s;"
        cursor.execute(query, (cname, cat_name, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByChangedDate(self, cname, cat_name, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and r_changed_date = %s;"
        cursor.execute(query, (cname, cat_name, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByQty(self, cname, cat_name, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rqty = %s;"
        cursor.execute(query, (cname, cat_name, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryByPrice(self, cname, cat_name, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryBySupplyDate(self, cname, cat_name, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category where cname = %s and cat_name = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeyword(self, rname, kid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s;"
        cursor.execute(query, (rname, kid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNameChangedDateQtyPriceSupplyDate(self, rname, kid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNameChangedDateQtyPrice(self, rname, kid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNameChangedDateQtySupplyDate(self, rname, kid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNameChangedDatePriceSupplyDate(self, rname, kid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNameQtyPriceSupplyDate(self, rname, kid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByChangedDateQtyPriceSupplyDate(self, rname, kid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNameChangedDateQty(self, rname, kid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (rname, kid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNameChangedDatePrice(self, rname, kid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNameChangedDateSupplyDate(self, rname, kid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNameQtyPrice(self, rname, kid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNameQtySupplyDate(self, rname, kid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNamePriceSupplyDate(self, rname, kid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByChangedDateQtyPrice(self, rname, kid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByChangedDateQtySupplyDate(self, rname, kid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByChangedDatePriceSupplyDate(self, rname, kid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByQtyPriceSupplyDate(self, rname, kid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNameChangedDate(self, rname, kid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (rname, kid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNameQty(self, rname, kid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (rname, kid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNamePrice(self, rname, kid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByNameSupplyDate(self, rname, kid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByChangedDateQty(self, rname, kid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (rname, kid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByChangedDatePrice(self, rname, kid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByChangedDateSupplyDate(self, rname, kid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByQtyPrice(self, rname, kid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByQtySupplyDate(self, rname, kid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByPriceSupplyDate(self, rname, kid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByName(self, rname, kid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rsname = %s;"
        cursor.execute(query, (rname, kid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByChangedDate(self, rname, kid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and r_changed_date = %s;"
        cursor.execute(query, (rname, kid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByQty(self, rname, kid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rqty = %s;"
        cursor.execute(query, (rname, kid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordByPrice(self, rname, kid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordBySupplyDate(self, rname, kid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword where rname = %s and kid = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategory(self, rname, cat_name):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s;"
        cursor.execute(query, (rname, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNameChangedDateQtyPriceSupplyDate(self, rname, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNameChangedDateQtyPrice(self, rname, cat_name, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNameChangedDateQtySupplyDate(self, rname, cat_name, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNameChangedDatePriceSupplyDate(self, rname, cat_name, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNameQtyPriceSupplyDate(self, rname, cat_name, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByChangedDateQtyPriceSupplyDate(self, rname, cat_name, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNameChangedDateQty(self, rname, cat_name, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (rname, cat_name, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNameChangedDatePrice(self, rname, cat_name, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNameChangedDateSupplyDate(self, rname, cat_name, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNameQtyPrice(self, rname, cat_name, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNameQtySupplyDate(self, rname, cat_name, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNamePriceSupplyDate(self, rname, cat_name, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByChangedDateQtyPrice(self, rname, cat_name, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByChangedDateQtySupplyDate(self, rname, cat_name, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByChangedDatePriceSupplyDate(self, rname, cat_name, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByQtyPriceSupplyDate(self, rname, cat_name, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNameChangedDate(self, rname, cat_name, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (rname, cat_name, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNameQty(self, rname, cat_name, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (rname, cat_name, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNamePrice(self, rname, cat_name, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByNameSupplyDate(self, rname, cat_name, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByChangedDateQty(self, rname, cat_name, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (rname, cat_name, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByChangedDatePrice(self, rname, cat_name, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByChangedDateSupplyDate(self, rname, cat_name, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByQtyPrice(self, rname, cat_name, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByQtySupplyDate(self, rname, cat_name, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByPriceSupplyDate(self, rname, cat_name, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByName(self, rname, cat_name, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rsname = %s;"
        cursor.execute(query, (rname, cat_name, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByChangedDate(self, rname, cat_name, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and r_changed_date = %s;"
        cursor.execute(query, (rname, cat_name, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByQty(self, rname, cat_name, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rqty = %s;"
        cursor.execute(query, (rname, cat_name, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryByPrice(self, rname, cat_name, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryBySupplyDate(self, rname, cat_name, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category where rname = %s and cat_name = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeyword(self, sid, kid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s;"
        cursor.execute(query, (sid, kid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNameChangedDateQtyPriceSupplyDate(self, sid, kid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNameChangedDateQtyPrice(self, sid, kid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNameChangedDateQtySupplyDate(self, sid, kid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNameChangedDatePriceSupplyDate(self, sid, kid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNameQtyPriceSupplyDate(self, sid, kid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByChangedDateQtyPriceSupplyDate(self, sid, kid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNameChangedDateQty(self, sid, kid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (sid, kid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNameChangedDatePrice(self, sid, kid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNameChangedDateSupplyDate(self, sid, kid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNameQtyPrice(self, sid, kid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNameQtySupplyDate(self, sid, kid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNamePriceSupplyDate(self, sid, kid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByChangedDateQtyPrice(self, sid, kid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByChangedDateQtySupplyDate(self, sid, kid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByChangedDatePriceSupplyDate(self, sid, kid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByQtyPriceSupplyDate(self, sid, kid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNameChangedDate(self, sid, kid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (sid, kid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNameQty(self, sid, kid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (sid, kid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNamePrice(self, sid, kid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByNameSupplyDate(self, sid, kid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByChangedDateQty(self, sid, kid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (sid, kid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByChangedDatePrice(self, sid, kid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByChangedDateSupplyDate(self, sid, kid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByQtyPrice(self, sid, kid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByQtySupplyDate(self, sid, kid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByPriceSupplyDate(self, sid, kid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByName(self, sid, kid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rsname = %s;"
        cursor.execute(query, (sid, kid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByChangedDate(self, sid, kid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and r_changed_date = %s;"
        cursor.execute(query, (sid, kid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByQty(self, sid, kid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rqty = %s;"
        cursor.execute(query, (sid, kid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordByPrice(self, sid, kid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordBySupplyDate(self, sid, kid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date Supplier natural inner join ResourceHasKeyword where sid = %s and kid = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategory(self, sid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s;"
        cursor.execute(query, (sid, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNameChangedDateQtyPriceSupplyDate(self, sid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNameChangedDateQtyPrice(self, sid, cat_name, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNameChangedDateQtySupplyDate(self, sid, cat_name, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNameChangedDatePriceSupplyDate(self, sid, cat_name, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNameQtyPriceSupplyDate(self, sid, cat_name, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByChangedDateQtyPriceSupplyDate(self, sid, cat_name, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNameChangedDateQty(self, sid, cat_name, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (sid, cat_name, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNameChangedDatePrice(self, sid, cat_name, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNameChangedDateSupplyDate(self, sid, cat_name, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNameQtyPrice(self, sid, cat_name, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNameQtySupplyDate(self, sid, cat_name, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNamePriceSupplyDate(self, sid, cat_name, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByChangedDateQtyPrice(self, sid, cat_name, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByChangedDateQtySupplyDate(self, sid, cat_name, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByChangedDatePriceSupplyDate(self, sid, cat_name, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByQtyPriceSupplyDate(self, sid, cat_name, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNameChangedDate(self, sid, cat_name, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (sid, cat_name, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNameQty(self, sid, cat_name, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (sid, cat_name, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNamePrice(self, sid, cat_name, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByNameSupplyDate(self, sid, cat_name, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByChangedDateQty(self, sid, cat_name, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (sid, cat_name, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByChangedDatePrice(self, sid, cat_name, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByChangedDateSupplyDate(self, sid, cat_name, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByQtyPrice(self, sid, cat_name, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByQtySupplyDate(self, sid, cat_name, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByPriceSupplyDate(self, sid, cat_name, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByName(self, sid, cat_name, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rsname = %s;"
        cursor.execute(query, (sid, cat_name, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByChangedDate(self, sid, cat_name, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and r_changed_date = %s;"
        cursor.execute(query, (sid, cat_name, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByQty(self, sid, cat_name, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rqty = %s;"
        cursor.execute(query, (sid, cat_name, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryByPrice(self, sid, cat_name, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryBySupplyDate(self, sid, cat_name, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category where sid = %s and cat_name = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrder(self, sid, oid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s;"
        cursor.execute(query, (sid, oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNameChangedDateQtyPriceSupplyDate(self, sid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNameChangedDateQtyPrice(self, sid, oid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, oid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNameChangedDateQtySupplyDate(self, sid, oid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNameChangedDatePriceSupplyDate(self, sid, oid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNameQtyPriceSupplyDate(self, sid, oid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByChangedDateQtyPriceSupplyDate(self, sid, oid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNameChangedDateQty(self, sid, oid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (sid, oid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNameChangedDatePrice(self, sid, oid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (sid, oid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNameChangedDateSupplyDate(self, sid, oid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNameQtyPrice(self, sid, oid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, oid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNameQtySupplyDate(self, sid, oid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNamePriceSupplyDate(self, sid, oid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByChangedDateQtyPrice(self, sid, oid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, oid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByChangedDateQtySupplyDate(self, sid, oid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByChangedDatePriceSupplyDate(self, sid, oid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByQtyPriceSupplyDate(self, sid, oid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNameChangedDate(self, sid, oid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (sid, oid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNameQty(self, sid, oid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (sid, oid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNamePrice(self, sid, oid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (sid, oid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByNameSupplyDate(self, sid, oid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByChangedDateQty(self, sid, oid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (sid, oid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByChangedDatePrice(self, sid, oid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (sid, oid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByChangedDateSupplyDate(self, sid, oid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByQtyPrice(self, sid, oid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, oid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByQtySupplyDate(self, sid, oid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByPriceSupplyDate(self, sid, oid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByName(self, sid, oid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rsname = %s;"
        cursor.execute(query, (sid, oid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByChangedDate(self, sid, oid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and r_changed_date = %s;"
        cursor.execute(query, (sid, oid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByQty(self, sid, oid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rqty = %s;"
        cursor.execute(query, (sid, oid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderByPrice(self, sid, oid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and rprice = %s;"
        cursor.execute(query, (sid, oid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierOrderBySupplyDate(self, sid, oid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Transaction where sid = %s and oid = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, oid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategory(self, kid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s;"
        cursor.execute(query, (kid, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNameChangedDateQtyPriceSupplyDate(self, kid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNameChangedDateQtyPrice(self, kid, cat_name, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNameChangedDateQtySupplyDate(self, kid, cat_name, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNameChangedDatePriceSupplyDate(self, kid, cat_name, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNameQtyPriceSupplyDate(self, kid, cat_name, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByChangedDateQtyPriceSupplyDate(self, kid, cat_name, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNameChangedDateQty(self, kid, cat_name, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (kid, cat_name, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNameChangedDatePrice(self, kid, cat_name, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNameChangedDateSupplyDate(self, kid, cat_name, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNameQtyPrice(self, kid, cat_name, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNameQtySupplyDate(self, kid, cat_name, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNamePriceSupplyDate(self, kid, cat_name, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByChangedDateQtyPrice(self, kid, cat_name, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByChangedDateQtySupplyDate(self, kid, cat_name, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByChangedDatePriceSupplyDate(self, kid, cat_name, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByQtyPriceSupplyDate(self, kid, cat_name, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNameChangedDate(self, kid, cat_name, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (kid, cat_name, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNameQty(self, kid, cat_name, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (kid, cat_name, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNamePrice(self, kid, cat_name, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByNameSupplyDate(self, kid, cat_name, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByChangedDateQty(self, kid, cat_name, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (kid, cat_name, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByChangedDatePrice(self, kid, cat_name, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByChangedDateSupplyDate(self, kid, cat_name, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByQtyPrice(self, kid, cat_name, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByQtySupplyDate(self, kid, cat_name, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByPriceSupplyDate(self, kid, cat_name, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByName(self, kid, cat_name, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rsname = %s;"
        cursor.execute(query, (kid, cat_name, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByChangedDate(self, kid, cat_name, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and r_changed_date = %s;"
        cursor.execute(query, (kid, cat_name, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByQty(self, kid, cat_name, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rqty = %s;"
        cursor.execute(query, (kid, cat_name, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryByPrice(self, kid, cat_name, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryBySupplyDate(self, kid, cat_name, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category where kid = %s and cat_name = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrder(self, kid, oid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s;"
        cursor.execute(query, (kid, oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNameChangedDateQtyPriceSupplyDate(self, kid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNameChangedDateQtyPrice(self, kid, oid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, oid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNameChangedDateQtySupplyDate(self, kid, oid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNameChangedDatePriceSupplyDate(self, kid, oid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNameQtyPriceSupplyDate(self, kid, oid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByChangedDateQtyPriceSupplyDate(self, kid, oid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNameChangedDateQty(self, kid, oid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (kid, oid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNameChangedDatePrice(self, kid, oid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (kid, oid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNameChangedDateSupplyDate(self, kid, oid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNameQtyPrice(self, kid, oid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, oid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNameQtySupplyDate(self, kid, oid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNamePriceSupplyDate(self, kid, oid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByChangedDateQtyPrice(self, kid, oid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, oid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByChangedDateQtySupplyDate(self, kid, oid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByChangedDatePriceSupplyDate(self, kid, oid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByQtyPriceSupplyDate(self, kid, oid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNameChangedDate(self, kid, oid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (kid, oid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNameQty(self, kid, oid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (kid, oid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNamePrice(self, kid, oid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (kid, oid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByNameSupplyDate(self, kid, oid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByChangedDateQty(self, kid, oid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (kid, oid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByChangedDatePrice(self, kid, oid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (kid, oid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByChangedDateSupplyDate(self, kid, oid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByQtyPrice(self, kid, oid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, oid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByQtySupplyDate(self, kid, oid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByPriceSupplyDate(self, kid, oid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByName(self, kid, oid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rsname = %s;"
        cursor.execute(query, (kid, oid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByChangedDate(self, kid, oid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and r_changed_date = %s;"
        cursor.execute(query, (kid, oid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByQty(self, kid, oid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rqty = %s;"
        cursor.execute(query, (kid, oid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderByPrice(self, kid, oid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and rprice = %s;"
        cursor.execute(query, (kid, oid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordOrderBySupplyDate(self, kid, oid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Transaction where kid = %s and oid = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, oid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrder(self, cat_name, oid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s;"
        cursor.execute(query, (cat_name, oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNameChangedDateQtyPriceSupplyDate(self, cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNameChangedDateQtyPrice(self, cat_name, oid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cat_name, oid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNameChangedDateQtySupplyDate(self, cat_name, oid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNameChangedDatePriceSupplyDate(self, cat_name, oid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNameQtyPriceSupplyDate(self, cat_name, oid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByChangedDateQtyPriceSupplyDate(self, cat_name, oid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNameChangedDateQty(self, cat_name, oid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cat_name, oid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNameChangedDatePrice(self, cat_name, oid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cat_name, oid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNameChangedDateSupplyDate(self, cat_name, oid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNameQtyPrice(self, cat_name, oid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cat_name, oid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNameQtySupplyDate(self, cat_name, oid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNamePriceSupplyDate(self, cat_name, oid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByChangedDateQtyPrice(self, cat_name, oid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cat_name, oid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByChangedDateQtySupplyDate(self, cat_name, oid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByChangedDatePriceSupplyDate(self, cat_name, oid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByQtyPriceSupplyDate(self, cat_name, oid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNameChangedDate(self, cat_name, oid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (cat_name, oid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNameQty(self, cat_name, oid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (cat_name, oid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNamePrice(self, cat_name, oid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (cat_name, oid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByNameSupplyDate(self, cat_name, oid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByChangedDateQty(self, cat_name, oid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cat_name, oid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByChangedDatePrice(self, cat_name, oid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cat_name, oid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByChangedDateSupplyDate(self, cat_name, oid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByQtyPrice(self, cat_name, oid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cat_name, oid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByQtySupplyDate(self, cat_name, oid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByPriceSupplyDate(self, cat_name, oid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByName(self, cat_name, oid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rsname = %s;"
        cursor.execute(query, (cat_name, oid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByChangedDate(self, cat_name, oid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and r_changed_date = %s;"
        cursor.execute(query, (cat_name, oid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByQty(self, cat_name, oid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rqty = %s;"
        cursor.execute(query, (cat_name, oid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderByPrice(self, cat_name, oid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and rprice = %s;"
        cursor.execute(query, (cat_name, oid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryOrderBySupplyDate(self, cat_name, oid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Category natural inner join Transaction where cat_name = %s and oid = %s and r_supply_date = %s;"
        cursor.execute(query, (cat_name, oid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrder(self, tid, oid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s;"
        cursor.execute(query, (tid, oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNameChangedDateQtyPriceSupplyDate(self, tid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNameChangedDateQtyPrice(self, tid, oid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (tid, oid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNameChangedDateQtySupplyDate(self, tid, oid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNameChangedDatePriceSupplyDate(self, tid, oid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNameQtyPriceSupplyDate(self, tid, oid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByChangedDateQtyPriceSupplyDate(self, tid, oid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNameChangedDateQty(self, tid, oid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (tid, oid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNameChangedDatePrice(self, tid, oid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (tid, oid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNameChangedDateSupplyDate(self, tid, oid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNameQtyPrice(self, tid, oid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (tid, oid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNameQtySupplyDate(self, tid, oid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNamePriceSupplyDate(self, tid, oid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByChangedDateQtyPrice(self, tid, oid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (tid, oid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByChangedDateQtySupplyDate(self, tid, oid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByChangedDatePriceSupplyDate(self, tid, oid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByQtyPriceSupplyDate(self, tid, oid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNameChangedDate(self, tid, oid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (tid, oid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNameQty(self, tid, oid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (tid, oid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNamePrice(self, tid, oid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (tid, oid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByNameSupplyDate(self, tid, oid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByChangedDateQty(self, tid, oid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (tid, oid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByChangedDatePrice(self, tid, oid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (tid, oid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByChangedDateSupplyDate(self, tid, oid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByQtyPrice(self, tid, oid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (tid, oid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByQtySupplyDate(self, tid, oid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByPriceSupplyDate(self, tid, oid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByName(self, tid, oid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rsname = %s;"
        cursor.execute(query, (tid, oid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByChangedDate(self, tid, oid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and r_changed_date = %s;"
        cursor.execute(query, (tid, oid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByQty(self, tid, oid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rqty = %s;"
        cursor.execute(query, (tid, oid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderByPrice(self, tid, oid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and rprice = %s;"
        cursor.execute(query, (tid, oid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByTransactionOrderBySupplyDate(self, tid, oid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Transaction where tid = %s and oid = %s and r_supply_date = %s;"
        cursor.execute(query, (tid, oid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategory(self, cname, kid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s;"
        cursor.execute(query, (cname, kid, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNameChangedDateQtyPriceSupplyDate(self, cname, kid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNameChangedDateQtyPrice(self, cname, kid, cat_name, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNameChangedDateQtySupplyDate(self, cname, kid, cat_name, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNameChangedDatePriceSupplyDate(self, cname, kid, cat_name, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNameQtyPriceSupplyDate(self, cname, kid, cat_name, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByChangedDateQtyPriceSupplyDate(self, cname, kid, cat_name, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNameChangedDateQty(self, cname, kid, cat_name, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNameChangedDatePrice(self, cname, kid, cat_name, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNameChangedDateSupplyDate(self, cname, kid, cat_name, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNameQtyPrice(self, cname, kid, cat_name, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNameQtySupplyDate(self, cname, kid, cat_name, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNamePriceSupplyDate(self, cname, kid, cat_name, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByChangedDateQtyPrice(self, cname, kid, cat_name, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, cat_name, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByChangedDateQtySupplyDate(self, cname, kid, cat_name, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByChangedDatePriceSupplyDate(self, cname, kid, cat_name, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByQtyPriceSupplyDate(self, cname, kid, cat_name, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNameChangedDate(self, cname, kid, cat_name, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNameQty(self, cname, kid, cat_name, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNamePrice(self, cname, kid, cat_name, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByNameSupplyDate(self, cname, kid, cat_name, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByChangedDateQty(self, cname, kid, cat_name, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cname, kid, cat_name, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByChangedDatePrice(self, cname, kid, cat_name, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, cat_name, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByChangedDateSupplyDate(self, cname, kid, cat_name, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByQtyPrice(self, cname, kid, cat_name, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, cat_name, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByQtySupplyDate(self, cname, kid, cat_name, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByPriceSupplyDate(self, cname, kid, cat_name, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByName(self, cname, kid, cat_name, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rsname = %s;"
        cursor.execute(query, (cname, kid, cat_name, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByChangedDate(self, cname, kid, cat_name, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and r_changed_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByQty(self, cname, kid, cat_name, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rqty = %s;"
        cursor.execute(query, (cname, kid, cat_name, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryByPrice(self, cname, kid, cat_name, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, cat_name, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordCategoryBySupplyDate(self, cname, kid, cat_name, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Category where cname = %s and kid = %s and cat_name = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, cat_name, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrder(self, cname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (cname, kid, oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNameChangedDateQtyPriceSupplyDate(self, cname, kid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNameChangedDateQtyPrice(self, cname, kid, oid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNameChangedDateQtySupplyDate(self, cname, kid, oid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNameChangedDatePriceSupplyDate(self, cname, kid, oid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNameQtyPriceSupplyDate(self, cname, kid, oid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByChangedDateQtyPriceSupplyDate(self, cname, kid, oid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNameChangedDateQty(self, cname, kid, oid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNameChangedDatePrice(self, cname, kid, oid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNameChangedDateSupplyDate(self, cname, kid, oid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNameQtyPrice(self, cname, kid, oid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNameQtySupplyDate(self, cname, kid, oid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNamePriceSupplyDate(self, cname, kid, oid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByChangedDateQtyPrice(self, cname, kid, oid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, oid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByChangedDateQtySupplyDate(self, cname, kid, oid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByChangedDatePriceSupplyDate(self, cname, kid, oid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByQtyPriceSupplyDate(self, cname, kid, oid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNameChangedDate(self, cname, kid, oid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNameQty(self, cname, kid, oid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNamePrice(self, cname, kid, oid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByNameSupplyDate(self, cname, kid, oid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByChangedDateQty(self, cname, kid, oid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cname, kid, oid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByChangedDatePrice(self, cname, kid, oid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, oid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByChangedDateSupplyDate(self, cname, kid, oid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByQtyPrice(self, cname, kid, oid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, oid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByQtySupplyDate(self, cname, kid, oid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByPriceSupplyDate(self, cname, kid, oid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByName(self, cname, kid, oid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rsname = %s;"
        cursor.execute(query, (cname, kid, oid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByChangedDate(self, cname, kid, oid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and r_changed_date = %s;"
        cursor.execute(query, (cname, kid, oid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByQty(self, cname, kid, oid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rqty = %s;"
        cursor.execute(query, (cname, kid, oid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderByPrice(self, cname, kid, oid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and rprice = %s;"
        cursor.execute(query, (cname, kid, oid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityKeywordOrderBySupplyDate(self, cname, kid, oid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join ResourceHasKeyword natural inner join Transaction where cname = %s and kid = %s and oid = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, kid, oid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrder(self, cname, cat_name, oid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s;"
        cursor.execute(query, (cname, cat_name, oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNameChangedDateQtyPriceSupplyDate(self, cname, cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNameChangedDateQtyPrice(self, cname, cat_name, oid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNameChangedDateQtySupplyDate(self, cname, cat_name, oid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNameChangedDatePriceSupplyDate(self, cname, cat_name, oid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNameQtyPriceSupplyDate(self, cname, cat_name, oid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByChangedDateQtyPriceSupplyDate(self, cname, cat_name, oid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNameChangedDateQty(self, cname, cat_name, oid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNameChangedDatePrice(self, cname, cat_name, oid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNameChangedDateSupplyDate(self, cname, cat_name, oid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNameQtyPrice(self, cname, cat_name, oid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNameQtySupplyDate(self, cname, cat_name, oid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNamePriceSupplyDate(self, cname, cat_name, oid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByChangedDateQtyPrice(self, cname, cat_name, oid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, oid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByChangedDateQtySupplyDate(self, cname, cat_name, oid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByChangedDatePriceSupplyDate(self, cname, cat_name, oid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByQtyPriceSupplyDate(self, cname, cat_name, oid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNameChangedDate(self, cname, cat_name, oid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNameQty(self, cname, cat_name, oid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNamePrice(self, cname, cat_name, oid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByNameSupplyDate(self, cname, cat_name, oid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByChangedDateQty(self, cname, cat_name, oid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (cname, cat_name, oid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByChangedDatePrice(self, cname, cat_name, oid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, oid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByChangedDateSupplyDate(self, cname, cat_name, oid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByQtyPrice(self, cname, cat_name, oid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, oid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByQtySupplyDate(self, cname, cat_name, oid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByPriceSupplyDate(self, cname, cat_name, oid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByName(self, cname, cat_name, oid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rsname = %s;"
        cursor.execute(query, (cname, cat_name, oid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByChangedDate(self, cname, cat_name, oid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and r_changed_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByQty(self, cname, cat_name, oid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rqty = %s;"
        cursor.execute(query, (cname, cat_name, oid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderByPrice(self, cname, cat_name, oid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and rprice = %s;"
        cursor.execute(query, (cname, cat_name, oid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCityCategoryOrderBySupplyDate(self, cname, cat_name, oid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join Category natural inner join Transaction where cname = %s and cat_name = %s and oid = %s and r_supply_date = %s;"
        cursor.execute(query, (cname, cat_name, oid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategory(self, rname, kid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s;"
        cursor.execute(query, (rname, kid, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNameChangedDateQtyPriceSupplyDate(self, rname, kid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNameChangedDateQtyPrice(self, rname, kid, cat_name, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNameChangedDateQtySupplyDate(self, rname, kid, cat_name, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNameChangedDatePriceSupplyDate(self, rname, kid, cat_name, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNameQtyPriceSupplyDate(self, rname, kid, cat_name, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByChangedDateQtyPriceSupplyDate(self, rname, kid, cat_name, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNameChangedDateQty(self, rname, kid, cat_name, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNameChangedDatePrice(self, rname, kid, cat_name, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNameChangedDateSupplyDate(self, rname, kid, cat_name, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNameQtyPrice(self, rname, kid, cat_name, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNameQtySupplyDate(self, rname, kid, cat_name, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNamePriceSupplyDate(self, rname, kid, cat_name, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByChangedDateQtyPrice(self, rname, kid, cat_name, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, cat_name, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByChangedDateQtySupplyDate(self, rname, kid, cat_name, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByChangedDatePriceSupplyDate(self, rname, kid, cat_name, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByQtyPriceSupplyDate(self, rname, kid, cat_name, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNameChangedDate(self, rname, kid, cat_name, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNameQty(self, rname, kid, cat_name, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNamePrice(self, rname, kid, cat_name, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByNameSupplyDate(self, rname, kid, cat_name, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByChangedDateQty(self, rname, kid, cat_name, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (rname, kid, cat_name, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByChangedDatePrice(self, rname, kid, cat_name, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, cat_name, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByChangedDateSupplyDate(self, rname, kid, cat_name, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByQtyPrice(self, rname, kid, cat_name, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, cat_name, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByQtySupplyDate(self, rname, kid, cat_name, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByPriceSupplyDate(self, rname, kid, cat_name, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByName(self, rname, kid, cat_name, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rsname = %s;"
        cursor.execute(query, (rname, kid, cat_name, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByChangedDate(self, rname, kid, cat_name, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and r_changed_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByQty(self, rname, kid, cat_name, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rqty = %s;"
        cursor.execute(query, (rname, kid, cat_name, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryByPrice(self, rname, kid, cat_name, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, cat_name, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordCategoryBySupplyDate(self, rname, kid, cat_name, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Category where rname = %s and kid = %s and cat_name = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, cat_name, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrder(self, rname, kid, oid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s;"
        cursor.execute(query, (rname, kid, oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNameChangedDateQtyPriceSupplyDate(self, rname, kid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNameChangedDateQtyPrice(self, rname, kid, oid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNameChangedDateQtySupplyDate(self, rname, kid, oid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNameChangedDatePriceSupplyDate(self, rname, kid, oid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNameQtyPriceSupplyDate(self, rname, kid, oid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByChangedDateQtyPriceSupplyDate(self, rname, kid, oid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNameChangedDateQty(self, rname, kid, oid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNameChangedDatePrice(self, rname, kid, oid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNameChangedDateSupplyDate(self, rname, kid, oid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNameQtyPrice(self, rname, kid, oid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNameQtySupplyDate(self, rname, kid, oid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNamePriceSupplyDate(self, rname, kid, oid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByChangedDateQtyPrice(self, rname, kid, oid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, oid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByChangedDateQtySupplyDate(self, rname, kid, oid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByChangedDatePriceSupplyDate(self, rname, kid, oid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByQtyPriceSupplyDate(self, rname, kid, oid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNameChangedDate(self, rname, kid, oid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNameQty(self, rname, kid, oid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNamePrice(self, rname, kid, oid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByNameSupplyDate(self, rname, kid, oid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByChangedDateQty(self, rname, kid, oid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (rname, kid, oid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByChangedDatePrice(self, rname, kid, oid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, oid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByChangedDateSupplyDate(self, rname, kid, oid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByQtyPrice(self, rname, kid, oid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, oid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByQtySupplyDate(self, rname, kid, oid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByPriceSupplyDate(self, rname, kid, oid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByName(self, rname, kid, oid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rsname = %s;"
        cursor.execute(query, (rname, kid, oid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByChangedDate(self, rname, kid, oid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and r_changed_date = %s;"
        cursor.execute(query, (rname, kid, oid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByQty(self, rname, kid, oid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rqty = %s;"
        cursor.execute(query, (rname, kid, oid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderByPrice(self, rname, kid, oid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and rprice = %s;"
        cursor.execute(query, (rname, kid, oid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionKeywordOrderBySupplyDate(self, rname, kid, oid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join ResourceHasKeyword natural inner join Transaction where rname = %s and kid = %s and oid = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, kid, oid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrder(self, rname, cat_name, oid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s;"
        cursor.execute(query, (rname, cat_name, oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNameChangedDateQtyPriceSupplyDate(self, rname, cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNameChangedDateQtyPrice(self, rname, cat_name, oid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNameChangedDateQtySupplyDate(self, rname, cat_name, oid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNameChangedDatePriceSupplyDate(self, rname, cat_name, oid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNameQtyPriceSupplyDate(self, rname, cat_name, oid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByChangedDateQtyPriceSupplyDate(self, rname, cat_name, oid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNameChangedDateQty(self, rname, cat_name, oid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNameChangedDatePrice(self, rname, cat_name, oid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNameChangedDateSupplyDate(self, rname, cat_name, oid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNameQtyPrice(self, rname, cat_name, oid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNameQtySupplyDate(self, rname, cat_name, oid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNamePriceSupplyDate(self, rname, cat_name, oid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByChangedDateQtyPrice(self, rname, cat_name, oid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, oid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByChangedDateQtySupplyDate(self, rname, cat_name, oid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByChangedDatePriceSupplyDate(self, rname, cat_name, oid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByQtyPriceSupplyDate(self, rname, cat_name, oid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNameChangedDate(self, rname, cat_name, oid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNameQty(self, rname, cat_name, oid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNamePrice(self, rname, cat_name, oid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByNameSupplyDate(self, rname, cat_name, oid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByChangedDateQty(self, rname, cat_name, oid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (rname, cat_name, oid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByChangedDatePrice(self, rname, cat_name, oid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, oid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByChangedDateSupplyDate(self, rname, cat_name, oid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByQtyPrice(self, rname, cat_name, oid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, oid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByQtySupplyDate(self, rname, cat_name, oid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByPriceSupplyDate(self, rname, cat_name, oid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByName(self, rname, cat_name, oid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rsname = %s;"
        cursor.execute(query, (rname, cat_name, oid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByChangedDate(self, rname, cat_name, oid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and r_changed_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByQty(self, rname, cat_name, oid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rqty = %s;"
        cursor.execute(query, (rname, cat_name, oid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderByPrice(self, rname, cat_name, oid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and rprice = %s;"
        cursor.execute(query, (rname, cat_name, oid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionCategoryOrderBySupplyDate(self, rname, cat_name, oid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from (Resource natural inner join Supplier) as S inner join Account as A on S.sid = A.aid natural inner join Address natural inner join City natural inner join Category natural inner join Transaction where rname = %s and cat_name = %s and oid = %s and r_supply_date = %s;"
        cursor.execute(query, (rname, cat_name, oid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategory(self, sid, kid, cat_name):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s;"
        cursor.execute(query, (sid, kid, cat_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNameChangedDateQtyPriceSupplyDate(self, sid, kid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNameChangedDateQtyPrice(self, sid, kid, cat_name, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNameChangedDateQtySupplyDate(self, sid, kid, cat_name, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNameChangedDatePriceSupplyDate(self, sid, kid, cat_name, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNameQtyPriceSupplyDate(self, sid, kid, cat_name, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByChangedDateQtyPriceSupplyDate(self, sid, kid, cat_name, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNameChangedDateQty(self, sid, kid, cat_name, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNameChangedDatePrice(self, sid, kid, cat_name, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNameChangedDateSupplyDate(self, sid, kid, cat_name, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNameQtyPrice(self, sid, kid, cat_name, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNameQtySupplyDate(self, sid, kid, cat_name, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNamePriceSupplyDate(self, sid, kid, cat_name, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByChangedDateQtyPrice(self, sid, kid, cat_name, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, cat_name, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByChangedDateQtySupplyDate(self, sid, kid, cat_name, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByChangedDatePriceSupplyDate(self, sid, kid, cat_name, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByQtyPriceSupplyDate(self, sid, kid, cat_name, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNameChangedDate(self, sid, kid, cat_name, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNameQty(self, sid, kid, cat_name, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNamePrice(self, sid, kid, cat_name, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByNameSupplyDate(self, sid, kid, cat_name, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByChangedDateQty(self, sid, kid, cat_name, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (sid, kid, cat_name, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByChangedDatePrice(self, sid, kid, cat_name, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, cat_name, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByChangedDateSupplyDate(self, sid, kid, cat_name, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByQtyPrice(self, sid, kid, cat_name, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, cat_name, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByQtySupplyDate(self, sid, kid, cat_name, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByPriceSupplyDate(self, sid, kid, cat_name, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByName(self, sid, kid, cat_name, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rsname = %s;"
        cursor.execute(query, (sid, kid, cat_name, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByChangedDate(self, sid, kid, cat_name, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and r_changed_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByQty(self, sid, kid, cat_name, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rqty = %s;"
        cursor.execute(query, (sid, kid, cat_name, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryByPrice(self, sid, kid, cat_name, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, cat_name, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordCategoryBySupplyDate(self, sid, kid, cat_name, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Category where sid = %s and kid = %s and cat_name = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, cat_name, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrder(self, sid, kid, oid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s;"
        cursor.execute(query, (sid, kid, oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNameChangedDateQtyPriceSupplyDate(self, sid, kid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNameChangedDateQtyPrice(self, sid, kid, oid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNameChangedDateQtySupplyDate(self, sid, kid, oid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNameChangedDatePriceSupplyDate(self, sid, kid, oid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNameQtyPriceSupplyDate(self, sid, kid, oid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByChangedDateQtyPriceSupplyDate(self, sid, kid, oid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNameChangedDateQty(self, sid, kid, oid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNameChangedDatePrice(self, sid, kid, oid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNameChangedDateSupplyDate(self, sid, kid, oid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNameQtyPrice(self, sid, kid, oid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNameQtySupplyDate(self, sid, kid, oid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNamePriceSupplyDate(self, sid, kid, oid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByChangedDateQtyPrice(self, sid, kid, oid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, oid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByChangedDateQtySupplyDate(self, sid, kid, oid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByChangedDatePriceSupplyDate(self, sid, kid, oid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByQtyPriceSupplyDate(self, sid, kid, oid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNameChangedDate(self, sid, kid, oid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNameQty(self, sid, kid, oid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNamePrice(self, sid, kid, oid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByNameSupplyDate(self, sid, kid, oid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByChangedDateQty(self, sid, kid, oid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (sid, kid, oid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByChangedDatePrice(self, sid, kid, oid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, oid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByChangedDateSupplyDate(self, sid, kid, oid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByQtyPrice(self, sid, kid, oid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, oid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByQtySupplyDate(self, sid, kid, oid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByPriceSupplyDate(self, sid, kid, oid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByName(self, sid, kid, oid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rsname = %s;"
        cursor.execute(query, (sid, kid, oid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByChangedDate(self, sid, kid, oid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and r_changed_date = %s;"
        cursor.execute(query, (sid, kid, oid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByQty(self, sid, kid, oid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rqty = %s;"
        cursor.execute(query, (sid, kid, oid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderByPrice(self, sid, kid, oid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and rprice = %s;"
        cursor.execute(query, (sid, kid, oid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierKeywordOrderBySupplyDate(self, sid, kid, oid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join ResourceHasKeyword natural inner join Transaction where sid = %s and kid = %s and oid = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, kid, oid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrder(self, sid, cat_name, oid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s;"
        cursor.execute(query, (sid, cat_name, oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNameChangedDateQtyPriceSupplyDate(self, sid, cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNameChangedDateQtyPrice(self, sid, cat_name, oid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNameChangedDateQtySupplyDate(self, sid, cat_name, oid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNameChangedDatePriceSupplyDate(self, sid, cat_name, oid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNameQtyPriceSupplyDate(self, sid, cat_name, oid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByChangedDateQtyPriceSupplyDate(self, sid, cat_name, oid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNameChangedDateQty(self, sid, cat_name, oid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNameChangedDatePrice(self, sid, cat_name, oid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNameChangedDateSupplyDate(self, sid, cat_name, oid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNameQtyPrice(self, sid, cat_name, oid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNameQtySupplyDate(self, sid, cat_name, oid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNamePriceSupplyDate(self, sid, cat_name, oid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByChangedDateQtyPrice(self, sid, cat_name, oid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, oid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByChangedDateQtySupplyDate(self, sid, cat_name, oid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByChangedDatePriceSupplyDate(self, sid, cat_name, oid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByQtyPriceSupplyDate(self, sid, cat_name, oid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNameChangedDate(self, sid, cat_name, oid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNameQty(self, sid, cat_name, oid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNamePrice(self, sid, cat_name, oid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByNameSupplyDate(self, sid, cat_name, oid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByChangedDateQty(self, sid, cat_name, oid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (sid, cat_name, oid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByChangedDatePrice(self, sid, cat_name, oid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, oid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByChangedDateSupplyDate(self, sid, cat_name, oid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByQtyPrice(self, sid, cat_name, oid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, oid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByQtySupplyDate(self, sid, cat_name, oid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByPriceSupplyDate(self, sid, cat_name, oid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByName(self, sid, cat_name, oid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rsname = %s;"
        cursor.execute(query, (sid, cat_name, oid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByChangedDate(self, sid, cat_name, oid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and r_changed_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByQty(self, sid, cat_name, oid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rqty = %s;"
        cursor.execute(query, (sid, cat_name, oid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderByPrice(self, sid, cat_name, oid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and rprice = %s;"
        cursor.execute(query, (sid, cat_name, oid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierCategoryOrderBySupplyDate(self, sid, cat_name, oid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join Supplier natural inner join Category natural inner join Transaction where sid = %s and cat_name = %s and oid = %s and r_supply_date = %s;"
        cursor.execute(query, (sid, cat_name, oid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrder(self, kid, cat_name, oid):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s;"
        cursor.execute(query, (kid, cat_name, oid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNameChangedDateQtyPriceSupplyDate(self, kid, cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNameChangedDateQtyPrice(self, kid, cat_name, oid, rsname, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNameChangedDateQtySupplyDate(self, kid, cat_name, oid, rsname, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNameChangedDatePriceSupplyDate(self, kid, cat_name, oid, rsname, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNameQtyPriceSupplyDate(self, kid, cat_name, oid, rsname, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByChangedDateQtyPriceSupplyDate(self, kid, cat_name, oid, r_changed_date, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, r_changed_date, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNameChangedDateQty(self, kid, cat_name, oid, rsname, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNameChangedDatePrice(self, kid, cat_name, oid, rsname, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNameChangedDateSupplyDate(self, kid, cat_name, oid, rsname, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNameQtyPrice(self, kid, cat_name, oid, rsname, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNameQtySupplyDate(self, kid, cat_name, oid, rsname, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNamePriceSupplyDate(self, kid, cat_name, oid, rsname, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByChangedDateQtyPrice(self, kid, cat_name, oid, r_changed_date, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, oid, r_changed_date, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByChangedDateQtySupplyDate(self, kid, cat_name, oid, r_changed_date, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, r_changed_date, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByChangedDatePriceSupplyDate(self, kid, cat_name, oid, r_changed_date, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and r_changed_date = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, r_changed_date, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByQtyPriceSupplyDate(self, kid, cat_name, oid, rqty, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rqty = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, rqty, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNameChangedDate(self, kid, cat_name, oid, rsname, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and r_changed_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNameQty(self, kid, cat_name, oid, rsname, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and rqty = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNamePrice(self, kid, cat_name, oid, rsname, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByNameSupplyDate(self, kid, cat_name, oid, rsname, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByChangedDateQty(self, kid, cat_name, oid, r_changed_date, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and r_changed_date = %s and rqty = %s;"
        cursor.execute(query, (kid, cat_name, oid, r_changed_date, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByChangedDatePrice(self, kid, cat_name, oid, r_changed_date, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and r_changed_date = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, oid, r_changed_date, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByChangedDateSupplyDate(self, kid, cat_name, oid, r_changed_date, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and r_changed_date = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, r_changed_date, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByQtyPrice(self, kid, cat_name, oid, rqty, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rqty = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, oid, rqty, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByQtySupplyDate(self, kid, cat_name, oid, rqty, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rqty = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, rqty, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByPriceSupplyDate(self, kid, cat_name, oid, rprice, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rprice = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, rprice, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByName(self, kid, cat_name, oid, rsname):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rsname = %s;"
        cursor.execute(query, (kid, cat_name, oid, rsname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByChangedDate(self, kid, cat_name, oid, r_changed_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and r_changed_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, r_changed_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByQty(self, kid, cat_name, oid, rqty):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rqty = %s;"
        cursor.execute(query, (kid, cat_name, oid, rqty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderByPrice(self, kid, cat_name, oid, rprice):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and rprice = %s;"
        cursor.execute(query, (kid, cat_name, oid, rprice,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByKeywordCategoryOrderBySupplyDate(self, kid, cat_name, oid, r_supply_date):
        cursor = self.conn.cursor()
        query = "Select rsid, rsname, rdescription, r_changed_date, rqty, rprice, r_supply_date from Resource natural inner join ResourceHasKeyword natural inner join Category natural inner join Transaction where kid = %s and cat_name = %s and oid = %s and r_supply_date = %s;"
        cursor.execute(query, (kid, cat_name, oid, r_supply_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result
