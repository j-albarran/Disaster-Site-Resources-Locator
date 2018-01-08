from config.dbconfig import conn

class AccountDAO:
    def __init__(self):
        self.conn = conn

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    def getAllAccounts(self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountById(aid, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where aid = %s;"
        cursor.execute(query, (aid,))
        result = cursor.fetchone()
        return result

    def getAccountsByAFirstALastEmailPhone(afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select * from account natural inner join phone where afirst = %s and alast = %s and email = %s and phone =%s;"
        cursor.execute(query, (afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByAFirstALastEmail(afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where afirst = %s and alast = %s and email =%s;"
        cursor.execute(query, (afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByAFirstALastPhone(afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where afirst = %s and alast = %s and phone =%s;"
        cursor.execute(query, (afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByAFirstPhoneEmail(afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where afirst = %s and phone = %s and email =%s;"
        cursor.execute(query, (afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByALastEmailPhone(alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where alast = %s and email = %s and phone =%s;"
        cursor.execute(query, (alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByAFirstALast(afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where afirst = %s and alast = %s;"
        cursor.execute(query, (afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByAFirstEmail(afirst, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where afirst = %s and email = %s;"
        cursor.execute(query, (afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByAFirstPhone(afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where afirst = %s and phone = %s;"
        cursor.execute(query, (afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByALastEmail(alast, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where alast = %s and email = %s;"
        cursor.execute(query, (alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByALastPhone(alast, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where alast = %s and phone = %s;"
        cursor.execute(query, (alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByEmailPhone(email, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where email = %s and phone = %s;"
        cursor.execute(query, (email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByAFirst(afirst, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where afirst = %s;"
        cursor.execute(query, (afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByALast(alast, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where alast = %s;"
        cursor.execute(query, (alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByEmail(email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where email = %s;"
        cursor.execute(query, (email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByPhone(phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where phone = %s;"
        cursor.execute(query, (phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisAddressID(addId, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s;"
        cursor.execute(query, (addId, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByAfirstAlastEmailPhone(addId, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, email, phone, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByAfirstAlastEmail(addId, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, afirst, alast, email, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByAfirstAlastPhone(addId, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, phone, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByAfirstPhoneEmail(addId, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (addId, afirst, phone, email, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByAlastEmailPhone(addId, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, alast, email, phone, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByAfirstAlast(addId, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (addId, afirst, alast, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByAfirstEmail(addId, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s and email = %s;"
        cursor.execute(query, (addId, afirst, email, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByAfirstPhone(addId, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, phone, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByAlastEmail(addId, alast, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, alast, email, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByAlastPhone(addId, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, alast, phone, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByEmailPhone(addId, email, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, email, phone, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByAfirst(addId, afirst, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s;"
        cursor.execute(query, (addId, afirst, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByAlast(addId, alast, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and alast = %s;"
        cursor.execute(query, (addId, alast, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByEmail(addId, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and email = %s;"
        cursor.execute(query, (addId, email, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisAddressIDByPhone(addId, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and phone = %s;"
        cursor.execute(query, (addId, phone, ))
        result = cursor.fetchone()
        return result

    def getAccountsOnThisCity(cname, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s;"
        cursor.execute(query, (cname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityAfirstAlastEmailPhone(cname, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAfirstAlastEmail(cname, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAfirstAlastPhone(cname, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAfirstPhoneEmail(cname, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAlastEmailPhone(cname, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAfirstAlast(cname, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAfirstEmail(cname, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAfirstPhone(cname, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAlastEmail(cname, alast, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAlastPhone(cname, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByEmailPhone(cname, email, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAfirst(cname, afirst, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s;"
        cursor.execute(query, (cname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAlast(cname, alast, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and alast = %s;"
        cursor.execute(query, (cname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByEmail(cname, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and email = %s;"
        cursor.execute(query, (cname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByPhone(cname, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and phone = %s;"
        cursor.execute(query, (cname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegion(rname, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s;"
        cursor.execute(query, (rname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionAfirstAlastEmailPhone(rname, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s and alast =%s and email =%s and phone = %s;"
        cursor.execute(query, (rname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAfirstAlastEmail(rname, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s and alast =%s and email =%s;"
        cursor.execute(query, (rname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAfirstAlastPhone(rname, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s and alast =%s and phone =%s;"
        cursor.execute(query, (rname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAfirstPhoneEmail(rname, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s and phone =%s and email =%s;"
        cursor.execute(query, (rname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAlastEmailPhone(rname, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and alast = %s and email =%s and phone =%s;"
        cursor.execute(query, (rname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAfirstAlast(rname, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s and alast =%s;"
        cursor.execute(query, (rname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAfirstEmail(rname, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s and email =%s;"
        cursor.execute(query, (rname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAfirstPhone(rname, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s and phone =%s;"
        cursor.execute(query, (rname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAlastEmail(rname, alast, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and alast = %s and email =%s;"
        cursor.execute(query, (rname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAlastPhone(rname, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and alast = %s and phone =%s;"
        cursor.execute(query, (rname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByEmailPhone(rname, email, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and email = %s and phone =%s;"
        cursor.execute(query, (rname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAfirst(rname, afirst, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s;"
        cursor.execute(query, (rname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAlast(rname, alast, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and alast = %s;"
        cursor.execute(query, (rname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByEmail(rname, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and email = %s;"
        cursor.execute(query, (rname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByPhone(rname, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and phone = %s;"
        cursor.execute(query, (rname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountWithThisUsername(username, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s;"
        cursor.execute(query, (username, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByAfirstAlastEmailPhone(username, afirst, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (username, afirst, alast, email, phone, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByAfirstAlastEmail(username, afirst, alast, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (username, afirst, alast, email, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByAfirstAlastPhone(username, afirst, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (username, afirst, alast, phone, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByAfirstPhoneEmail(username, afirst, phone, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (username, afirst, phone, email, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByAlastEmailPhone(username, alast, email, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (username, alast, email, phone, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByAfirstAlast(username, afirst, alast, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (username, afirst, alast, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByAfirstEmail(username, afirst, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s and email = %s;"
        cursor.execute(query, (username, afirst, email, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByAfirstPhone(username, afirst, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (username, afirst, phone, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByAlastEmail(username, alast, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and alast = %s and email = %s;"
        cursor.execute(query, (username, alast, email, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByAlastPhone(username, alast, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and alast = %s and phone = %s;"
        cursor.execute(query, (username, alast, phone, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByEmailPhone(username, email, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and email = %s and phone = %s;"
        cursor.execute(query, (username, email, phone, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByAfirst(username, afirst, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s;"
        cursor.execute(query, (username, afirst, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByAlast(username, alast, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and alast = %s;"
        cursor.execute(query, (username, alast, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByEmail(username, email, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and email = %s;"
        cursor.execute(query, (username, email, ))
        result = cursor.fetchone()
        return result

    def getAccountsWithThisUsernameByPhone(username, phone, self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and phone = %s;"
        cursor.execute(query, (username, phone, ))
        result = cursor.fetchone()
        return result