from config.dbconfig import conn

class AccountDAO:
    def __init__(self):
        self.conn = conn

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    # ============ #
    #    Updates   #
    # ============ #

    def addNewAccount(self, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "insert into account(afirst, alast, email) values(%s, %s, %s) returning aid;"
        cursor.execute(query, (afirst, alast, email,))
        aid = cursor.fetchone()[0]
        query = "insert into phone(aid, phone) values(%s, %s);"
        cursor.execute(query, (aid, phone, ))
        self.conn.commit()
        return aid

    def updateAccount(self, aid, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "update account set afirst = %s, alast = %s, email = %s where aid = %s;"
        cursor.execute(query, (afirst, alast, email, aid, ))
        query = "update phone set phone = %s where aid = %s;"
        cursor.execute(query, (phone, aid, ))
        self.conn.commit()
        return aid

    def deleteAccount(self, aid):
        cursor = self.conn.cursor()
        query = "delete from phone where aid = %s;"
        cursor.execute(query, (aid,))
        query = "delete from account where aid = %s;"
        cursor.execute(query, (aid,))
        self.conn.commit()
        return aid


        # ============ #
        #    Gets      #
        # ============ #

    def getAllAccounts(self):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountById(self, aid):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where aid = %s;"
        cursor.execute(query, (aid,))
        result = cursor.fetchone()
        return result

    def getAccountsByAFirstALastEmailPhone(self,afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select * from account natural inner join phone where afirst = %s and alast = %s and email = %s and phone =%s;"
        cursor.execute(query, (afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByAFirstALastEmail(self,afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where afirst = %s and alast = %s and email =%s;"
        cursor.execute(query, (afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByAFirstALastPhone(self,afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where afirst = %s and alast = %s and phone =%s;"
        cursor.execute(query, (afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByAFirstPhoneEmail(self,afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where afirst = %s and phone = %s and email =%s;"
        cursor.execute(query, (afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByALastEmailPhone(self,alast, email, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where alast = %s and email = %s and phone =%s;"
        cursor.execute(query, (alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByAFirstALast(self,afirst, alast):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where afirst = %s and alast = %s;"
        cursor.execute(query, (afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByAFirstEmail(self,afirst, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where afirst = %s and email = %s;"
        cursor.execute(query, (afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByAFirstPhone(self,afirst, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where afirst = %s and phone = %s;"
        cursor.execute(query, (afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByALastEmail(self,alast, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where alast = %s and email = %s;"
        cursor.execute(query, (alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByALastPhone(self,alast, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where alast = %s and phone = %s;"
        cursor.execute(query, (alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByEmailPhone(self,email, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where email = %s and phone = %s;"
        cursor.execute(query, (email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByAFirst(self,afirst):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where afirst = %s;"
        cursor.execute(query, (afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByALast(self,alast):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where alast = %s;"
        cursor.execute(query, (alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByEmail(self,email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where email = %s;"
        cursor.execute(query, (email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsByPhone(self,phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone where phone = %s;"
        cursor.execute(query, (phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisAddressID(self,addId):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s;"
        cursor.execute(query, (addId, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByAfirstAlastEmailPhone(self,addId, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByAfirstAlastEmail(self,addId, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByAfirstAlastPhone(self,addId, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByAfirstPhoneEmail(self,addId, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (addId, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByAlastEmailPhone(self,addId, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByAfirstAlast(self,addId, afirst, alast):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (addId, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByAfirstEmail(self,addId, afirst, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s and email = %s;"
        cursor.execute(query, (addId, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByAfirstPhone(self,addId, afirst, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (addId, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByAlastEmail(self,addId, alast, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and alast = %s and email = %s;"
        cursor.execute(query, (addId, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByAlastPhone(self,addId, alast, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and alast = %s and phone = %s;"
        cursor.execute(query, (addId, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByEmailPhone(self,addId, email, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and email = %s and phone = %s;"
        cursor.execute(query, (addId, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByAfirst(self,addId, afirst):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and afirst = %s;"
        cursor.execute(query, (addId, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByAlast(self,addId, alast):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and alast = %s;"
        cursor.execute(query, (addId, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByEmail(self,addId, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and email = %s;"
        cursor.execute(query, (addId, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisAddressIDByPhone(self,addId, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where addId = %s and phone = %s;"
        cursor.execute(query, (addId, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCity(self,cname):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s;"
        cursor.execute(query, (cname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityAfirstAlastEmailPhone(self,cname, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAfirstAlastEmail(self,cname, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAfirstAlastPhone(self,cname, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAfirstPhoneEmail(self,cname, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (cname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAlastEmailPhone(self,cname, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAfirstAlast(self,cname, afirst, alast):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (cname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAfirstEmail(self,cname, afirst, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s and email = %s;"
        cursor.execute(query, (cname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAfirstPhone(self,cname, afirst, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (cname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAlastEmail(self,cname, alast, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and alast = %s and email = %s;"
        cursor.execute(query, (cname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAlastPhone(self,cname, alast, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and alast = %s and phone = %s;"
        cursor.execute(query, (cname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByEmailPhone(self,cname, email, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and email = %s and phone = %s;"
        cursor.execute(query, (cname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAfirst(self,cname, afirst):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and afirst = %s;"
        cursor.execute(query, (cname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByAlast(self,cname, alast):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and alast = %s;"
        cursor.execute(query, (cname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByEmail(self,cname, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and email = %s;"
        cursor.execute(query, (cname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisCityByPhone(self,cname, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address where cname = %s and phone = %s;"
        cursor.execute(query, (cname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegion(self,rname):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s;"
        cursor.execute(query, (rname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionAfirstAlastEmailPhone(self,rname, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s and alast =%s and email =%s and phone = %s;"
        cursor.execute(query, (rname, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAfirstAlastEmail(self,rname, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s and alast =%s and email =%s;"
        cursor.execute(query, (rname, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAfirstAlastPhone(self,rname, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s and alast =%s and phone =%s;"
        cursor.execute(query, (rname, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAfirstPhoneEmail(self,rname, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s and phone =%s and email =%s;"
        cursor.execute(query, (rname, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAlastEmailPhone(self,rname, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and alast = %s and email =%s and phone =%s;"
        cursor.execute(query, (rname, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAfirstAlast(self,rname, afirst, alast):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s and alast =%s;"
        cursor.execute(query, (rname, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAfirstEmail(self,rname, afirst, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s and email =%s;"
        cursor.execute(query, (rname, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAfirstPhone(self,rname, afirst, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s and phone =%s;"
        cursor.execute(query, (rname, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAlastEmail(self,rname, alast, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and alast = %s and email =%s;"
        cursor.execute(query, (rname, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAlastPhone(self,rname, alast, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and alast = %s and phone =%s;"
        cursor.execute(query, (rname, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByEmailPhone(self,rname, email, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and email = %s and phone =%s;"
        cursor.execute(query, (rname, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAfirst(self,rname, afirst):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and afirst = %s;"
        cursor.execute(query, (rname, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByAlast(self,rname, alast):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and alast = %s;"
        cursor.execute(query, (rname, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByEmail(self, rname, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and email = %s;"
        cursor.execute(query, (rname, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsOnThisRegionByPhone(self, rname, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join address natural inner join city where rname = %s and phone = %s;"
        cursor.execute(query, (rname, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountWithThisUsername(self, username):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s;"
        cursor.execute(query, (username, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByAfirstAlastEmailPhone(self, username, afirst, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (username, afirst, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByAfirstAlastEmail(self, username, afirst, alast, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s and alast = %s and email = %s;"
        cursor.execute(query, (username, afirst, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByAfirstAlastPhone(self, username, afirst, alast, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s and alast = %s and phone = %s;"
        cursor.execute(query, (username, afirst, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByAfirstPhoneEmail(self, username, afirst, phone, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s and phone = %s and email = %s;"
        cursor.execute(query, (username, afirst, phone, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByAlastEmailPhone(self, username, alast, email, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and alast = %s and email = %s and phone = %s;"
        cursor.execute(query, (username, alast, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByAfirstAlast(self, username, afirst, alast):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s and alast = %s;"
        cursor.execute(query, (username, afirst, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByAfirstEmail(self, username, afirst, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s and email = %s;"
        cursor.execute(query, (username, afirst, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByAfirstPhone(self, username, afirst, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s and phone = %s;"
        cursor.execute(query, (username, afirst, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByAlastEmail(self, username, alast, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and alast = %s and email = %s;"
        cursor.execute(query, (username, alast, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByAlastPhone(self, username, alast, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and alast = %s and phone = %s;"
        cursor.execute(query, (username, alast, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByEmailPhone(self, username, email, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and email = %s and phone = %s;"
        cursor.execute(query, (username, email, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByAfirst(self, username, afirst):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and afirst = %s;"
        cursor.execute(query, (username, afirst, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByAlast(self, username, alast):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and alast = %s;"
        cursor.execute(query, (username, alast, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByEmail(self, username, email):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and email = %s;"
        cursor.execute(query, (username, email, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountsWithThisUsernameByPhone(self, username, phone):
        cursor = self.conn.cursor()
        query = "select aid, afirst, alast, email, phone from account natural inner join phone natural inner join credentials where username = %s and phone = %s;"
        cursor.execute(query, (username, phone, ))
        result = []
        for row in cursor:
            result.append(row)
        return result