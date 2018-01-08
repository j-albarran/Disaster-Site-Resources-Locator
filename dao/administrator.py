from config.dbconfig import conn


class AdministratorDAO:
    def __init__(self):
        self.conn = conn

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    def getAllAdministrators(self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorById(adminId, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where administrator.adminId = %s;"
        cursor.execute(query, (adminId,))
        result = cursor.fetchone()
        return result

    def getAdministratorsByAFirstALastEmailPhone(afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (afirst, alast, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirstALastEmail(afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (afirst, alast, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirstALastPhone(afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (afirst, alast, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirstPhoneEmail(afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (afirst, phone, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByALastEmailPhone(alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (alast, email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirstALast(afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s and alast = %s;"
        cursor.execute(query, (afirst, alast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirstEmail(afirst, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s and email = %s;"
        cursor.execute(query, (afirst, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirstPhone(afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s and phone = %s;"
        cursor.execute(query, (afirst, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByALastEmail(alast, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where alast = %s and email = %s;"
        cursor.execute(query, (alast, email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByALastPhone(alast, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where alast = %s and phone = %s;"
        cursor.execute(query, (alast, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByEmailPhone(email, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where email = %s and phone = %s;"
        cursor.execute(query, (email, phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByAFirst(afirst, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where afirst = %s;"
        cursor.execute(query, (afirst,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByALast(alast, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where alast = %s;"
        cursor.execute(query, (alast,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByEmail(email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where email = %s;"
        cursor.execute(query, (email,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsByPhone(phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone inner join administrator on account.aid = administrator.adminId where phone = %s;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsWithThisAddressID(addId, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s;"
        cursor.execute(query, (addId, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByAfirstAlastEmailPhone(addId, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, email, phone, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByAfirstAlastEmail(addId, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, afirst, alast, email, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByAfirstAlastPhone(addId, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, phone, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByAfirstPhoneEmail(addId, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (addId, afirst, phone, email, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByAlastEmailPhone(addId, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, alast, email, phone, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByAfirstAlast(addId, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (addId, afirst, alast, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByAfirstEmail(addId, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and afirst = %s and email = %s;"
        cursor.execute(query, (addId, afirst, email, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByAfirstPhone(addId, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, phone, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByAlastEmail(addId, alast, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, alast, email, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByAlastPhone(addId, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, alast, phone, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByEmailPhone(addId, email, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, email, phone, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByAfirst(addId, afirst, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and afirst = %s;"
        cursor.execute(query, (addId, afirst, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByAlast(addId, alast, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and alast = %s;"
        cursor.execute(query, (addId, alast, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByEmail(addId, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and email = %s;"
        cursor.execute(query, (addId, email, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisAddressIDByPhone(addId, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where addId = %s and phone = %s;"
        cursor.execute(query, (addId, phone, ))
        result = cursor.fetchone()
        return result

    def getAdministratorsOnThisCity(cname, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s;"
        cursor.execute(query, (cname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityAfirstAlastEmailPhone(cname, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAfirstAlastEmail(cname, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAfirstAlastPhone(cname, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAfirstPhoneEmail(cname, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAlastEmailPhone(cname, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAfirstAlast(cname, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAfirstEmail(cname, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAfirstPhone(cname, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAlastEmail(cname, alast, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAlastPhone(cname, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByEmailPhone(cname, email, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAfirst(cname, afirst, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and afirst = %s;"
        cursor.execute(query, (cname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByAlast(cname, alast, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and alast = %s;"
        cursor.execute(query, (cname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByEmail(cname, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and email = %s;"
        cursor.execute(query, (cname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisCityByPhone(cname, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address inner join administrator on account.aid = administrator.adminId where cname = %s and phone = %s;"
        cursor.execute(query, (cname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegion(rname, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s;"
        cursor.execute(query, (rname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionAfirstAlastEmailPhone(rname, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAfirstAlastEmail(rname, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAfirstAlastPhone(rname, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAfirstPhoneEmail(rname, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (rname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAlastEmailPhone(rname, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAfirstAlast(rname, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (rname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAfirstEmail(rname, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and afirst = %s and email = %s;"
        cursor.execute(query, (rname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAfirstPhone(rname, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (rname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAlastEmail(rname, alast, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and alast = %s and email = %s;"
        cursor.execute(query, (rname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAlastPhone(rname, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and alast = %s and phone = %s;"
        cursor.execute(query, (rname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByEmailPhone(rname, email, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and email = %s and phone = %s;"
        cursor.execute(query, (rname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAfirst(rname, afirst, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and afirst = %s;"
        cursor.execute(query, (rname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByAlast(rname, alast, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and alast = %s;"
        cursor.execute(query, (rname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByEmail(rname, email, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and email = %s;"
        cursor.execute(query, (rname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorsOnThisRegionByPhone(rname, phone, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city inner join administrator on account.aid = administrator.adminId where rname = %s and phone = %s;"
        cursor.execute(query, (rname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result