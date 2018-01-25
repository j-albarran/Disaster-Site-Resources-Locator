from config.dbconfig import conn

class AddressDAO:
    def __init__(self):
        self.conn = conn

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    # ============ #
    #    Updates   #
    # ============ #

    def addNewAddress(self, street, number, unit, zipcode, aid, cname):
        cursor = self.conn.cursor()
        query = "insert into address(street, number, unit, zipcode, aid, cname) values(%s, %s, %s, %s, %s, %s) returning addId;"
        cursor.execute(query, (street, number, unit, zipcode, aid, cname, ))
        addId = cursor.fetchone()[0]
        self.conn.commit()
        return addId

    def updateAddress(self, addId, street, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "update address set street = %s, number = %s, unit = %s, zipcode = %s where addId = %s;"
        cursor.execute(query, (street, number, unit, zipcode, addId,))
        self.conn.commit()
        return addId

    def deleteAddress(self, addId):
        cursor = self.conn.cursor()
        query = "delete from address where addId = %s;"
        cursor.execute(query, (addId,))
        self.conn.commit()
        return addId


        # ============ #
        #    Gets      #
        # ============ #

    def getAllAddresses(self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressById(self,addId):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where addId = %s;"
        cursor.execute(query, (addId, ))
        result = cursor.fetchone()
        return result

    def getAddressByStreetNumberUnitZipCode(self,street, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where street = %s and number = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (street, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStreetNumberUnit(self,street, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where street = %s and number = %s and unit = %s;"
        cursor.execute(query, (street, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStreetNumberZipCode(self,street, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where street = %s and number = %s and zipcode = %s;"
        cursor.execute(query, (street, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStreetZipCodeUnit(self,street, zipcode, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where street = %s and zipcode = %s and unit = %s;"
        cursor.execute(query, (street, zipcode, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByNumberUnitZipCode(self,number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where number = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStreetNumber(self,street, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where street = %s and number = %s;"
        cursor.execute(query, (street, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStreetUnit(self,street, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where street = %s and unit = %s;"
        cursor.execute(query, (street, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStreetZipCode(self,street, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where street = %s and zipcode = %s;"
        cursor.execute(query, (street, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByNumberUnit(self,number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where number = %s and unit = %s;"
        cursor.execute(query, (number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByNumberZipCode(self,number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where number = %s and zipcode = %s;"
        cursor.execute(query, (number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByUnitZipCode(self,unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where unit = %s and zipcode = %s;"
        cursor.execute(query, (unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStreet(self,street):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where street = %s;"
        cursor.execute(query, (street, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByNumber(self,number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where number = %s;"
        cursor.execute(query, (number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByUnit(self,unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where unit = %s;"
        cursor.execute(query, (unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByZipCode(self,zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where zipcode = %s;"
        cursor.execute(query, (zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddress(self,aid):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s;"
        cursor.execute(query, (aid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByStreetNumberUnitZipCode(self,aid, street, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and street = %s and number = %s and unit = %s and zipcode=%s;"
        cursor.execute(query, (aid, street, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByStreetNumberUnit(self,aid, street, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and street = %s and number = %s and unit = %s;"
        cursor.execute(query, (aid, street, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByStreetNumberZipCode(self,aid, street, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and street = %s and number = %s and zipcode = %s;"
        cursor.execute(query, (aid, street, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByStreetZipCodeUnit(self,aid, street, zipcode, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and street = %s and zipcode = %s and unit = %s;"
        cursor.execute(query, (aid, street, zipcode, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByNumberUnitZipCode(self,aid, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and number = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (aid, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByStreetNumber(self,aid, street, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and street = %s and number = %s;"
        cursor.execute(query, (aid, street, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByStreetUnit(self,aid, street, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and street = %s and unit = %s;"
        cursor.execute(query, (aid, street, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByStreetZipCode(self,aid, street, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and street = %s and zipcode = %s;"
        cursor.execute(query, (aid, street, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByNumberUnit(self,aid, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and number = %s and unit = %s;"
        cursor.execute(query, (aid, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByNumberZipCode(self,aid, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and number = %s and zipcode = %s;"
        cursor.execute(query, (aid, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByUnitZipCode(self,aid, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (aid, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByStreet(self,aid, street):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and street = %s;"
        cursor.execute(query, (aid, street, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByNumber(self,aid, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and number = %s;"
        cursor.execute(query, (aid, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByUnit(self,aid, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and unit = %s;"
        cursor.execute(query, (aid, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByZipCode(self,aid, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account natural inner join address where aid = %s and zipcode = %s;"
        cursor.execute(query, (aid, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddress(self,adminId):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s;"
        cursor.execute(query, (adminId, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByStreetNumberUnitZipCode(self,adminId, street, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s and number = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (adminId, street, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByStreetNumberUnit(self,adminId, street, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s and number = %s and unit = %s;"
        cursor.execute(query, (adminId, street, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByStreetNumberZipCode(self,adminId, street, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s and number = %s and zipcode = %s;"
        cursor.execute(query, (adminId, street, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByStreetZipCodeUnit(self,adminId, street, zipcode, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s and zipcode = %s and unit = %s;"
        cursor.execute(query, (adminId, street, zipcode, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByNumberUnitZipCode(self,adminId, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and number = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (adminId, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByStreetNumber(self,adminId, street, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s and number = %s;"
        cursor.execute(query, (adminId, street, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByStreetUnit(self,adminId, street, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s and unit = %s;"
        cursor.execute(query, (adminId, street, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByStreetZipCode(self,adminId, street, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s and zipcode = %s;"
        cursor.execute(query, (adminId, street, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByNumberUnit(self,adminId, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and number = %s and unit = %s;"
        cursor.execute(query, (adminId, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByNumberZipCode(self,adminId, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and number = %s and zipcode = %s;"
        cursor.execute(query, (adminId, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByUnitZipCode(self,adminId, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (adminId, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByStreet(self,adminId, street):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s;"
        cursor.execute(query, (adminId, street, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByNumber(self,adminId, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and number = %s;"
        cursor.execute(query, (adminId, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByUnit(self,adminId, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and unit = %s;"
        cursor.execute(query, (adminId, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdministratorAddressesByZipCode(self,adminId, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and zipcode = %s;"
        cursor.execute(query, (adminId, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddress(self, sid):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByStreetNumberUnitZipCode(self,sid, street, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s and number = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (sid, street, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByStreetNumberUnit(self,sid, street, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s and number = %s and unit = %s;"
        cursor.execute(query, (sid, street, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByStreetNumberZipCode(self,sid, street, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s and number = %s and zipcode = %s;"
        cursor.execute(query, (sid, street, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByStreetZipCodeUnit(self,sid, street, zipcode, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s and zipcode = %s and unit = %s;"
        cursor.execute(query, (sid, street, zipcode, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByNumberUnitZipCode(self,sid, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and number = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (sid, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByStreetNumber(self,sid, street, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s and number = %s;"
        cursor.execute(query, (sid, street, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByStreetUnit(self,sid, street, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s and unit = %s;"
        cursor.execute(query, (sid, street, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByStreetZipCode(self,sid, street, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s and zipcode = %s;"
        cursor.execute(query, (sid, street, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByNumberUnit(self,sid, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and number = %s and unit = %s;"
        cursor.execute(query, (sid, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByNumberZipCode(self,sid, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and number = %s and zipcode = %s;"
        cursor.execute(query, (sid, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByUnitZipCode(self,sid, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (sid, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByStreet(self,sid, street):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s;"
        cursor.execute(query, (sid, street, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByNumber(self,sid, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and number = %s;"
        cursor.execute(query, (sid, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByUnit(self,sid, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and unit = %s;"
        cursor.execute(query, (sid, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierAddressesByZipCode(self,sid, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and zipcode = %s;"
        cursor.execute(query, (sid, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddress(self,rid):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s;"
        cursor.execute(query, (rid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByStreetNumberUnitZipCode(self,rid, street, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s and number = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (rid, street, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByStreetNumberUnit(self,rid, street, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s and number = %s and unit = %s;"
        cursor.execute(query, (rid, street, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByStreetNumberZipCode(self,rid, street, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s and number = %s and zipcode = %s;"
        cursor.execute(query, (rid, street, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByStreetZipCodeUnit(self,rid, street, zipcode, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s and zipcode = %s and unit = %s;"
        cursor.execute(query, (rid, street, zipcode, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByNumberUnitZipCode(self,rid, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and number = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (rid, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByStreetNumber(self,rid, street, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s and number = %s;"
        cursor.execute(query, (rid, street, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByStreetUnit(self,rid, street, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s and unit = %s;"
        cursor.execute(query, (rid, street, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByStreetZipCode(self,rid, street, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s and zipcode = %s;"
        cursor.execute(query, (rid, street, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByNumberUnit(self,rid, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and number = %s and unit = %s;"
        cursor.execute(query, (rid, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByNumberZipCode(self,rid, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and number = %s and zipcode = %s;"
        cursor.execute(query, (rid, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByUnitZipCode(self,rid, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (rid, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByStreet(self,rid, street):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s;"
        cursor.execute(query, (rid, street, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByNumber(self,rid, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and number = %s;"
        cursor.execute(query, (rid, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByUnit(self,rid, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and unit = %s;"
        cursor.execute(query, (rid, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterAddressesByZipCode(self,rid, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and zipcode = %s;"
        cursor.execute(query, (rid, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCity(self,cname):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s;"
        cursor.execute(query, (cname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressOnThisCityByStreetNumberUnitZipCode(self,cname, street, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and street = %s and number = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (cname, street, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByStreetNumberUnit(self,cname, street, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and street = %s and number = %s and unit = %s;"
        cursor.execute(query, (cname, street, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByStreetNumberZipCode(self,cname, street, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and street = %s and number = %s and zipcode = %s;"
        cursor.execute(query, (cname, street, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByStreetZipCodeUnit(self,cname, street, zipcode, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and street = %s and zipcode = %s and unit = %s;"
        cursor.execute(query, (cname, street, zipcode, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByNumberUnitZipCode(self,cname, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and number = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (cname, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByStreetNumber(self,cname, street, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and street = %s and number = %s;"
        cursor.execute(query, (cname, street, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByStreetUnit(self,cname, street, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and street = %s and unit = %s;"
        cursor.execute(query, (cname, street, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByStreetZipCode(self,cname, street, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and street = %s and zipcode = %s;"
        cursor.execute(query, (cname, street, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByNumberUnit(self,cname, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and number = %s and unit = %s;"
        cursor.execute(query, (cname, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByNumberZipCode(self,cname, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and number = %s and zipcode = %s;"
        cursor.execute(query, (cname, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByUnitZipCode(self,cname, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (cname, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByStreet(self,cname, street):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and street = %s;"
        cursor.execute(query, (cname, street, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByNumber(self,cname, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and number = %s;"
        cursor.execute(query, (cname, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByUnit(self,cname, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and unit = %s;"
        cursor.execute(query, (cname, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByZipCode(self,cname, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address where cname = %s and zipcode = %s;"
        cursor.execute(query, (cname, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegion(self,rname):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s;"
        cursor.execute(query, (rname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressOnThisRegionByStreetNumberUnitZipCode(self,rname, street, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and street = %s and number = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (rname, street, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByStreetNumberUnit(self,rname, street, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and street = %s and number = %s and unit = %s;"
        cursor.execute(query, (rname, street, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByStreetNumberZipCode(self,rname, street, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and street = %s and number = %s and zipcode = %s;"
        cursor.execute(query, (rname, street, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByStreetZipCodeUnit(self,rname, street, zipcode, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and street = %s and zipcode = %s and unit = %s;"
        cursor.execute(query, (rname, street, zipcode, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByNumberUnitZipCode(self,rname, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and number = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (rname, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByStreetNumber(self,rname, street, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and street = %s and number = %s;"
        cursor.execute(query, (rname, street, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByStreetUnit(self,rname, street, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and street = %s and unit = %s;"
        cursor.execute(query, (rname, street, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByStreetZipCode(self,rname, street, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and street = %s and zipcode = %s;"
        cursor.execute(query, (rname, street, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByNumberUnit(self,rname, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and number = %s and unit = %s;"
        cursor.execute(query, (rname, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByNumberZipCode(self,rname, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and number = %s and zipcode = %s;"
        cursor.execute(query, (rname, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByUnitZipCode(self,rname, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and unit = %s and zipcode = %s;"
        cursor.execute(query, (rname, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByStreet(self,rname, street):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and street = %s;"
        cursor.execute(query, (rname, street, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByNumber(self,rname, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and number = %s;"
        cursor.execute(query, (rname, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByUnit(self,rname, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and unit = %s;"
        cursor.execute(query, (rname, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByZipCode(self,rname, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join city where rname = %s and zipcode = %s;"
        cursor.execute(query, (rname, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardAddress(self,cid):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s"
        cursor.execute(query, (cid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressOnThisCreditCardByStreetNumberUnitZipCode(self,cid, street, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and street = %s and number = %s and unit = %s and zipcode = %s"
        cursor.execute(query, (cid, street, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCreditCardByStreetNumberUnit(self,cid, street, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and street = %s and number = %s and unit = %s"
        cursor.execute(query, (cid, street, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCreditCardByStreetNumberZipCode(self,cid, street, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and street = %s and number = %s and zipcode = %s"
        cursor.execute(query, (cid, street, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCreditCardByStreetZipCodeUnit(self,cid, street, zipcode, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and street = %s and zipcode = %s and unit = %s"
        cursor.execute(query, (cid, street, zipcode, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCreditCardByNumberUnitZipCode(self,cid, number, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and number = %s and unit = %s and zipcode = %s"
        cursor.execute(query, (cid, number, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCreditCardByStreetNumber(self,cid, street, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and street = %s and number = %s"
        cursor.execute(query, (cid, street, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCreditCardByStreetUnit(self,cid, street, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and street = %s and unit = %s"
        cursor.execute(query, (cid, street, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCreditCardByStreetZipCode(self,cid, street, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and street = %s and zipcode = %s"
        cursor.execute(query, (cid, street, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCreditCardByNumberUnit(self,cid, number, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and number = %s and unit = %s"
        cursor.execute(query, (cid, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCreditCardByNumberZipCode(self,cid, number, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and number = %s and zipcode = %s"
        cursor.execute(query, (cid, number, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCreditCardByUnitZipCode(self,cid, unit, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and unit = %s and zipcode = %s"
        cursor.execute(query, (cid, unit, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCreditCardByStreet(self,cid, street):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and street = %s;"
        cursor.execute(query, (cid, street, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCreditCardByNumber(self,cid, number):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and number = %s;"
        cursor.execute(query, (cid, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCreditCardByUnit(self,cid, unit):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and unit = %s;"
        cursor.execute(query, (cid, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCreditCardByZipCode(self,cid, zipcode):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zipcode from address natural inner join credit_card where cid = %s and zipcode = %s;"
        cursor.execute(query, (cid, zipcode, ))
        result = []
        for row in cursor:
            result.append(row)
        return result
