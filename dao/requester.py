from config.dbconfig import conn

class RequesterDAO:
    def __init__(self):
        self.conn = conn
# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    def getAllRequesters(self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid ;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterById(self, rid):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where requester.rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getRequestersByAFirstALastEmailPhone(self,afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (afirst, alast, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByAFirstALastEmail(self,afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (afirst, alast, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByAFirstALastPhone(self,afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (afirst, alast, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByAFirstPhoneEmail(self,afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (afirst, phone, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByALastEmailPhone(self,alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (alast, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByAFirstALast(self,afirst, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where afirst = %s and alast = %s;"
        cursor.execute(query, (afirst, alast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByAFirstEmail(self,afirst, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where afirst = %s and email = %s;"
        cursor.execute(query, (afirst, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByAFirstPhone(self,afirst, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where afirst = %s and phone = %s;"
        cursor.execute(query, (afirst, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByALastEmail(self,alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where alast = %s and email = %s;"
        cursor.execute(query, (alast, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByALastPhone(self,alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where alast = %s and phone = %s;"
        cursor.execute(query, (alast, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByEmailPhone(self,email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where email = %s and phone = %s;"
        cursor.execute(query, (email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByAFirst(self,afirst):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where afirst = %s;"
        cursor.execute(query, (afirst,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByALast(self,alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where alast = %s;"
        cursor.execute(query, (alast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByEmail(self,email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where email = %s;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByPhone(self,phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  where phone = %s;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersWithThisAddressID(self,addId):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where addId = %s;"
        cursor.execute(query, (addId, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByAfirstAlastEmailPhone(self,addId, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where addId = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByAfirstAlastEmail(self,addId, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where addId = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByAfirstAlastPhone(self,addId, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where addId = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByAfirstPhoneEmail(self,addId, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where addId = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (addId, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByAlastEmailPhone(self,addId, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where addId = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByAfirstAlast(self,addId, afirst, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where addId = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (addId, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByAfirstEmail(self,addId, afirst, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where addId = %s and afirst = %s and email = %s;"
        cursor.execute(query, (addId, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByAfirstPhone(self,addId, afirst, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where addId = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByAlastEmail(self,addId, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where addId = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByAlastPhone(self,addId, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where addId = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByEmailPhone(self,addId, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where addId = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByAfirst(self,addId, afirst):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  natural inner join address where addId = %s and afirst = %s;"
        cursor.execute(query, (addId, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByAlast(self,addId, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid  natural inner join address where addId = %s and alast = %s;"
        cursor.execute(query, (addId, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByEmail(self,addId, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where addId = %s and email = %s;"
        cursor.execute(query, (addId, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisAddressIDByPhone(self,addId, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where addId = %s and phone = %s;"
        cursor.execute(query, (addId, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCity(self,cname):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s;"
        cursor.execute(query, (cname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityAfirstAlastEmailPhone(self,cname, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAfirstAlastEmail(self,cname, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAfirstAlastPhone(self,cname, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAfirstPhoneEmail(self,cname, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAlastEmailPhone(self,cname, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAfirstAlast(self,cname, afirst, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAfirstEmail(self,cname, afirst, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAfirstPhone(self,cname, afirst, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAlastEmail(self,cname, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAlastPhone(self,cname, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByEmailPhone(self,cname, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAfirst(self,cname, afirst):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and afirst = %s;"
        cursor.execute(query, (cname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAlast(self,cname, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and alast = %s;"
        cursor.execute(query, (cname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByEmail(self,cname, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and email = %s;"
        cursor.execute(query, (cname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByPhone(self,cname, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address  where cname = %s and phone = %s;"
        cursor.execute(query, (cname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegion(self,rname):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s;"
        cursor.execute(query, (rname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionAfirstAlastEmailPhone(self,rname, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAfirstAlastEmail(self,rname, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAfirstAlastPhone(self,rname, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAfirstPhoneEmail(self,rname, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (rname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAlastEmailPhone(self,rname, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAfirstAlast(self,rname, afirst, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (rname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAfirstEmail(self,rname, afirst, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and afirst = %s and email = %s;"
        cursor.execute(query, (rname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAfirstPhone(self,rname, afirst, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAlastEmail(self,rname, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAlastPhone(self,rname, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByEmailPhone(self,rname, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAfirst(self,rname, afirst):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and afirst = %s;"
        cursor.execute(query, (rname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAlast(self,rname, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and alast = %s;"
        cursor.execute(query, (rname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByEmail(self,rname, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and email = %s;"
        cursor.execute(query, (rname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByPhone(self,rname, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join address natural inner join city  where rname = %s and phone = %s;"
        cursor.execute(query, (rname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResource(self,rsid):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource join requester on account.aid = requester.rid where rsid = %s;"
        cursor.execute(query, (rsid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceAfirstAlastEmailPhone(self,rsid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rsid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAfirstAlastEmail(self,rsid, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (rsid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAfirstAlastPhone(self,rsid, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rsid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAfirstPhoneEmail(self,rsid, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (rsid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAlastEmailPhone(self,rsid, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rsid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAfirstAlast(self,rsid, afirst, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (rsid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAfirstEmail(self,rsid, afirst, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (rsid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAfirstPhone(self,rsid, afirst, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (rsid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAlastEmail(self,rsid, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and alast = %s and email = %s;"
        cursor.execute(query, (rsid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAlastPhone(self,rsid, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rsid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByEmailPhone(self,rsid, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and email = %s and phone = %s;"
        cursor.execute(query, (rsid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAfirst(self,rsid, afirst):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and afirst = %s;"
        cursor.execute(query, (rsid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAlast(self,rsid, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and alast = %s;"
        cursor.execute(query, (rsid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByEmail(self,rsid, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and email = %s;"
        cursor.execute(query, (rsid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByPhone(self,rsid, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested natural inner join resource  where rsid = %s and phone = %s;"
        cursor.execute(query, (rsid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequested(self,rrid):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s;"
        cursor.execute(query, (rrid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedAfirstAlastEmailPhone(self,rrid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rrid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAfirstAlastEmail(self,rrid, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (rrid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAfirstAlastPhone(self,rrid, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rrid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAfirstPhoneEmail(self,rrid, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (rrid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAlastEmailPhone(self,rrid, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rrid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAfirstAlast(self,rrid, afirst, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (rrid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAfirstEmail(self,rrid, afirst, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (rrid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAfirstPhone(self,rrid, afirst, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (rrid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAlastEmail(self,rrid, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and alast = %s and email = %s;"
        cursor.execute(query, (rrid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAlastPhone(self,rrid, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rrid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByEmailPhone(self,rrid, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and email = %s and phone = %s;"
        cursor.execute(query, (rrid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAfirst(self,rrid, afirst):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and afirst = %s;"
        cursor.execute(query, (rrid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAlast(self,rrid, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and alast = %s;"
        cursor.execute(query, (rrid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByEmail(self,rrid, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and email = %s;"
        cursor.execute(query, (rrid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByPhone(self,rrid, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where rrid = %s and phone = %s;"
        cursor.execute(query, (rrid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategory(self,cat_name):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s;"
        cursor.execute(query, (cat_name, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryAfirstAlastEmailPhone(self,cat_name, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cat_name, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAfirstAlastEmail(self,cat_name, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cat_name, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAfirstAlastPhone(self,cat_name, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cat_name, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAfirstPhoneEmail(self,cat_name, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cat_name, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAlastEmailPhone(self,cat_name, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cat_name, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAfirstAlast(self,cat_name, afirst, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cat_name, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAfirstEmail(self,cat_name, afirst, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cat_name, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAfirstPhone(self,cat_name, afirst, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cat_name, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAlastEmail(self,cat_name, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and alast = %s and email = %s;"
        cursor.execute(query, (cat_name, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAlastPhone(self,cat_name, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cat_name, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByEmailPhone(self,cat_name, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and email = %s and phone = %s;"
        cursor.execute(query, (cat_name, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAfirst(self,cat_name, afirst):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and afirst = %s;"
        cursor.execute(query, (cat_name, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAlast(self,cat_name, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and alast = %s;"
        cursor.execute(query, (cat_name, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByEmail(self,cat_name, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and email = %s;"
        cursor.execute(query, (cat_name, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByPhone(self,cat_name, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join resource_requested  where cat_name = %s and phone = %s;"
        cursor.execute(query, (cat_name, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransaction(self,tid):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s;"
        cursor.execute(query, (tid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionAfirstAlastEmailPhone(self,tid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (tid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAfirstAlastEmail(self,tid, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (tid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAfirstAlastPhone(self,tid, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (tid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAfirstPhoneEmail(self,tid, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (tid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAlastEmailPhone(self,tid, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (tid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAfirstAlast(self,tid, afirst, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (tid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAfirstEmail(self,tid, afirst, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (tid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAfirstPhone(self,tid, afirst, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (tid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAlastEmail(self,tid, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and alast = %s and email = %s;"
        cursor.execute(query, (tid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAlastPhone(self,tid, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (tid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByEmailPhone(self,tid, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and email = %s and phone = %s;"
        cursor.execute(query, (tid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAfirst(self,tid, afirst):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and afirst = %s;"
        cursor.execute(query, (tid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAlast(self,tid, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and alast = %s;"
        cursor.execute(query, (tid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByEmail(self,tid, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and email = %s;"
        cursor.execute(query, (tid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByPhone(self,tid, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where tid = %s and phone = %s;"
        cursor.execute(query, (tid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result



    def getRequestersOnThisCreditCard(self,cid):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s;"
        cursor.execute(query, (cid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardAfirstAlastEmailPhone(self,cid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAfirstAlastEmail(self,cid, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAfirstAlastPhone(self,cid, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAfirstPhoneEmail(self,cid, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAlastEmailPhone(self,cid, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAfirstAlast(self,cid, afirst, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAfirstEmail(self,cid, afirst, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAfirstPhone(self,cid, afirst, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAlastEmail(self,cid, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and alast = %s and email = %s;"
        cursor.execute(query, (cid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAlastPhone(self,cid, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByEmailPhone(self,cid, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and email = %s and phone = %s;"
        cursor.execute(query, (cid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAfirst(self,cid, afirst):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and afirst = %s;"
        cursor.execute(query, (cid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAlast(self,cid, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and alast = %s;"
        cursor.execute(query, (cid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByEmail(self,cid, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and email = %s;"
        cursor.execute(query, (cid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByPhone(self,cid, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join credit_card  where cid = %s and phone = %s;"
        cursor.execute(query, (cid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfo(self,oid):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s;"
        cursor.execute(query, (oid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoAfirstAlastEmailPhone(self,oid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (oid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAfirstAlastEmail(self,oid, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (oid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAfirstAlastPhone(self,oid, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (oid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAfirstPhoneEmail(self,oid, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (oid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAlastEmailPhone(self,oid, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (oid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAfirstAlast(self,oid, afirst, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (oid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAfirstEmail(self,oid, afirst, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (oid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAfirstPhone(self,oid, afirst, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (oid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAlastEmail(self,oid, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and alast = %s and email = %s;"
        cursor.execute(query, (oid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAlastPhone(self,oid, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (oid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByEmailPhone(self,oid, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and email = %s and phone = %s;"
        cursor.execute(query, (oid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAfirst(self,oid, afirst):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and afirst = %s;"
        cursor.execute(query, (oid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAlast(self,oid, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and alast = %s;"
        cursor.execute(query, (oid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByEmail(self,oid, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and email = %s;"
        cursor.execute(query, (oid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByPhone(self,oid, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join transaction  where oid = %s and phone = %s;"
        cursor.execute(query, (oid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPayment(self,payid):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s;"
        cursor.execute(query, (payid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentAfirstAlastEmailPhone(self,payid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (payid, afirst, alast, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentByAfirstAlastEmail(self,payid, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (payid, afirst, alast, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentByAfirstAlastPhone(self,payid, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (payid, afirst, alast, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentByAfirstPhoneEmail(self,payid, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (payid, afirst, phone, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentByAlastEmailPhone(self,payid, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (payid, alast, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentByAfirstAlast(self,payid, afirst, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (payid, afirst, alast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentByAfirstEmail(self,payid, afirst, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (payid, afirst, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentByAfirstPhone(self,payid, afirst, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (payid, afirst, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentByAlastEmail(self,payid, alast, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and alast = %s and email = %s;"
        cursor.execute(query, (payid, alast, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentByAlastPhone(self,payid, alast, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (payid, alast, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentByEmailPhone(self,payid, email, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and email = %s and phone = %s;"
        cursor.execute(query, (payid, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentByAfirst(self,payid, afirst):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and afirst = %s;"
        cursor.execute(query, (payid, afirst,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentByAlast(self,payid, alast):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and alast = %s;"
        cursor.execute(query, (payid, alast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentByEmail(self,payid, email):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and email = %s;"
        cursor.execute(query, (payid, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisPaymentByPhone(self,payid, phone):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid natural inner join payment  where payid = %s and phone = %s;"
        cursor.execute(query, (payid, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result