from config.dbconfig import conn


class SupplierDAO:
    def __init__(self):
        self.conn = conn

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #
    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(sid, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where supplier.sid = %s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result

    def getSuppliersByAFirstALastEmailPhone(afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (afirst, alast, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAFirstALastEmail(afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (afirst, alast, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAFirstALastPhone(afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (afirst, alast, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAFirstPhoneEmail(afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (afirst, phone, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByALastEmailPhone(alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (alast, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAFirstALast(afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s and alast = %s;"
        cursor.execute(query, (afirst, alast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAFirstEmail(afirst, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s and email = %s;"
        cursor.execute(query, (afirst, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAFirstPhone(afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s and phone = %s;"
        cursor.execute(query, (afirst, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByALastEmail(alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where alast = %s and email = %s;"
        cursor.execute(query, (alast, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByALastPhone(alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where alast = %s and phone = %s;"
        cursor.execute(query, (alast, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByEmailPhone(email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where email = %s and phone = %s;"
        cursor.execute(query, (email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAFirst(afirst, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s;"
        cursor.execute(query, (afirst,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByALast(alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where alast = %s;"
        cursor.execute(query, (alast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByEmail(email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where email = %s;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByPhone(phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where phone = %s;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersWithThisAddressID(addId, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s;"
        cursor.execute(query, (addId, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByAfirstAlastEmailPhone(addId, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, email, phone, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByAfirstAlastEmail(addId, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, afirst, alast, email, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByAfirstAlastPhone(addId, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, phone, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByAfirstPhoneEmail(addId, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (addId, afirst, phone, email, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByAlastEmailPhone(addId, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, alast, email, phone, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByAfirstAlast(addId, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (addId, afirst, alast, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByAfirstEmail(addId, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and afirst = %s and email = %s;"
        cursor.execute(query, (addId, afirst, email, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByAfirstPhone(addId, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, phone, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByAlastEmail(addId, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, alast, email, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByAlastPhone(addId, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, alast, phone, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByEmailPhone(addId, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, email, phone, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByAfirst(addId, afirst, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and afirst = %s;"
        cursor.execute(query, (addId, afirst, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByAlast(addId, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and alast = %s;"
        cursor.execute(query, (addId, alast, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByEmail(addId, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and email = %s;"
        cursor.execute(query, (addId, email, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisAddressIDByPhone(addId, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where addId = %s and phone = %s;"
        cursor.execute(query, (addId, phone, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOnThisCity(cname, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s;"
        cursor.execute(query, (cname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityAfirstAlastEmailPhone(cname, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAfirstAlastEmail(cname, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAfirstAlastPhone(cname, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAfirstPhoneEmail(cname, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAlastEmailPhone(cname, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAfirstAlast(cname, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAfirstEmail(cname, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAfirstPhone(cname, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAlastEmail(cname, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAlastPhone(cname, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByEmailPhone(cname, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAfirst(cname, afirst, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and afirst = %s;"
        cursor.execute(query, (cname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAlast(cname, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and alast = %s;"
        cursor.execute(query, (cname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByEmail(cname, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and email = %s;"
        cursor.execute(query, (cname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByPhone(cname, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join supplier on account.aid = supplier.sid where cname = %s and phone = %s;"
        cursor.execute(query, (cname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegion(rname, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s;"
        cursor.execute(query, (rname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionAfirstAlastEmailPhone(rname, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAfirstAlastEmail(rname, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAfirstAlastPhone(rname, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAfirstPhoneEmail(rname, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (rname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAlastEmailPhone(rname, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAfirstAlast(rname, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (rname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAfirstEmail(rname, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and afirst = %s and email = %s;"
        cursor.execute(query, (rname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAfirstPhone(rname, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAlastEmail(rname, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAlastPhone(rname, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByEmailPhone(rname, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAfirst(rname, afirst, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and afirst = %s;"
        cursor.execute(query, (rname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAlast(rname, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and alast = %s;"
        cursor.execute(query, (rname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByEmail(rname, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and email = %s;"
        cursor.execute(query, (rname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByPhone(rname, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join supplier on account.aid = supplier.sid where rname = %s and phone = %s;"
        cursor.execute(query, (rname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccount(bid, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s;"
        cursor.execute(query, (bid, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByAfirstAlastEmailPhone(bid, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (bid, afirst, alast, email, phone, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByAfirstAlastEmail(bid, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (bid, afirst, alast, email, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByAfirstAlastPhone(bid, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (bid, afirst, alast, phone, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByAfirstPhoneEmail(bid, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (bid, afirst, phone, email, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByAlastEmailPhone(bid, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (bid, alast, email, phone, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByAfirstAlast(bid, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (bid, afirst, alast, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByAfirstEmail(bid, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (bid, afirst, email, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByAfirstPhone(bid, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (bid, afirst, phone, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByAlastEmail(bid, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and alast = %s and email = %s;"
        cursor.execute(query, (bid, alast, email, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByAlastPhone(bid, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (bid, alast, phone, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByEmailPhone(bid, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and email = %s and phone = %s;"
        cursor.execute(query, (bid, email, phone, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByAfirst(bid, afirst, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and afirst = %s;"
        cursor.execute(query, (bid, afirst, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByAlast(bid, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and alast = %s;"
        cursor.execute(query, (bid, alast, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByEmail(bid, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and email = %s;"
        cursor.execute(query, (bid, email, ))
        result = cursor.fetchone()
        return result

    def getSupplierOfThisBankAccountByPhone(bid, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join bank_account inner join supplier on account.aid = supplier.sid where bid = %s and phone = %s;"
        cursor.execute(query, (bid, phone, ))
        result = cursor.fetchone()
        return result

    def getSuppliersOfThisResource(rsid, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource join supplier on account.aid = supplier.sid where rsid = %s;"
        cursor.execute(query, (rsid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirstAlastEmailPhone(rsid, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rsid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirstAlastEmail(rsid, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (rsid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirstAlastPhone(rsid, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rsid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirstPhoneEmail(rsid, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (rsid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAlastEmailPhone(rsid, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rsid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirstAlast(rsid, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (rsid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirstEmail(rsid, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (rsid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirstPhone(rsid, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (rsid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAlastEmail(rsid, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and alast = %s and email = %s;"
        cursor.execute(query, (rsid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAlastPhone(rsid, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rsid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByEmailPhone(rsid, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and email = %s and phone = %s;"
        cursor.execute(query, (rsid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirst(rsid, afirst, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and afirst = %s;"
        cursor.execute(query, (rsid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAlast(rsid, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and alast = %s;"
        cursor.execute(query, (rsid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByEmail(rsid, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and email = %s;"
        cursor.execute(query, (rsid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByPhone(rsid, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where rsid = %s and phone = %s;"
        cursor.execute(query, (rsid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategory(cat_name, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join supplier on account.aid = supplier.sid where cat_name = %s;"
        cursor.execute(query, (cat_name, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirstAlastEmailPhone(cat_name, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join supplier on account.aid = supplier.sid where cat_name = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cat_name, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirstAlastEmail(cat_name, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource_requested inner join supplier on account.aid = supplier.sid where cat_name = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cat_name, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirstAlastPhone(cat_name, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where cat_name = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cat_name, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirstPhoneEmail(cat_name, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where cat_name = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cat_name, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAlastEmailPhone(cat_name, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where cat_name = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cat_name, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirstAlast(cat_name, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where cat_name = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cat_name, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirstEmail(cat_name, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where cat_name = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cat_name, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirstPhone(cat_name, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where cat_name = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cat_name, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAlastEmail(cat_name, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where cat_name = %s and alast = %s and email = %s;"
        cursor.execute(query, (cat_name, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAlastPhone(cat_name, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where cat_name = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cat_name, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByEmailPhone(cat_name, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where cat_name = %s and email = %s and phone = %s;"
        cursor.execute(query, (cat_name, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirst(cat_name, afirst, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where cat_name = %s and afirst = %s;"
        cursor.execute(query, (cat_name, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAlast(cat_name, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where cat_name = %s and alast = %s;"
        cursor.execute(query, (cat_name, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByEmail(cat_name, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where cat_name = %s and email = %s;"
        cursor.execute(query, (cat_name, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByPhone(cat_name, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join resource inner join supplier on account.aid = supplier.sid where cat_name = %s and phone = %s;"
        cursor.execute(query, (cat_name, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransaction(tid, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s;"
        cursor.execute(query, (tid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirstAlastEmailPhone(tid, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (tid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirstAlastEmail(tid, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (tid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirstAlastPhone(tid, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (tid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirstPhoneEmail(tid, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (tid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAlastEmailPhone(tid, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (tid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirstAlast(tid, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (tid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirstEmail(tid, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (tid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirstPhone(tid, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (tid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAlastEmail(tid, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and alast = %s and email = %s;"
        cursor.execute(query, (tid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAlastPhone(tid, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (tid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByEmailPhone(tid, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and email = %s and phone = %s;"
        cursor.execute(query, (tid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirst(tid, afirst, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and afirst = %s;"
        cursor.execute(query, (tid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAlast(tid, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and alast = %s;"
        cursor.execute(query, (tid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByEmail(tid, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and email = %s;"
        cursor.execute(query, (tid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByPhone(tid, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where tid = %s and phone = %s;"
        cursor.execute(query, (tid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfo(oid, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s;"
        cursor.execute(query, (oid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirstAlastEmailPhone(oid, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (oid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirstAlastEmail(oid, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (oid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirstAlastPhone(oid, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (oid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirstPhoneEmail(oid, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (oid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAlastEmailPhone(oid, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (oid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirstAlast(oid, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (oid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirstEmail(oid, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (oid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirstPhone(oid, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (oid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAlastEmail(oid, alast, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and alast = %s and email = %s;"
        cursor.execute(query, (oid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAlastPhone(oid, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (oid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByEmailPhone(oid, email, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and email = %s and phone = %s;"
        cursor.execute(query, (oid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirst(oid, afirst, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and afirst = %s;"
        cursor.execute(query, (oid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAlast(oid, alast, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and alast = %s;"
        cursor.execute(query, (oid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByEmail(oid, email, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and email = %s;"
        cursor.execute(query, (oid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByPhone(oid, phone, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone natural inner join transaction inner join supplier on account.aid = supplier.sid where oid = %s and phone = %s;"
        cursor.execute(query, (oid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCity(self, cname, rsid):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s;"
        cursor.execute(query, (cname, rsid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirstAlastEmailPhone(self, cname, rsid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, rsid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirstAlastEmail(self, cname, rsid, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, rsid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirstAlastPhone(self, cname, rsid, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, rsid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirstPhoneEmail(self, cname, rsid, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cname, rsid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAlastEmailPhone(self, cname, rsid, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, rsid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirstAlast(self, cname, rsid, afirst, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cname, rsid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirstEmail(self, cname, rsid, afirst, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cname, rsid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirstPhone(self, cname, rsid, afirst, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cname, rsid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAlastEmail(self, cname, rsid, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, rsid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAlastPhone(self, cname, rsid, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, rsid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByEmailPhone(self, cname, rsid, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, rsid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirst(self, cname, rsid, afirst):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and afirst = %s;"
        cursor.execute(query, (cname, rsid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAlast(self, cname, rsid, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and alast = %s;"
        cursor.execute(query, (cname, rsid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByEmail(self, cname, rsid, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and email = %s;"
        cursor.execute(query, (cname, rsid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByPhone(self, cname, rsid, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join resource inner join supplier on account.aid = supplier.sid where cname = %s and rsid = %s and phone = %s;"
        cursor.execute(query, (cname, rsid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegion(self, rname, rsid):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s;"
        cursor.execute(query, (rname, rsid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirstAlastEmailPhone(self, rname, rsid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, rsid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirstAlastEmail(self, rname, rsid, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, rsid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirstAlastPhone(self, rname, rsid, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, rsid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirstPhoneEmail(self, rname, rsid, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (rname, rsid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAlastEmailPhone(self, rname, rsid, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, rsid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirstAlast(self, rname, rsid, afirst, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (rname, rsid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirstEmail(self, rname, rsid, afirst, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (rname, rsid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirstPhone(self, rname, rsid, afirst, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (rname, rsid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAlastEmail(self, rname, rsid, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, rsid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAlastPhone(self, rname, rsid, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, rsid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByEmailPhone(self, rname, rsid, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, rsid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirst(self, rname, rsid, afirst):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and afirst = %s;"
        cursor.execute(query, (rname, rsid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAlast(self, rname, rsid, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and alast = %s;"
        cursor.execute(query, (rname, rsid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByEmail(self, rname, rsid, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and email = %s;"
        cursor.execute(query, (rname, rsid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByPhone(self, rname, rsid, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone, from account natural inner join phone natural inner join address natural inner join city natural inner join resource inner join supplier on account.aid = supplier.sid where rname = %s and rsid = %s and phone = %s;"
        cursor.execute(query, (rname, rsid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result