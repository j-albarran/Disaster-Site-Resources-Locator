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

    def getSupplierById(self, sid):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where supplier.sid = %s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result

    def getSuppliersByAFirstALastEmailPhone(self,afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (afirst, alast, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAFirstALastEmail(self,afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (afirst, alast, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAFirstALastPhone(self,afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (afirst, alast, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAFirstPhoneEmail(self,afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (afirst, phone, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByALastEmailPhone(self,alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (alast, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAFirstALast(self,afirst, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s and alast = %s;"
        cursor.execute(query, (afirst, alast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAFirstEmail(self,afirst, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s and email = %s;"
        cursor.execute(query, (afirst, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAFirstPhone(self,afirst, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s and phone = %s;"
        cursor.execute(query, (afirst, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByALastEmail(self,alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where alast = %s and email = %s;"
        cursor.execute(query, (alast, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByALastPhone(self,alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where alast = %s and phone = %s;"
        cursor.execute(query, (alast, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByEmailPhone(self,email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where email = %s and phone = %s;"
        cursor.execute(query, (email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByAFirst(self,afirst):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where afirst = %s;"
        cursor.execute(query, (afirst,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByALast(self,alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sidinner join supplier on account.aid = supplier.sidinner join supplier on account.aid = supplier.sid where alast = %s;"
        cursor.execute(query, (alast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByEmail(self,email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sidinner join supplier on account.aid = supplier.sid where email = %s;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByPhone(self,phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid where phone = %s;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersWithThisAddressID(self,addId):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address where addId = %s;"
        cursor.execute(query, (addId, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByAfirstAlastEmailPhone(self,addId, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address where addId = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByAfirstAlastEmail(self,addId, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where addId = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByAfirstAlastPhone(self,addId, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where addId = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByAfirstPhoneEmail(self,addId, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where addId = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (addId, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByAlastEmailPhone(self,addId, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where addId = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByAfirstAlast(self,addId, afirst, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where addId = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (addId, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByAfirstEmail(self,addId, afirst, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where addId = %s and afirst = %s and email = %s;"
        cursor.execute(query, (addId, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByAfirstPhone(self,addId, afirst, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where addId = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByAlastEmail(self,addId, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address where addId = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByAlastPhone(self,addId, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address where addId = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByEmailPhone(self,addId, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address where addId = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByAfirst(self,addId, afirst):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address where addId = %s and afirst = %s;"
        cursor.execute(query, (addId, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByAlast(self,addId, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address where addId = %s and alast = %s;"
        cursor.execute(query, (addId, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByEmail(self,addId, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address where addId = %s and email = %s;"
        cursor.execute(query, (addId, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisAddressIDByPhone(self,addId, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sidnatural inner join address where addId = %s and phone = %s;"
        cursor.execute(query, (addId, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCity(self,cname):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address where cname = %s;"
        cursor.execute(query, (cname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityAfirstAlastEmailPhone(self,cname, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address where cname = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAfirstAlastEmail(self,cname, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address where cname = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAfirstAlastPhone(self,cname, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where cname = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAfirstPhoneEmail(self,cname, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where cname = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAlastEmailPhone(self,cname, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where cname = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAfirstAlast(self,cname, afirst, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where cname = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAfirstEmail(self,cname, afirst, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where cname = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAfirstPhone(self,cname, afirst, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where cname = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAlastEmail(self,cname, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where cname = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAlastPhone(self,cname, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where cname = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByEmailPhone(self,cname, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where cname = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAfirst(self,cname, afirst):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone ninner join supplier on account.aid = supplier.sid atural inner join address  where cname = %s and afirst = %s;"
        cursor.execute(query, (cname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByAlast(self,cname, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where cname = %s and alast = %s;"
        cursor.execute(query, (cname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByEmail(self,cname, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where cname = %s and email = %s;"
        cursor.execute(query, (cname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisCityByPhone(self,cname, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address  where cname = %s and phone = %s;"
        cursor.execute(query, (cname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegion(self,rname):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s;"
        cursor.execute(query, (rname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionAfirstAlastEmailPhone(self,rname, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAfirstAlastEmail(self,rname, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAfirstAlastPhone(self,rname, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAfirstPhoneEmail(self,rname, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (rname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAlastEmailPhone(self,rname, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAfirstAlast(self,rname, afirst, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (rname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAfirstEmail(self,rname, afirst, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and afirst = %s and email = %s;"
        cursor.execute(query, (rname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAfirstPhone(self,rname, afirst, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAlastEmail(self,rname, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAlastPhone(self,rname, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByEmailPhone(self,rname, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAfirst(self,rname, afirst):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and afirst = %s;"
        cursor.execute(query, (rname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByAlast(self,rname, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and alast = %s;"
        cursor.execute(query, (rname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByEmail(self,rname, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and email = %s;"
        cursor.execute(query, (rname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOnThisRegionByPhone(self,rname, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city  where rname = %s and phone = %s;"
        cursor.execute(query, (rname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccount(self,bid):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s;"
        cursor.execute(query, (bid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByAfirstAlastEmailPhone(self,bid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (bid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByAfirstAlastEmail(self,bid, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (bid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByAfirstAlastPhone(self,bid, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (bid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByAfirstPhoneEmail(self,bid, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (bid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByAlastEmailPhone(self,bid, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (bid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByAfirstAlast(self,bid, afirst, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (bid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByAfirstEmail(self,bid, afirst, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (bid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByAfirstPhone(self,bid, afirst, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (bid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByAlastEmail(self,bid, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s and alast = %s and email = %s;"
        cursor.execute(query, (bid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByAlastPhone(self,bid, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (bid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByEmailPhone(self,bid, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s and email = %s and phone = %s;"
        cursor.execute(query, (bid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByAfirst(self,bid, afirst):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s and afirst = %s;"
        cursor.execute(query, (bid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByAlast(self,bid, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s and alast = %s;"
        cursor.execute(query, (bid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByEmail(self,bid, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account where bid = %s and email = %s;"
        cursor.execute(query, (bid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisBankAccountByPhone(self,bid, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join bank_account  where bid = %s and phone = %s;"
        cursor.execute(query, (bid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersOfThisResource(self,rsid):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource where rsid = %s;"
        cursor.execute(query, (rsid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirstAlastEmailPhone(self,rsid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rsid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirstAlastEmail(self,rsid, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (rsid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirstAlastPhone(self,rsid, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rsid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirstPhoneEmail(self,rsid, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (rsid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAlastEmailPhone(self,rsid, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rsid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirstAlast(self,rsid, afirst, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (rsid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirstEmail(self,rsid, afirst, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (rsid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirstPhone(self,rsid, afirst, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (rsid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAlastEmail(self,rsid, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and alast = %s and email = %s;"
        cursor.execute(query, (rsid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAlastPhone(self,rsid, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rsid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByEmailPhone(self,rsid, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and email = %s and phone = %s;"
        cursor.execute(query, (rsid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAfirst(self,rsid, afirst):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and afirst = %s;"
        cursor.execute(query, (rsid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByAlast(self,rsid, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and alast = %s;"
        cursor.execute(query, (rsid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByEmail(self,rsid, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and email = %s;"
        cursor.execute(query, (rsid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceByPhone(self,rsid, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where rsid = %s and phone = %s;"
        cursor.execute(query, (rsid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategory(self,cat_name):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s;"
        cursor.execute(query, (cat_name, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirstAlastEmailPhone(self,cat_name, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cat_name, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirstAlastEmail(self,cat_name, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cat_name, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirstAlastPhone(self,cat_name, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cat_name, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirstPhoneEmail(self,cat_name, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cat_name, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAlastEmailPhone(self,cat_name, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cat_name, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirstAlast(self,cat_name, afirst, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cat_name, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirstEmail(self,cat_name, afirst, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cat_name, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirstPhone(self,cat_name, afirst, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cat_name, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAlastEmail(self,cat_name, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s and alast = %s and email = %s;"
        cursor.execute(query, (cat_name, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAlastPhone(self,cat_name, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cat_name, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByEmailPhone(self,cat_name, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s and email = %s and phone = %s;"
        cursor.execute(query, (cat_name, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAfirst(self,cat_name, afirst):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid " \
                " natural inner join resource  where cat_name = %s and afirst = %s;"
        cursor.execute(query, (cat_name, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByAlast(self,cat_name, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s and alast = %s;"
        cursor.execute(query, (cat_name, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByEmail(self,cat_name, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s and email = %s;"
        cursor.execute(query, (cat_name, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisCategoryByPhone(self,cat_name, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join resource  where cat_name = %s and phone = %s;"
        cursor.execute(query, (cat_name, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransaction(self,tid):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s;"
        cursor.execute(query, (tid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirstAlastEmailPhone(self,tid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (tid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirstAlastEmail(self,tid, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (tid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirstAlastPhone(self,tid, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (tid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirstPhoneEmail(self,tid, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (tid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAlastEmailPhone(self,tid, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (tid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirstAlast(self,tid, afirst, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (tid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirstEmail(self,tid, afirst, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (tid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirstPhone(self,tid, afirst, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (tid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAlastEmail(self,tid, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and alast = %s and email = %s;"
        cursor.execute(query, (tid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAlastPhone(self,tid, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (tid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByEmailPhone(self,tid, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and email = %s and phone = %s;"
        cursor.execute(query, (tid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAfirst(self,tid, afirst):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and afirst = %s;"
        cursor.execute(query, (tid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByAlast(self,tid, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and alast = %s;"
        cursor.execute(query, (tid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByEmail(self,tid, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and email = %s;"
        cursor.execute(query, (tid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisTransactionByPhone(self,tid, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where tid = %s and phone = %s;"
        cursor.execute(query, (tid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfo(self,oid):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s;"
        cursor.execute(query, (oid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirstAlastEmailPhone(self,oid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (oid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirstAlastEmail(self,oid, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (oid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirstAlastPhone(self,oid, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (oid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirstPhoneEmail(self,oid, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (oid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAlastEmailPhone(self,oid, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (oid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirstAlast(self,oid, afirst, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (oid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirstEmail(self,oid, afirst, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (oid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirstPhone(self,oid, afirst, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (oid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAlastEmail(self,oid, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and alast = %s and email = %s;"
        cursor.execute(query, (oid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAlastPhone(self,oid, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (oid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByEmailPhone(self,oid, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and email = %s and phone = %s;"
        cursor.execute(query, (oid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAfirst(self,oid, afirst):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and afirst = %s;"
        cursor.execute(query, (oid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByAlast(self,oid, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and alast = %s;"
        cursor.execute(query, (oid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByEmail(self,oid, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and email = %s;"
        cursor.execute(query, (oid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisOrderInfoByPhone(self,oid, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join transaction  where oid = %s and phone = %s;"
        cursor.execute(query, (oid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCity(self, cname, rsid):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s;"
        cursor.execute(query, (cname, rsid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirstAlastEmailPhone(self, cname, rsid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, rsid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirstAlastEmail(self, cname, rsid, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, rsid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirstAlastPhone(self, cname, rsid, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, rsid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirstPhoneEmail(self, cname, rsid, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cname, rsid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAlastEmailPhone(self, cname, rsid, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, rsid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirstAlast(self, cname, rsid, afirst, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cname, rsid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirstEmail(self, cname, rsid, afirst, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cname, rsid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirstPhone(self, cname, rsid, afirst, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cname, rsid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAlastEmail(self, cname, rsid, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, rsid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAlastPhone(self, cname, rsid, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, rsid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByEmailPhone(self, cname, rsid, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, rsid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAfirst(self, cname, rsid, afirst):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and afirst = %s;"
        cursor.execute(query, (cname, rsid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByAlast(self, cname, rsid, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and alast = %s;"
        cursor.execute(query, (cname, rsid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByEmail(self, cname, rsid, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and email = %s;"
        cursor.execute(query, (cname, rsid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisCityByPhone(self, cname, rsid, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join resource  where cname = %s and rsid = %s and phone = %s;"
        cursor.execute(query, (cname, rsid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegion(self, rname, rsid):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s;"
        cursor.execute(query, (rname, rsid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirstAlastEmailPhone(self, rname, rsid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, rsid, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirstAlastEmail(self, rname, rsid, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, rsid, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirstAlastPhone(self, rname, rsid, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, rsid, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirstPhoneEmail(self, rname, rsid, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (rname, rsid, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAlastEmailPhone(self, rname, rsid, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, rsid, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirstAlast(self, rname, rsid, afirst, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (rname, rsid, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirstEmail(self, rname, rsid, afirst, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and afirst = %s and email = %s;"
        cursor.execute(query, (rname, rsid, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirstPhone(self, rname, rsid, afirst, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (rname, rsid, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAlastEmail(self, rname, rsid, alast, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, rsid, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAlastPhone(self, rname, rsid, alast, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, rsid, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByEmailPhone(self, rname, rsid, email, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, rsid, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAfirst(self, rname, rsid, afirst):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and afirst = %s;"
        cursor.execute(query, (rname, rsid, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByAlast(self, rname, rsid, alast):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and alast = %s;"
        cursor.execute(query, (rname, rsid, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByEmail(self, rname, rsid, email):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and email = %s;"
        cursor.execute(query, (rname, rsid, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierOfThisResourceOnThisRegionByPhone(self, rname, rsid, phone):
        cursor = self.conn.cursor()
        query = "select supplier.sid, afirst, alast, email, phone from account natural inner join phone inner join supplier on account.aid = supplier.sid natural inner join address natural inner join city natural inner join resource  where rname = %s and rsid = %s and phone = %s;"
        cursor.execute(query, (rname, rsid, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result
