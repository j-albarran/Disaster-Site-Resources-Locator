from config.dbconfig import conn

class AddressDAO:
    def __init__(self):
        self.conn = conn

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    def getAllAddresses(self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressById(addId, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where addId = %s;"
        cursor.execute(query, (addId, ))
        result = cursor.fetchone()
        return result

    def getAddressByStreetNumberUnitZipCode(street, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where street = %s and number = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (street, number, unit, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStreetNumberUnit(street, number, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where street = %s and number = %s and unit = %s;"
        cursor.execute(query, (street, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStreetNumberZipCode(street, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where street = %s and number = %s and zip_code = %s;"
        cursor.execute(query, (street, number, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStreetZipCodeUnit(street, zip_code, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where street = %s and zip_code = %s and unit = %s;"
        cursor.execute(query, (street, zip_code, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByNumberUnitZipCode(number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where number = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (number, unit, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStreetNumber(street, number, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where street = %s and number = %s;"
        cursor.execute(query, (street, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStreetUnit(street, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where street = %s and unit = %s;"
        cursor.execute(query, (street, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStreetZipCode(street, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where street = %s and zip_code = %s;"
        cursor.execute(query, (street, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByNumberUnit(number, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where number = %s and unit = %s;"
        cursor.execute(query, (number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByNumberZipCode(number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where number = %s and zip_code = %s;"
        cursor.execute(query, (number, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByUnitZipCode(unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where unit = %s and zip_code = %s;"
        cursor.execute(query, (unit, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByStreet(street, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where street = %s;"
        cursor.execute(query, (street, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByNumber(number, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where number = %s;"
        cursor.execute(query, (number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByUnit(unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where unit = %s;"
        cursor.execute(query, (unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesByZipCode(zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where zip_code = %s;"
        cursor.execute(query, (zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddress(aid, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s;"
        cursor.execute(query, (aid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAccountAddressesByStreetNumberUnitZipCode(aid, street, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and street = %s and number = %s and unit = %s and zip_code=%s;"
        cursor.execute(query, (aid, street, number, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAccountAddressesByStreetNumberUnit(aid, street, number, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and street = %s and number = %s and unit = %s;"
        cursor.execute(query, (aid, street, number, unit, ))
        result = cursor.fetchone()
        return result

    def getAccountAddressesByStreetNumberZipCode(aid, street, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and street = %s and number = %s and zip_code = %s;"
        cursor.execute(query, (aid, street, number, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAccountAddressesByStreetZipCodeUnit(aid, street, zip_code, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and street = %s and zip_code = %s and unit = %s;"
        cursor.execute(query, (aid, street, zip_code, unit, ))
        result = cursor.fetchone()
        return result

    def getAccountAddressesByNumberUnitZipCode(aid, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and number = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (aid, number, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAccountAddressesByStreetNumber(aid, street, number, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and street = %s and number = %s;"
        cursor.execute(query, (aid, street, number, ))
        result = cursor.fetchone()
        return result

    def getAccountAddressesByStreetUnit(aid, street, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and street = %s and unit = %s;"
        cursor.execute(query, (aid, street, unit, ))
        result = cursor.fetchone()
        return result

    def getAccountAddressesByStreetZipCode(aid, street, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and street = %s and zip_code = %s;"
        cursor.execute(query, (aid, street, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAccountAddressesByNumberUnit(aid, number, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and number = %s and unit = %s;"
        cursor.execute(query, (aid, number, unit, ))
        result = cursor.fetchone()
        return result

    def getAccountAddressesByNumberZipCode(aid, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and number = %s and zip_code = %s;"
        cursor.execute(query, (aid, number, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAccountAddressesByUnitZipCode(aid, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (aid, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAccountAddressesByStreet(aid, street, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and street = %s;"
        cursor.execute(query, (aid, street, ))
        result = cursor.fetchone()
        return result

    def getAccountAddressesByNumber(aid, number, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and number = %s;"
        cursor.execute(query, (aid, number, ))
        result = cursor.fetchone()
        return result

    def getAccountAddressesByUnit(aid, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and unit = %s;"
        cursor.execute(query, (aid, unit, ))
        result = cursor.fetchone()
        return result

    def getAccountAddressesByZipCode(aid, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from account natural inner join address where aid = %s and zip_code = %s;"
        cursor.execute(query, (aid, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddress(adminId, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s;"
        cursor.execute(query, (adminId, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByStreetNumberUnitZipCode(adminId, street, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s and number = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (adminId, street, number, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByStreetNumberUnit(adminId, street, number, unit, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s and number = %s and unit = %s;"
        cursor.execute(query, (adminId, street, number, unit, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByStreetNumberZipCode(adminId, street, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s and number = %s and zip_code = %s;"
        cursor.execute(query, (adminId, street, number, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByStreetZipCodeUnit(adminId, street, zip_code, unit, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s and zip_code = %s and unit = %s;"
        cursor.execute(query, (adminId, street, zip_code, unit, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByNumberUnitZipCode(adminId, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and number = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (adminId, number, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByStreetNumber(adminId, street, number, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s and number = %s;"
        cursor.execute(query, (adminId, street, number, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByStreetUnit(adminId, street, unit, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s and unit = %s;"
        cursor.execute(query, (adminId, street, unit, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByStreetZipCode(adminId, street, zip_code, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s and zip_code = %s;"
        cursor.execute(query, (adminId, street, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByNumberUnit(adminId, number, unit, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and number = %s and unit = %s;"
        cursor.execute(query, (adminId, number, unit, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByNumberZipCode(adminId, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and number = %s and zip_code = %s;"
        cursor.execute(query, (adminId, number, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByUnitZipCode(adminId, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (adminId, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByStreet(adminId, street, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and street = %s;"
        cursor.execute(query, (adminId, street, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByNumber(adminId, number, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and number = %s;"
        cursor.execute(query, (adminId, number, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByUnit(adminId, unit, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and unit = %s;"
        cursor.execute(query, (adminId, unit, ))
        result = cursor.fetchone()
        return result

    def getAdministratorAddressesByZipCode(adminId, zip_code, self):
        cursor = self.conn.cursor()
        query = "select administrator.adminId, street, number, unit, zip_code from account inner join administrator on account.aid = administrator.adminId natural inner join address where administrator.adminId = %s and zip_code = %s;"
        cursor.execute(query, (adminId, zip_code, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddress(sid, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s;"
        cursor.execute(query, (sid, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByStreetNumberUnitZipCode(sid, street, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s and number = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (sid, street, number, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByStreetNumberUnit(sid, street, number, unit, self):
        cursor = self.conn.cursor()
        query = "select supplier.supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s and number = %s and unit = %s;"
        cursor.execute(query, (sid, street, number, unit, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByStreetNumberZipCode(sid, street, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s and number = %s and zip_code = %s;"
        cursor.execute(query, (sid, street, number, zip_code, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByStreetZipCodeUnit(sid, street, zip_code, unit, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s and zip_code = %s and unit = %s;"
        cursor.execute(query, (sid, street, zip_code, unit, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByNumberUnitZipCode(sid, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and number = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (sid, number, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByStreetNumber(sid, street, number, self):
        cursor = self.conn.cursor()
        query = "select supplier.supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s and number = %s;"
        cursor.execute(query, (sid, street, number, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByStreetUnit(sid, street, unit, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s and unit = %s;"
        cursor.execute(query, (sid, street, unit, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByStreetZipCode(sid, street, zip_code, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s and zip_code = %s;"
        cursor.execute(query, (sid, street, zip_code, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByNumberUnit(sid, number, unit, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and number = %s and unit = %s;"
        cursor.execute(query, (sid, number, unit, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByNumberZipCode(sid, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and number = %s and zip_code = %s;"
        cursor.execute(query, (sid, number, zip_code, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByUnitZipCode(sid, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (sid, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByStreet(sid, street, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and street = %s;"
        cursor.execute(query, (sid, street, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByNumber(sid, number, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and number = %s;"
        cursor.execute(query, (sid, number, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByUnit(sid, unit, self):
        cursor = self.conn.cursor()
        query = "select supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and unit = %s;"
        cursor.execute(query, (sid, unit, ))
        result = cursor.fetchone()
        return result

    def getSupplierAddressesByZipCode(sid, zip_code, self):
        cursor = self.conn.cursor()
        query = "select supplier.supplier.sid, street, number, unit, zip_code from account inner join supplier on account.aid = supplier.sid natural inner join address where supplier.sid = %s and zip_code = %s;"
        cursor.execute(query, (sid, zip_code, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddress(rid, self):
        cursor = self.conn.cursor()
        query = "select supplier.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s;"
        cursor.execute(query, (rid, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByStreetNumberUnitZipCode(rid, street, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s and number = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (rid, street, number, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByStreetNumberUnit(rid, street, number, unit, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s and number = %s and unit = %s;"
        cursor.execute(query, (rid, street, number, unit, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByStreetNumberZipCode(rid, street, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s and number = %s and zip_code = %s;"
        cursor.execute(query, (rid, street, number, zip_code, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByStreetZipCodeUnit(rid, street, zip_code, unit, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s and zip_code = %s and unit = %s;"
        cursor.execute(query, (rid, street, zip_code, unit, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByNumberUnitZipCode(rid, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and number = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (rid, number, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByStreetNumber(rid, street, number, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s and number = %s;"
        cursor.execute(query, (rid, street, number, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByStreetUnit(rid, street, unit, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s and unit = %s;"
        cursor.execute(query, (rid, street, unit, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByStreetZipCode(rid, street, zip_code, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s and zip_code = %s;"
        cursor.execute(query, (rid, street, zip_code, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByNumberUnit(rid, number, unit, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and number = %s and unit = %s;"
        cursor.execute(query, (rid, number, unit, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByNumberZipCode(rid, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and number = %s and zip_code = %s;"
        cursor.execute(query, (rid, number, zip_code, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByUnitZipCode(rid, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (rid, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByStreet(rid, street, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and street = %s;"
        cursor.execute(query, (rid, street, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByNumber(rid, number, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and number = %s;"
        cursor.execute(query, (rid, number, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByUnit(rid, unit, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and unit = %s;"
        cursor.execute(query, (rid, unit, ))
        result = cursor.fetchone()
        return result

    def getRequesterAddressesByZipCode(rid, zip_code, self):
        cursor = self.conn.cursor()
        query = "select requester.rid, street, number, unit, zip_code from account inner join requester on account.aid = requester.rid natural inner join address where requester.rid = %s and zip_code = %s;"
        cursor.execute(query, (rid, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCity(cname, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s;"
        cursor.execute(query, (cname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressOnThisCityByStreetNumberUnitZipCode(cname, street, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and street = %s and number = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (cname, street, number, unit, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByStreetNumberUnit(cname, street, number, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and street = %s and number = %s and unit = %s;"
        cursor.execute(query, (cname, street, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByStreetNumberZipCode(cname, street, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and street = %s and number = %s and zip_code = %s;"
        cursor.execute(query, (cname, street, number, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByStreetZipCodeUnit(cname, street, zip_code, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and street = %s and zip_code = %s and unit = %s;"
        cursor.execute(query, (cname, street, zip_code, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByNumberUnitZipCode(cname, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and number = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (cname, number, unit, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByStreetNumber(cname, street, number, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and street = %s and number = %s;"
        cursor.execute(query, (cname, street, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByStreetUnit(cname, street, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and street = %s and unit = %s;"
        cursor.execute(query, (cname, street, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByStreetZipCode(cname, street, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and street = %s and zip_code = %s;"
        cursor.execute(query, (cname, street, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByNumberUnit(cname, number, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and number = %s and unit = %s;"
        cursor.execute(query, (cname, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByNumberZipCode(cname, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and number = %s and zip_code = %s;"
        cursor.execute(query, (cname, number, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByUnitZipCode(cname, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (cname, unit, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByStreet(cname, street, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and street = %s;"
        cursor.execute(query, (cname, street, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByNumber(cname, number, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and number = %s;"
        cursor.execute(query, (cname, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByUnit(cname, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and unit = %s;"
        cursor.execute(query, (cname, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisCityByZipCode(cname, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address where cname = %s and zip_code = %s;"
        cursor.execute(query, (cname, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegion(rname, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s;"
        cursor.execute(query, (rname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressOnThisRegionByStreetNumberUnitZipCode(rname, street, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and street = %s and number = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (rname, street, number, unit, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByStreetNumberUnit(rname, street, number, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and street = %s and number = %s and unit = %s;"
        cursor.execute(query, (rname, street, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByStreetNumberZipCode(rname, street, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and street = %s and number = %s and zip_code = %s;"
        cursor.execute(query, (rname, street, number, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByStreetZipCodeUnit(rname, street, zip_code, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and street = %s and zip_code = %s and unit = %s;"
        cursor.execute(query, (rname, street, zip_code, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByNumberUnitZipCode(rname, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and number = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (rname, number, unit, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByStreetNumber(rname, street, number, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and street = %s and number = %s;"
        cursor.execute(query, (rname, street, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByStreetUnit(rname, street, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and street = %s and unit = %s;"
        cursor.execute(query, (rname, street, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByStreetZipCode(rname, street, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and street = %s and zip_code = %s;"
        cursor.execute(query, (rname, street, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByNumberUnit(rname, number, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and number = %s and unit = %s;"
        cursor.execute(query, (rname, number, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByNumberZipCode(rname, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and number = %s and zip_code = %s;"
        cursor.execute(query, (rname, number, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByUnitZipCode(rname, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and unit = %s and zip_code = %s;"
        cursor.execute(query, (rname, unit, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByStreet(rname, street, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and street = %s;"
        cursor.execute(query, (rname, street, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByNumber(rname, number, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and number = %s;"
        cursor.execute(query, (rname, number, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByUnit(rname, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and unit = %s;"
        cursor.execute(query, (rname, unit, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressesOnThisRegionByZipCode(rname, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join city where rname = %s and zip_code = %s;"
        cursor.execute(query, (rname, zip_code, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardAddress(cid, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s"
        cursor.execute(query, (cid, ))
        result = cursor.fetchone()
        return result

    def getAddressOnThisCreditCardByStreetNumberUnitZipCode(cid, street, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and street = %s and number = %s and unit = %s and zip_code = %s"
        cursor.execute(query, (cid, street, number, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCreditCardByStreetNumberUnit(cid, street, number, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and street = %s and number = %s and unit = %s"
        cursor.execute(query, (cid, street, number, unit, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCreditCardByStreetNumberZipCode(cid, street, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and street = %s and number = %s and zip_code = %s"
        cursor.execute(query, (cid, street, number, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCreditCardByStreetZipCodeUnit(cid, street, zip_code, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and street = %s and zip_code = %s and unit = %s"
        cursor.execute(query, (cid, street, zip_code, unit, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCreditCardByNumberUnitZipCode(cid, number, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and number = %s and unit = %s and zip_code = %s"
        cursor.execute(query, (cid, number, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCreditCardByStreetNumber(cid, street, number, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and street = %s and number = %s"
        cursor.execute(query, (cid, street, number, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCreditCardByStreetUnit(cid, street, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and street = %s and unit = %s"
        cursor.execute(query, (cid, street, unit, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCreditCardByStreetZipCode(cid, street, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and street = %s and zip_code = %s"
        cursor.execute(query, (cid, street, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCreditCardByNumberUnit(cid, number, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and number = %s and unit = %s"
        cursor.execute(query, (cid, number, unit, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCreditCardByNumberZipCode(cid, number, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and number = %s and zip_code = %s"
        cursor.execute(query, (cid, number, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCreditCardByUnitZipCode(cid, unit, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and unit = %s and zip_code = %s"
        cursor.execute(query, (cid, unit, zip_code, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCreditCardByStreet(cid, street, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and street = %s;"
        cursor.execute(query, (cid, street, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCreditCardByNumber(cid, number, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and number = %s;"
        cursor.execute(query, (cid, number, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCreditCardByUnit(cid, unit, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and unit = %s;"
        cursor.execute(query, (cid, unit, ))
        result = cursor.fetchone()
        return result

    def getAddressesOnThisCreditCardByZipCode(cid, zip_code, self):
        cursor = self.conn.cursor()
        query = "select addId, street, number, unit, zip_code from address natural inner join credit_card where cid = %s and zip_code = %s;"
        cursor.execute(query, (cid, zip_code, ))
        result = cursor.fetchone()
        return result