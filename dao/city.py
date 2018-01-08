from config.dbconfig import conn


class CityDAO:
    def __init__(self):
        self.conn = conn

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    def getAllCities(self):
        cursor = self.conn.cursor()
        query = "select cname from city;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCityByName(cname, self):
        cursor = self.conn.cursor()
        query = "select cname from city where cname = %s;"
        cursor.execute(query, (cname,))
        result = cursor.fetchone()
        return result

    def getCitiesByName(cname, self):
        cursor = self.conn.cursor()
        query = "select cname from city where cname = %s;"
        cursor.execute(query, (cname,))
        result = cursor.fetchone()
        return result

    def getCitiesOnThisRegion(rname, self):
        cursor = self.conn.cursor()
        query = "select cname from city where rname = %s;"
        cursor.execute(query, (rname,))
        result = cursor.fetchone()
        return result

    def getCityOfThisAddress(addId, self):
        cursor = self.conn.cursor()
        query = "select cname from address where addId = %s;"
        cursor.execute(query, (addId,))
        result = cursor.fetchone()
        return result

    def getAccountCity(aid, self):
        cursor = self.conn.cursor()
        query = "select cname from account natural inner join address where aid = %s;"
        cursor.execute(query, (aid,))
        result = cursor.fetchone()
        return result

    def getAdministratorCity(adminId, self):
        cursor = self.conn.cursor()
        query = "select cname from account natural inner join address inner join administrator on account.aid = administrator.adminId where administrator.adminId = %s;"
        cursor.execute(query, (adminId,))
        result = cursor.fetchone()
        return result

    def getSupplierCity(sid, self):
        cursor = self.conn.cursor()
        query = "select cname from account natural inner join address inner join supplier on account.aid = supplier.sid where supplier.sid = %s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result

    def getRequesterCity(rid, self):
        cursor = self.conn.cursor()
        query = "select cname from account natural inner join address inner join requester on account.aid = requester.rid where requester.rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result