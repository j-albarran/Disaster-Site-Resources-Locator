from config.dbconfig import conn

class RegionDAO:
    def __init__(self):
        self.conn = conn

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    def getAllRegions(self):
        cursor = self.conn.cursor()
        query = "select * from region;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRegionByName(self, rname):
        cursor = self.conn.cursor()
        query = "select * from region where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRegionsByName(self, rname):
        cursor = self.conn.cursor()
        query = "select * from region where rname = %s;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCityRegion(self, cname):
        cursor = self.conn.cursor()
        query = "select rname from city where cname = %s;"
        cursor.execute(query, (cname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRegionOfThisAddress(self, addId):
        cursor = self.conn.cursor()
        query = "select rname from city natural inner join address where addId = %s;"
        cursor.execute(query, (addId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountRegion(self, aid):
        cursor = self.conn.cursor()
        query = "select rname from account natural inner join address natural inner join city where aid = %s;"
        cursor.execute(query, (aid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorRegion(self, adminId):
        cursor = self.conn.cursor()
        query = "select rname from account inner join adminstrator on account.aid = administrator.adminId natural inner join address natural inner join city where administrator.adminId = %s;"
        cursor.execute(query, (adminId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierRegion(self, sid):
        cursor = self.conn.cursor()
        query = "select rname from account inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city where supplier.sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterRegion(self, rid):
        cursor = self.conn.cursor()
        query = "select rname from account inner join requester on account.aid = requester.rid natural inner join address natural inner join city where requester.rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
