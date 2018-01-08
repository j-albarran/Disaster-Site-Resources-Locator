from config.dbconfig import conn

class RequesterDAO:
    def __init__(self):
        self.conn = conn
# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    def getAllRequesters(self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterById(rid, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where requester.rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getRequestersByAFirstALastEmailPhone(afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (afirst, alast, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByAFirstALastEmail(afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (afirst, alast, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByAFirstALastPhone(afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (afirst, alast, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByAFirstPhoneEmail(afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (afirst, phone, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByALastEmailPhone(alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (alast, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByAFirstALast(afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where afirst = %s and alast = %s;"
        cursor.execute(query, (afirst, alast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByAFirstEmail(afirst, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where afirst = %s and email = %s;"
        cursor.execute(query, (afirst, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByAFirstPhone(afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where afirst = %s and phone = %s;"
        cursor.execute(query, (afirst, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByALastEmail(alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where alast = %s and email = %s;"
        cursor.execute(query, (alast, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByALastPhone(alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where alast = %s and phone = %s;"
        cursor.execute(query, (alast, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByEmailPhone(email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where email = %s and phone = %s;"
        cursor.execute(query, (email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByAFirst(afirst, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where afirst = %s;"
        cursor.execute(query, (afirst,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByALast(alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where alast = %s;"
        cursor.execute(query, (alast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByEmail(email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where email = %s;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersByPhone(phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone inner join requester on account.aid = requester.rid where phone = %s;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersWithThisAddressID(addId, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s;"
        cursor.execute(query, (addId, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByAfirstAlastEmailPhone(addId, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, email, phone, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByAfirstAlastEmail(addId, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, afirst, alast, email, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByAfirstAlastPhone(addId, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, phone, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByAfirstPhoneEmail(addId, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (addId, afirst, phone, email, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByAlastEmailPhone(addId, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, alast, email, phone, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByAfirstAlast(addId, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (addId, afirst, alast, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByAfirstEmail(addId, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and afirst = %s and email = %s;"
        cursor.execute(query, (addId, afirst, email, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByAfirstPhone(addId, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, phone, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByAlastEmail(addId, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, alast, email, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByAlastPhone(addId, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, alast, phone, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByEmailPhone(addId, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, email, phone, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByAfirst(addId, afirst, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and afirst = %s;"
        cursor.execute(query, (addId, afirst, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByAlast(addId, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and alast = %s;"
        cursor.execute(query, (addId, alast, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByEmail(addId, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and email = %s;"
        cursor.execute(query, (addId, email, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisAddressIDByPhone(addId, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where addId = %s and phone = %s;"
        cursor.execute(query, (addId, phone, ))
        result = cursor.fetchone()
        return result

    def getRequestersOnThisCity(cname, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s;"
        cursor.execute(query, (cname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityAfirstAlastEmailPhone(cname, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAfirstAlastEmail(cname, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAfirstAlastPhone(cname, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAfirstPhoneEmail(cname, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAlastEmailPhone(cname, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAfirstAlast(cname, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAfirstEmail(cname, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAfirstPhone(cname, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAlastEmail(cname, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAlastPhone(cname, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByEmailPhone(cname, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAfirst(cname, afirst, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and afirst = %s;"
        cursor.execute(query, (cname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByAlast(cname, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and alast = %s;"
        cursor.execute(query, (cname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByEmail(cname, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and email = %s;"
        cursor.execute(query, (cname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCityByPhone(cname, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join requester on account.aid = requester.rid where cname = %s and phone = %s;"
        cursor.execute(query, (cname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegion(rname, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s;"
        cursor.execute(query, (rname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionAfirstAlastEmailPhone(rname, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAfirstAlastEmail(rname, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAfirstAlastPhone(rname, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAfirstPhoneEmail(rname, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (rname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAlastEmailPhone(rname, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAfirstAlast(rname, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (rname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAfirstEmail(rname, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and afirst = %s and email = %s;"
        cursor.execute(query, (rname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAfirstPhone(rname, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAlastEmail(rname, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAlastPhone(rname, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByEmailPhone(rname, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAfirst(rname, afirst, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and afirst = %s;"
        cursor.execute(query, (rname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByAlast(rname, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and alast = %s;"
        cursor.execute(query, (rname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByEmail(rname, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and email = %s;"
        cursor.execute(query, (rname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisRegionByPhone(rname, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join requester on account.aid = requester.rid where rname = %s and phone = %s;"
        cursor.execute(query, (rname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResource(rsid, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource join requester on account.aid = requester.rid where rsid = %s;"
        cursor.execute(query, (rsid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceAfirstAlastEmailPhone(rsid, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rsid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAfirstAlastEmail(rsid, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (rsid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAfirstAlastPhone(rsid, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rsid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAfirstPhoneEmail(rsid, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (rsid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAlastEmailPhone(rsid, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rsid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAfirstAlast(rsid, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (rsid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAfirstEmail(rsid, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (rsid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAfirstPhone(rsid, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (rsid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAlastEmail(rsid, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and alast = %s and email = %s;"
        cursor.execute(query, (rsid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAlastPhone(rsid, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rsid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByEmailPhone(rsid, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and email = %s and phone = %s;"
        cursor.execute(query, (rsid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAfirst(rsid, afirst, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and afirst = %s;"
        cursor.execute(query, (rsid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByAlast(rsid, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and alast = %s;"
        cursor.execute(query, (rsid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByEmail(rsid, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and email = %s;"
        cursor.execute(query, (rsid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceByPhone(rsid, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested natural inner join resource inner join requester on account.aid = requester.rid where rsid = %s and phone = %s;"
        cursor.execute(query, (rsid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequested(rrid, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s;"
        cursor.execute(query, (rrid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedAfirstAlastEmailPhone(rrid, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rrid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAfirstAlastEmail(rrid, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (rrid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAfirstAlastPhone(rrid, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rrid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAfirstPhoneEmail(rrid, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (rrid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAlastEmailPhone(rrid, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rrid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAfirstAlast(rrid, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (rrid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAfirstEmail(rrid, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (rrid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAfirstPhone(rrid, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (rrid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAlastEmail(rrid, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and alast = %s and email = %s;"
        cursor.execute(query, (rrid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAlastPhone(rrid, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rrid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByEmailPhone(rrid, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and email = %s and phone = %s;"
        cursor.execute(query, (rrid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAfirst(rrid, afirst, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and afirst = %s;"
        cursor.execute(query, (rrid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByAlast(rrid, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and alast = %s;"
        cursor.execute(query, (rrid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByEmail(rrid, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and email = %s;"
        cursor.execute(query, (rrid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisResourceRequestedByPhone(rrid, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where rrid = %s and phone = %s;"
        cursor.execute(query, (rrid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategory(cat_name, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s;"
        cursor.execute(query, (cat_name, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryAfirstAlastEmailPhone(cat_name, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cat_name, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAfirstAlastEmail(cat_name, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cat_name, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAfirstAlastPhone(cat_name, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cat_name, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAfirstPhoneEmail(cat_name, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cat_name, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAlastEmailPhone(cat_name, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cat_name, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAfirstAlast(cat_name, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cat_name, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAfirstEmail(cat_name, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cat_name, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAfirstPhone(cat_name, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cat_name, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAlastEmail(cat_name, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and alast = %s and email = %s;"
        cursor.execute(query, (cat_name, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAlastPhone(cat_name, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cat_name, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByEmailPhone(cat_name, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and email = %s and phone = %s;"
        cursor.execute(query, (cat_name, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAfirst(cat_name, afirst, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and afirst = %s;"
        cursor.execute(query, (cat_name, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByAlast(cat_name, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and alast = %s;"
        cursor.execute(query, (cat_name, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByEmail(cat_name, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and email = %s;"
        cursor.execute(query, (cat_name, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCategoryByPhone(cat_name, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join requester on account.aid = requester.rid where cat_name = %s and phone = %s;"
        cursor.execute(query, (cat_name, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransaction(tid, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s;"
        cursor.execute(query, (tid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionAfirstAlastEmailPhone(tid, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (tid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAfirstAlastEmail(tid, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (tid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAfirstAlastPhone(tid, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (tid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAfirstPhoneEmail(tid, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (tid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAlastEmailPhone(tid, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (tid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAfirstAlast(tid, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (tid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAfirstEmail(tid, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (tid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAfirstPhone(tid, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (tid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAlastEmail(tid, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and alast = %s and email = %s;"
        cursor.execute(query, (tid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAlastPhone(tid, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (tid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByEmailPhone(tid, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and email = %s and phone = %s;"
        cursor.execute(query, (tid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAfirst(tid, afirst, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and afirst = %s;"
        cursor.execute(query, (tid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByAlast(tid, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and alast = %s;"
        cursor.execute(query, (tid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByEmail(tid, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and email = %s;"
        cursor.execute(query, (tid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisTransactionByPhone(tid, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where tid = %s and phone = %s;"
        cursor.execute(query, (tid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result



    def getRequestersOnThisCreditCard(cid, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s;"
        cursor.execute(query, (cid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardAfirstAlastEmailPhone(cid, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAfirstAlastEmail(cid, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAfirstAlastPhone(cid, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAfirstPhoneEmail(cid, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAlastEmailPhone(cid, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAfirstAlast(cid, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAfirstEmail(cid, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAfirstPhone(cid, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAlastEmail(cid, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and alast = %s and email = %s;"
        cursor.execute(query, (cid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAlastPhone(cid, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByEmailPhone(cid, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and email = %s and phone = %s;"
        cursor.execute(query, (cid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAfirst(cid, afirst, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and afirst = %s;"
        cursor.execute(query, (cid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByAlast(cid, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and alast = %s;"
        cursor.execute(query, (cid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByEmail(cid, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and email = %s;"
        cursor.execute(query, (cid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisCreditCardByPhone(cid, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join credit_card inner join requester on account.aid = requester.rid where cid = %s and phone = %s;"
        cursor.execute(query, (cid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfo(oid, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s;"
        cursor.execute(query, (oid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoAfirstAlastEmailPhone(oid, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (oid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAfirstAlastEmail(oid, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (oid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAfirstAlastPhone(oid, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (oid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAfirstPhoneEmail(oid, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (oid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAlastEmailPhone(oid, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (oid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAfirstAlast(oid, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (oid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAfirstEmail(oid, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (oid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAfirstPhone(oid, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (oid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAlastEmail(oid, alast, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and alast = %s and email = %s;"
        cursor.execute(query, (oid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAlastPhone(oid, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (oid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByEmailPhone(oid, email, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and email = %s and phone = %s;"
        cursor.execute(query, (oid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAfirst(oid, afirst, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and afirst = %s;"
        cursor.execute(query, (oid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByAlast(oid, alast, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and alast = %s;"
        cursor.execute(query, (oid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByEmail(oid, email, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and email = %s;"
        cursor.execute(query, (oid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestersOnThisOrderInfoByPhone(oid, phone, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join requester on account.aid = requester.rid where oid = %s and phone = %s;"
        cursor.execute(query, (oid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result