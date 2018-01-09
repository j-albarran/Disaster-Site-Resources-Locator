from flask import jsonify

from dao.address import AddressDAO
from dao.account import AccountDAO
from dao.requester import RequesterDAO
from dao.supplier import SupplierDAO
from dao.city import CityDAO
from dao.region import RegionDAO
from dao.administrator import AdministratorDAO

class AddressHandler:

# =========================================================================== #
#                                 Builders                                    #
# =========================================================================== #

    def build_address_dict(self, row):
        result = {}
        result['addId'] = row[0]
        result['street'] = row[1]
        result['number'] = row[2]
        result['unit'] = row[3]
        result['zipcode'] = row[4]
        return result

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

# ================ #
#    Addresses     #
# ================ #

    def getAllAddresses(self):

        dao = AddressDAO()

        addresses_list = dao.getAllAddresses()

        result_list = []
        for address in addresses_list:
            result = self.build_address_dict(address)
            result_list.append(result)
        return jsonify(Addresses=result_list)

    def getAddressById(self, addId):

        dao = AddressDAO()

        row = dao.getAddressById(addId)

        if not row:
            return jsonify(Error = "Address Not Found"), 404
        else:
            address = self.build_address_dict(row)
            return jsonify(Address = address)

    def searchAddresses(self, args):

        dao = AddressDAO()

        street = args.get('street')
        number = args.get('number')
        unit = args.get('unit')
        zipcode = args.get('zipcode')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zipcode:
            addresses_list = dao.getAddressByStreetNumberUnitZipCode(street, number, unit, zipcode)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getAddressesByStreetNumberUnit(street, number, unit)
        elif(len(args) == 3) and street and number and zipcode:
            addresses_list = dao.getAddressesByStreetNumberZipCode(street, number, zipcode)
        elif(len(args) == 3) and street and zipcode and unit:
            addresses_list = dao.getAddressesByStreetZipCodeUnit(street, zipcode, unit)
        elif(len(args) == 3) and number and unit and zipcode:
            addresses_list = dao.getAddressesByNumberUnitZipCode(number, unit, zipcode)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getAddressesByStreetNumber(street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getAddressesByStreetUnit(street, unit)
        elif(len(args) == 2) and street and zipcode:
            addresses_list = dao.getAddressesByStreetZipCode(street, zipcode)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getAddressesByNumberUnit(number, unit)
        elif(len(args) == 2) and number and zipcode:
            addresses_list = dao.getAddressesByNumberZipCode(number, zipcode)
        elif(len(args) == 2) and unit and zipcode:
            addresses_list = dao.getAddressesByUnitZipCode(unit, zipcode)
        elif(len(args) == 1) and street:
            addresses_list = dao.getAddressesByStreet(street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getAddressesByNumber(number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getAddressesByUnit(unit)
        elif(len(args) == 1) and zipcode:
            addresses_list = dao.getAddressesByZipCode(zipcode)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in addresses_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list)

# ================ #
#    Accounts      #
# ================ #

    def getAccountAddress(self, aid):

        daoAcc = AccountDAO()
        dao = AddressDAO()

        if not daoAcc.getAccountById(aid):
            return jsonify(Error = 'Account Not Found'), 404

        address_list = dao.getAccountAddress(aid)
        results_list = []
        for row in address_list:
            result = self.build_address_dict(row)
            results_list.append(result)
        return jsonify(Address = results_list)

    def searchAccountAddress(self, aid, args):

        daoAcc = AccountDAO()
        dao = AddressDAO()

        if not daoAcc.getAccountById(aid):
            return jsonify(Error = 'Account Not Found'), 404

        street = args.get('street')
        number = args.get('number')
        unit = args.get('unit')
        zipcode = args.get('zipcode')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zipcode:
            addresses_list = dao.getAccountAddressesByStreetNumberUnitZipCode(aid, street, number, unit, zipcode)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getAccountAddressesByStreetNumberUnit(aid, street, number, unit)
        elif(len(args) == 3) and street and number and zipcode:
            addresses_list = dao.getAccountAddressesByStreetNumberZipCode(aid, street, number, zipcode)
        elif(len(args) == 3) and street and zipcode and unit:
            addresses_list = dao.getAccountAddressesByStreetZipCodeUnit(aid, street, zipcode, unit)
        elif(len(args) == 3) and number and unit and zipcode:
            addresses_list = dao.getAccountAddressesByNumberUnitZipCode(aid, number, unit, zipcode)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getAccountAddressesByStreetNumber(aid, street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getAccountAddressesByStreetUnit(aid, street, unit)
        elif(len(args) == 2) and street and zipcode:
            addresses_list = dao.getAccountAddressesByStreetZipCode(aid, street, zipcode)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getAccountAddressesByNumberUnit(aid, number, unit)
        elif(len(args) == 2) and number and zipcode:
            addresses_list = dao.getAccountAddressesByNumberZipCode(aid, number, zipcode)
        elif(len(args) == 2) and unit and zipcode:
            addresses_list = dao.getAccountAddressesByUnitZipCode(aid, unit, zipcode)
        elif(len(args) == 1) and street:
            addresses_list = dao.getAccountAddressesByStreet(aid, street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getAccountAddressesByNumber(aid, number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getAccountAddressesByUnit(aid, unit)
        elif(len(args) == 1) and zipcode:
            addresses_list = dao.getAccountAddressesByZipCode(aid, zipcode)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in addresses_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list)

    # ================ #
    #  Administrators  #
    # ================ #
    def getAdministratorAddress(self, adminId):

        daoAdmin = AdministratorDAO()
        dao = AddressDAO()

        if not daoAdmin.getAdministratorById(adminId):
            return jsonify(Error = 'Administrator Not Found'), 404

        address_list = dao.getAdministratorAddress(adminId)
        results_list = []
        for row in address_list:
            result = self.build_address_dict(row)
            results_list.append(result)
        return jsonify(Address = results_list)

    def searchAdministratorAddress(self, adminId, args):

        daoAdmin = AdministratorDAO()
        dao = AddressDAO()

        if not daoAdmin.getAdministratorById(adminId):
            return jsonify(Error = 'Administrator Not Found'), 404

        street = args.get('street')
        number = args.get('number')
        unit = args.get('unit')
        zipcode = args.get('zipcode')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zipcode:
            addresses_list = dao.getAdministratorAddressesByStreetNumberUnitZipCode(adminId, street, number, unit, zipcode)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getAdministratorAddressesByStreetNumberUnit(adminId, street, number, unit)
        elif(len(args) == 3) and street and number and zipcode:
            addresses_list = dao.getAdministratorAddressesByStreetNumberZipCode(adminId, street, number, zipcode)
        elif(len(args) == 3) and street and zipcode and unit:
            addresses_list = dao.getAdministratorAddressesByStreetZipCodeUnit(adminId, street, zipcode, unit)
        elif(len(args) == 3) and number and unit and zipcode:
            addresses_list = dao.getAdministratorAddressesByNumberUnitZipCode(adminId, number, unit, zipcode)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getAdministratorAddressesByStreetNumber(adminId, street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getAdministratorAddressesByStreetUnit(adminId, street, unit)
        elif(len(args) == 2) and street and zipcode:
            addresses_list = dao.getAdministratorAddressesByStreetZipCode(adminId, street, zipcode)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getAdministratorAddressesByNumberUnit(adminId, number, unit)
        elif(len(args) == 2) and number and zipcode:
            addresses_list = dao.getAdministratorAddressesByNumberZipCode(adminId, number, zipcode)
        elif(len(args) == 2) and unit and zipcode:
            addresses_list = dao.getAdministratorAddressesByUnitZipCode(adminId, unit, zipcode)
        elif(len(args) == 1) and street:
            addresses_list = dao.getAdministratorAddressesByStreet(adminId, street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getAdministratorAddressesByNumber(adminId, number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getAdministratorAddressesByUnit(adminId, unit)
        elif(len(args) == 1) and zipcode:
            addresses_list = dao.getAdministratorAddressesByZipCode(adminId, zipcode)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in addresses_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list)

# ================ #
#    Suppliers     #
# ================ #

    def getSupplierAddress(self, sid):

        daoSup = SupplierDAO()
        dao = AddressDAO()

        if not daoSup.getSupplierById(sid):
            return jsonify(Error = 'Supplier Not Found'), 404

        address_list = dao.getSupplierAddress(sid)

        results_list = []

        for row in address_list:
            result = self.build_address_dict(row)
            results_list.append(result)
        return jsonify(Address = results_list)

    def searchSupplierAddress(self, sid, args):

        daoSup = SupplierDAO()
        dao = AddressDAO()

        if not daoSup.getSupplierById(sid):
            return jsonify(Error = 'Supplier Not Found'), 404

        street = args.get('street')
        number = args.get('number')
        unit = args.get('unit')
        zipcode = args.get('zipcode')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zipcode:
            addresses_list = dao.getSupplierAddressesByStreetNumberUnitZipCode(sid, street, number, unit, zipcode)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getSupplierAddressesByStreetNumberUnit(sid, street, number, unit)
        elif(len(args) == 3) and street and number and zipcode:
            addresses_list = dao.getSupplierAddressesByStreetNumberZipCode(sid, street, number, zipcode)
        elif(len(args) == 3) and street and zipcode and unit:
            addresses_list = dao.getSupplierAddressesByStreetZipCodeUnit(sid, street, zipcode, unit)
        elif(len(args) == 3) and number and unit and zipcode:
            addresses_list = dao.getSupplierAddressesByNumberUnitZipCode(sid, number, unit, zipcode)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getSupplierAddressesByStreetNumber(sid, street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getSupplierAddressesByStreetUnit(sid, street, unit)
        elif(len(args) == 2) and street and zipcode:
            addresses_list = dao.getSupplierAddressesByStreetZipCode(sid, street, zipcode)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getSupplierAddressesByNumberUnit(sid, number, unit)
        elif(len(args) == 2) and number and zipcode:
            addresses_list = dao.getSupplierAddressesByNumberZipCode(sid, number, zipcode)
        elif(len(args) == 2) and unit and zipcode:
            addresses_list = dao.getSupplierAddressesByUnitZipCode(sid, unit, zipcode)
        elif(len(args) == 1) and street:
            addresses_list = dao.getSupplierAddressesByStreet(sid, street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getSupplierAddressesByNumber(sid, number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getSupplierAddressesByUnit(sid, unit)
        elif(len(args) == 1) and zipcode:
            addresses_list = dao.getSupplierAddressesByZipCode(sid, zipcode)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in addresses_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list)

# ================ #
#    Requesters    #
# ================ #

    def getRequesterAddress(self, rid):

        daoReq = RequesterDAO()
        dao = AddressDAO()

        if not daoReq.getRequesterById(rid):
            return jsonify(Error = 'Requester Not Found'), 404

        address_list = dao.getRequesterAddress(rid)

        results_list = []
        for row in address_list:
            result = self.build_address_dict(row)
            results_list.append(result)
        return jsonify(Address = results_list)

    def searchRequesterAddress(self, rid, args):

        daoReq = RequesterDAO()
        dao = AddressDAO()

        if not daoReq.getRequesterById(rid):
            return jsonify(Error = 'Requester Not Found'), 404

        street = args.get('street')
        number = args.get('number')
        unit = args.get('unit')
        zipcode = args.get('zipcode')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zipcode:
            addresses_list = dao.getRequesterAddressesByStreetNumberUnitZipCode(rid, street, number, unit, zipcode)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getRequesterAddressesByStreetNumberUnit(rid, street, number, unit)
        elif(len(args) == 3) and street and number and zipcode:
            addresses_list = dao.getRequesterAddressesByStreetNumberZipCode(rid, street, number, zipcode)
        elif(len(args) == 3) and street and zipcode and unit:
            addresses_list = dao.getRequesterAddressesByStreetZipCodeUnit(rid, street, zipcode, unit)
        elif(len(args) == 3) and number and unit and zipcode:
            addresses_list = dao.getRequesterAddressesByNumberUnitZipCode(rid, number, unit, zipcode)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getRequesterAddressesByStreetNumber(rid, street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getRequesterAddressesByStreetUnit(rid, street, unit)
        elif(len(args) == 2) and street and zipcode:
            addresses_list = dao.getRequesterAddressesByStreetZipCode(rid, street, zipcode)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getRequesterAddressesByNumberUnit(rid, number, unit)
        elif(len(args) == 2) and number and zipcode:
            addresses_list = dao.getRequesterAddressesByNumberZipCode(rid, number, zipcode)
        elif(len(args) == 2) and unit and zipcode:
            addresses_list = dao.getRequesterAddressesByUnitZipCode(rid, unit, zipcode)
        elif(len(args) == 1) and street:
            addresses_list = dao.getRequesterAddressesByStreet(rid, street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getRequesterAddressesByNumber(rid, number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getRequesterAddressesByUnit(rid, unit)
        elif(len(args) == 1) and zipcode:
            addresses_list = dao.getRequesterAddressesByZipCode(rid, zipcode)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in addresses_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list)


# ================ #
#     Cities       #
# ================ #

    def getAddressesOnThisCity(self, cname):

        daoCities = CityDAO()
        dao = AddressDAO()

        if not daoCities.getCityByName(cname):
            return jsonify(Error="City Not Found"), 404

        addresses_list = dao.getAddressesOnThisCity(cname)
        result_list = []
        for row in addresses_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list)

    def searchAddressesOnThisCity(self, cname, args):

        daoCities = CityDAO()
        dao = AddressDAO()

        if not daoCities.getCityByName(cname):
            return jsonify(Error="City Not Found"), 404

        street = args.get('street')
        number = args.get('number')
        unit = args.get('unit')
        zipcode = args.get('zipcode')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zipcode:
            addresses_list = dao.getAddressOnThisCityByStreetNumberUnitZipCode(cname, street, number, unit, zipcode)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getAddressesOnThisCityByStreetNumberUnit(cname, street, number, unit)
        elif(len(args) == 3) and street and number and zipcode:
            addresses_list = dao.getAddressesOnThisCityByStreetNumberZipCode(cname, street, number, zipcode)
        elif(len(args) == 3) and street and zipcode and unit:
            addresses_list = dao.getAddressesOnThisCityByStreetZipCodeUnit(cname, street, zipcode, unit)
        elif(len(args) == 3) and number and unit and zipcode:
            addresses_list = dao.getAddressesOnThisCityByNumberUnitZipCode(cname, number, unit, zipcode)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getAddressesOnThisCityByStreetNumber(cname, street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getAddressesOnThisCityByStreetUnit(cname, street, unit)
        elif(len(args) == 2) and street and zipcode:
            addresses_list = dao.getAddressesOnThisCityByStreetZipCode(cname, street, zipcode)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getAddressesOnThisCityByNumberUnit(cname, number, unit)
        elif(len(args) == 2) and number and zipcode:
            addresses_list = dao.getAddressesOnThisCityByNumberZipCode(cname, number, zipcode)
        elif(len(args) == 2) and unit and zipcode:
            addresses_list = dao.getAddressesOnThisCityByUnitZipCode(cname, unit, zipcode)
        elif(len(args) == 1) and street:
            addresses_list = dao.getAddressesOnThisCityByStreet(cname, street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getAddressesOnThisCityByNumber(cname, number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getAddressesOnThisCityByUnit(cname, unit)
        elif(len(args) == 1) and zipcode:
            addresses_list = dao.getAddressesOnThisCityByZipCode(cname, zipcode)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in addresses_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list)

# ================ #
#     Regions      #
# ================ #

    def getAddressesOnThisRegion(self, rname):

        daoReg = RegionDAO()
        dao = AddressDAO()

        if not daoReg.getRegionByName(rname):
            return jsonify(Error="Region Not Found"), 404

        addresses_list = dao.getAddressesOnThisRegion(rname)
        result_list = []
        for row in addresses_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list)

    def searchAddressesOnThisRegion(self, rname, args):

        daoReg = RegionDAO()
        dao = AddressDAO()

        if not daoReg.getRegionByName(rname):
            return jsonify(Error="Region Not Found"), 404

        street = args.get('street')
        number = args.get('number')
        unit = args.get('unit')
        zipcode = args.get('zipcode')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zipcode:
            addresses_list = dao.getAddressOnThisRegionByStreetNumberUnitZipCode(rname, street, number, unit, zipcode)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getAddressesOnThisRegionByStreetNumberUnit(rname, street, number, unit)
        elif(len(args) == 3) and street and number and zipcode:
            addresses_list = dao.getAddressesOnThisRegionByStreetNumberZipCode(rname, street, number, zipcode)
        elif(len(args) == 3) and street and zipcode and unit:
            addresses_list = dao.getAddressesOnThisRegionByStreetZipCodeUnit(rname, street, zipcode, unit)
        elif(len(args) == 3) and number and unit and zipcode:
            addresses_list = dao.getAddressesOnThisRegionByNumberUnitZipCode(rname, number, unit, zipcode)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getAddressesOnThisRegionByStreetNumber(rname, street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getAddressesOnThisRegionByStreetUnit(rname, street, unit)
        elif(len(args) == 2) and street and zipcode:
            addresses_list = dao.getAddressesOnThisRegionByStreetZipCode(rname, street, zipcode)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getAddressesOnThisRegionByNumberUnit(rname, number, unit)
        elif(len(args) == 2) and number and zipcode:
            addresses_list = dao.getAddressesOnThisRegionByNumberZipCode(rname, number, zipcode)
        elif(len(args) == 2) and unit and zipcode:
            addresses_list = dao.getAddressesOnThisRegionByUnitZipCode(rname, unit, zipcode)
        elif(len(args) == 1) and street:
            addresses_list = dao.getAddressesOnThisRegionByStreet(rname, street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getAddressesOnThisRegionByNumber(rname, number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getAddressesOnThisRegionByUnit(rname, unit)
        elif(len(args) == 1) and zipcode:
            addresses_list = dao.getAddressesOnThisRegionByZipCode(rname, zipcode)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in addresses_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list)

# ================ #
#   Credit Cards   #
# ================ #


    def getCreditCardAddress(self, cid):

      #  daoCred = CreditCardsDAO()
        dao = AddressDAO()

       # if not daoCred.getCreditCardById(cid):
       #     return jsonify(Error="Credit Card Not Found"), 404

        addresses_list = dao.getCreditCardAddress(cid)

        result_list = []
        for row in addresses_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list)

    def searchCreditCardAddress(self, cid, args):

      #  daoCred = CreditCardsDAO()
        dao = AddressDAO()

    #    if not daoCred.getCreditCardById(cid):
    #        return jsonify(Error="Credit Card Not Found"), 404

        street = args.get('street')
        number = args.get('number')
        unit = args.get('unit')
        zipcode = args.get('zipcode')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zipcode:
            addresses_list = dao.getAddressOnThisCreditCardByStreetNumberUnitZipCode(cid, street, number, unit, zipcode)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getAddressesOnThisCreditCardByStreetNumberUnit(cid, street, number, unit)
        elif(len(args) == 3) and street and number and zipcode:
            addresses_list = dao.getAddressesOnThisCreditCardByStreetNumberZipCode(cid, street, number, zipcode)
        elif(len(args) == 3) and street and zipcode and unit:
            addresses_list = dao.getAddressesOnThisCreditCardByStreetZipCodeUnit(cid, street, zipcode, unit)
        elif(len(args) == 3) and number and unit and zipcode:
            addresses_list = dao.getAddressesOnThisCreditCardByNumberUnitZipCode(cid, number, unit, zipcode)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getAddressesOnThisCreditCardByStreetNumber(cid, street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getAddressesOnThisCreditCardByStreetUnit(cid, street, unit)
        elif(len(args) == 2) and street and zipcode:
            addresses_list = dao.getAddressesOnThisCreditCardByStreetZipCode(cid, street, zipcode)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getAddressesOnThisCreditCardByNumberUnit(cid, number, unit)
        elif(len(args) == 2) and number and zipcode:
            addresses_list = dao.getAddressesOnThisCreditCardByNumberZipCode(cid, number, zipcode)
        elif(len(args) == 2) and unit and zipcode:
            addresses_list = dao.getAddressesOnThisCreditCardByUnitZipCode(cid, unit, zipcode)
        elif(len(args) == 1) and street:
            addresses_list = dao.getAddressesOnThisCreditCardByStreet(cid, street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getAddressesOnThisCreditCardByNumber(cid, number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getAddressesOnThisCreditCardByUnit(cid, unit)
        elif(len(args) == 1) and zipcode:
            addresses_list = dao.getAddressesOnThisCreditCardByZipCode(cid, zipcode)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in addresses_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list)