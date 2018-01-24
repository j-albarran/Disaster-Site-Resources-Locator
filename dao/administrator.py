from config.dbconfig import conn


class AdministratorDAO:
    def __init__(self):
        self.conn = conn

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    # ============ #
    #    Updates   #
    # ============ #

    def addNewAdministrator(self, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "insert into account(afirst, alast, email) values(%s, %s, %s) returning aid;"
        cursor.execute(query, (afirst, alast, email,))
        aid = cursor.fetchone()[0]
        query = "insert into phone(aid, phone) values(%s, %s);"
        cursor.execute(query, (aid, phone,))
        query = "insert into administrator(adminId) values(%s)"
        cursor.execute(query, (aid,))
        self.conn.commit()
        return aid

    def updateAdministrator(self, adminId, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "update account set afirst = %s, alast = %s, email = %s where aid = %s;"
        cursor.execute(query, (afirst, alast, email, adminId, ))
        query = "update phone set phone = %s where aid = %s;"
        cursor.execute(query, (phone, adminId, ))
        self.conn.commit()
        return adminId

    def deleteAdministrator(self, adminId):
        cursor = self.conn.cursor()
        query = "delete from administrator where adminId = %s;"
        cursor.execute(query, (adminId, ))
        query = "delete from phone where aid = %s;"
        cursor.execute(query, (adminId, ))
        query = "delete from account where aid = %s;"
        cursor.execute(query, (adminId,))
        self.conn.commit()
        return adminId


    # ============ #
    #    Gets      #
    # ============ #

    def getAllAdministrators(self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorById(self,adminId):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where administrator.adminId = %s;"
        cursor.execute(query, (adminId,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirstALastEmailPhone(self,afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (afirst, alast, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirstALastEmail(self,afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (afirst, alast, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirstALastPhone(self,afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (afirst, alast, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirstPhoneEmail(self,afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (afirst, phone, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByALastEmailPhone(self,alast, email, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (alast, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirstALast(self,afirst, alast):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s and alast = %s;"
        cursor.execute(query, (afirst, alast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirstEmail(self,afirst, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s and email = %s;"
        cursor.execute(query, (afirst, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirstPhone(self,afirst, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s and phone = %s;"
        cursor.execute(query, (afirst, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByALastEmail(self,alast, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where alast = %s and email = %s;"
        cursor.execute(query, (alast, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByALastPhone(self,alast, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where alast = %s and phone = %s;"
        cursor.execute(query, (alast, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByEmailPhone(self,email, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where email = %s and phone = %s;"
        cursor.execute(query, (email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirst(self,afirst):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s;"
        cursor.execute(query, (afirst,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByALast(self,alast):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where alast = %s;"
        cursor.execute(query, (alast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByEmail(self,email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where email = %s;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByPhone(self,phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where phone = %s;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsWithThisAddressID(self,addId):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s;"
        cursor.execute(query, (addId, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByAfirstAlastEmailPhone(self,addId, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByAfirstAlastEmail(self,addId, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByAfirstAlastPhone(self,addId, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByAfirstPhoneEmail(self,addId, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (addId, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByAlastEmailPhone(self,addId, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByAfirstAlast(self,addId, afirst, alast):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (addId, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByAfirstEmail(self,addId, afirst, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and afirst = %s and email = %s;"
        cursor.execute(query, (addId, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByAfirstPhone(self,addId, afirst, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByAlastEmail(self,addId, alast, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByAlastPhone(self,addId, alast, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByEmailPhone(self,addId, email, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByAfirst(self,addId, afirst):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and afirst = %s;"
        cursor.execute(query, (addId, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByAlast(self,addId, alast):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and alast = %s;"
        cursor.execute(query, (addId, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByEmail(self,addId, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and email = %s;"
        cursor.execute(query, (addId, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisAddressIDByPhone(self,addId, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where addId = %s and phone = %s;"
        cursor.execute(query, (addId, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCity(self,cname):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s;"
        cursor.execute(query, (cname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityAfirstAlastEmailPhone(self,cname, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAfirstAlastEmail(self,cname, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAfirstAlastPhone(self,cname, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAfirstPhoneEmail(self,cname, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAlastEmailPhone(self,cname, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAfirstAlast(self,cname, afirst, alast):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAfirstEmail(self,cname, afirst, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAfirstPhone(self,cname, afirst, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAlastEmail(self,cname, alast, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAlastPhone(self,cname, alast, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByEmailPhone(self,cname, email, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAfirst(self,cname, afirst):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and afirst = %s;"
        cursor.execute(query, (cname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAlast(self,cname, alast):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and alast = %s;"
        cursor.execute(query, (cname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByEmail(self,cname, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and email = %s;"
        cursor.execute(query, (cname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByPhone(self,cname, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address  where cname = %s and phone = %s;"
        cursor.execute(query, (cname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegion(self,rname):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s;"
        cursor.execute(query, (rname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionAfirstAlastEmailPhone(self,rname, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAfirstAlastEmail(self,rname, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAfirstAlastPhone(self,rname, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAfirstPhoneEmail(self,rname, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (rname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAlastEmailPhone(self,rname, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAfirstAlast(self,rname, afirst, alast):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (rname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAfirstEmail(self,rname, afirst, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and afirst = %s and email = %s;"
        cursor.execute(query, (rname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAfirstPhone(self,rname, afirst, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAlastEmail(self,rname, alast, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAlastPhone(self,rname, alast, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByEmailPhone(self,rname, email, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAfirst(self,rname, afirst):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and afirst = %s;"
        cursor.execute(query, (rname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAlast(self,rname, alast):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and alast = %s;"
        cursor.execute(query, (rname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByEmail(self,rname, email):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and email = %s;"
        cursor.execute(query, (rname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByPhone(self,rname, phone):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId natural inner join address natural inner join city  where rname = %s and phone = %s;"
        cursor.execute(query, (rname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result
