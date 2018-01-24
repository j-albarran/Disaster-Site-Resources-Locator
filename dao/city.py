from config.dbconfig import conn


class CityDAO:
    def __init__(self):
        self.conn = conn

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    # ============ #
    #    Updates   #
    # ============ #

    def addNewCity(self, cname, rname):
        cursor = self.conn.cursor()
        query = "insert into city(cname, rname) values(%s, %s) returning cname;"
        cursor.execute(query, (cname, rname, ))
        cname = cursor.fetchone()[0]
        self.conn.commit()
        return cname

    def updateCity(self, cname, rname):
        cursor = self.conn.cursor()
        query = "update city set rname = %s where cname = %s;"
        cursor.execute(query, (rname, cname, ))
        self.conn.commit()
        return cname


    def deleteCity(self, cname):
        cursor = self.conn.cursor()
        query = "delete from city where cname = %s;"
        cursor.execute(query, (cname, ))
        self.conn.commit()
        return cname


    # ============ #
    #    Gets      #
    # ============ #

    def getAllCities(self):
        cursor = self.conn.cursor()
        query = "select cname from city;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCityByName(self, cname):
        cursor = self.conn.cursor()
        query = "select cname from city where cname = %s;"
        cursor.execute(query, (cname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCitiesByName(self,cname):
        cursor = self.conn.cursor()
        query = "select cname from city where cname = %s;"
        cursor.execute(query, (cname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCitiesOnThisRegion(self,rname):
        cursor = self.conn.cursor()
        query = "select cname from city where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCityOfThisAddress(self,addId):
        cursor = self.conn.cursor()
        query = "select cname from address where addId = %s;"
        cursor.execute(query, (addId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountCity(self,aid):
        cursor = self.conn.cursor()
        query = "select cname from account natural inner join address natural inner join city where aid = %s;"
        cursor.execute(query, (aid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorCity(self,adminId):
        cursor = self.conn.cursor()
        query = "select cname from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s;"
        cursor.execute(query, (adminId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierCity(self,sid):
        cursor = self.conn.cursor()
        query = "select cname from account inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterCity(self,rid):
        cursor = self.conn.cursor()
        query = "select cname from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
