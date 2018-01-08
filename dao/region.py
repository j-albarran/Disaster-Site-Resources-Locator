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

    def getRegionByName(rname, self):
        cursor = self.conn.cursor()
        query = "select * from region where rname = %s;"
        cursor.execute(query, (rname,))
        result = cursor.fetchone()
        return result

    def getRegionsByName(rname, self):
        cursor = self.conn.cursor()
        query = "select * from region where rname = %s;"
        cursor.execute(query, (rname,))
        result = cursor.fetchone()
        return result

    def getCityRegion(cname, self):
        cursor = self.conn.cursor()
        query = "select rname from city where cname = %s;"
        cursor.execute(query, (cname,))
        result = cursor.fetchone()
        return result

    def getRegionOfThisAddress(addId, self):
        cursor = self.conn.cursor()
        query = "select rname from city natural inner join address where addId = %s;"
        cursor.execute(query, (addId,))
        result = cursor.fetchone()
        return result

    def getAccountRegion(aid, self):
        cursor = self.conn.cursor()
        query = "select rname from account natural inner join address natural inner join city where aid = %s;"
        cursor.execute(query, (aid,))
        result = cursor.fetchone()
        return result

    def getAdministratorRegion(adminId, self):
        cursor = self.conn.cursor()
        query = "select rname from account natural inner join address natural inner join city inner join adminstrator on account.aid = administrator.adminId where administrator.adminId = %s;"
        cursor.execute(query, (adminId,))
        result = cursor.fetchone()
        return result

    def getSupplierRegion(sid, self):
        cursor = self.conn.cursor()
        query = "select cname from account natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where supplier.sid = %s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result

    def getRequesterRegion(rid, self):
        cursor = self.conn.cursor()
        query = "select cname from account natural inner join address natural inner join city inner join requester on account.aid = requester.rid where requester.rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result