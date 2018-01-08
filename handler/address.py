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
        result['zip_code'] = row[4]
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
        zip_code = args.get('zip_code')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zip_code:
            addresses_list = dao.getAddressByStreetNumberUnitZipCode(street, number, unit, zip_code)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getAddressesByStreetNumberUnit(street, number, unit)
        elif(len(args) == 3) and street and number and zip_code:
            addresses_list = dao.getAddressesByStreetNumberZipCode(street, number, zip_code)
        elif(len(args) == 3) and street and zip_code and unit:
            addresses_list = dao.getAddressesByStreetZipCodeUnit(street, zip_code, unit)
        elif(len(args) == 3) and number and unit and zip_code:
            addresses_list = dao.getAddressesByNumberUnitZipCode(number, unit, zip_code)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getAddressesByStreetNumber(street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getAddressesByStreetUnit(street, unit)
        elif(len(args) == 2) and street and zip_code:
            addresses_list = dao.getAddressesByStreetZipCode(street, zip_code)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getAddressesByNumberUnit(number, unit)
        elif(len(args) == 2) and number and zip_code:
            addresses_list = dao.getAddressesByNumberZipCode(number, zip_code)
        elif(len(args) == 2) and unit and zip_code:
            addresses_list = dao.getAddressesByUnitZipCode(unit, zip_code)
        elif(len(args) == 1) and street:
            addresses_list = dao.getAddressesByStreet(street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getAddressesByNumber(number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getAddressesByUnit(unit)
        elif(len(args) == 1) and zip_code:
            addresses_list = dao.getAddressesByZipCode(zip_code)
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
            return jsonify(Error = 'Address Not Found'), 404

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
            return jsonify(Error = 'Address Not Found'), 404

        street = args.get('street')
        number = args.get('number')
        unit = args.get('unit')
        zip_code = args.get('zip_code')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zip_code:
            addresses_list = dao.getAccountAddressesByStreetNumberUnitZipCode(aid, street, number, unit, zip_code)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getAccountAddressesByStreetNumberUnit(aid, street, number, unit)
        elif(len(args) == 3) and street and number and zip_code:
            addresses_list = dao.getAccountAddressesByStreetNumberZipCode(aid, street, number, zip_code)
        elif(len(args) == 3) and street and zip_code and unit:
            addresses_list = dao.getAccountAddressesByStreetZipCodeUnit(aid, street, zip_code, unit)
        elif(len(args) == 3) and number and unit and zip_code:
            addresses_list = dao.getAccountAddressesByNumberUnitZipCode(aid, number, unit, zip_code)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getAccountAddressesByStreetNumber(aid, street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getAccountAddressesByStreetUnit(aid, street, unit)
        elif(len(args) == 2) and street and zip_code:
            addresses_list = dao.getAccountAddressesByStreetZipCode(aid, street, zip_code)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getAccountAddressesByNumberUnit(aid, number, unit)
        elif(len(args) == 2) and number and zip_code:
            addresses_list = dao.getAccountAddressesByNumberZipCode(aid, number, zip_code)
        elif(len(args) == 2) and unit and zip_code:
            addresses_list = dao.getAccountAddressesByUnitZipCode(aid, unit, zip_code)
        elif(len(args) == 1) and street:
            addresses_list = dao.getAccountAddressesByStreet(aid, street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getAccountAddressesByNumber(aid, number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getAccountAddressesByUnit(aid, unit)
        elif(len(args) == 1) and zip_code:
            addresses_list = dao.getAccountAddressesByZipCode(aid, zip_code)
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
            return jsonify(Error = 'Address Not Found'), 404

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
            return jsonify(Error = 'Address Not Found'), 404

        street = args.get('street')
        number = args.get('number')
        unit = args.get('unit')
        zip_code = args.get('zip_code')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zip_code:
            addresses_list = dao.getAdministratorAddressesByStreetNumberUnitZipCode(adminId, street, number, unit, zip_code)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getAdministratorAddressesByStreetNumberUnit(adminId, street, number, unit)
        elif(len(args) == 3) and street and number and zip_code:
            addresses_list = dao.getAdministratorAddressesByStreetNumberZipCode(adminId, street, number, zip_code)
        elif(len(args) == 3) and street and zip_code and unit:
            addresses_list = dao.getAdministratorAddressesByStreetZipCodeUnit(adminId, street, zip_code, unit)
        elif(len(args) == 3) and number and unit and zip_code:
            addresses_list = dao.getAdministratorAddressesByNumberUnitZipCode(adminId, number, unit, zip_code)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getAdministratorAddressesByStreetNumber(adminId, street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getAdministratorAddressesByStreetUnit(adminId, street, unit)
        elif(len(args) == 2) and street and zip_code:
            addresses_list = dao.getAdministratorAddressesByStreetZipCode(adminId, street, zip_code)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getAdministratorAddressesByNumberUnit(adminId, number, unit)
        elif(len(args) == 2) and number and zip_code:
            addresses_list = dao.getAdministratorAddressesByNumberZipCode(adminId, number, zip_code)
        elif(len(args) == 2) and unit and zip_code:
            addresses_list = dao.getAdministratorAddressesByUnitZipCode(adminId, unit, zip_code)
        elif(len(args) == 1) and street:
            addresses_list = dao.getAdministratorAddressesByStreet(adminId, street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getAdministratorAddressesByNumber(adminId, number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getAdministratorAddressesByUnit(adminId, unit)
        elif(len(args) == 1) and zip_code:
            addresses_list = dao.getAdministratorAddressesByZipCode(adminId, zip_code)
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
            return jsonify(Error = 'Address Not Found'), 404

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
            return jsonify(Error = 'Address Not Found'), 404

        street = args.get('street')
        number = args.get('number')
        unit = args.get('unit')
        zip_code = args.get('zip_code')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zip_code:
            addresses_list = dao.getSupplierAddressesByStreetNumberUnitZipCode(sid, street, number, unit, zip_code)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getSupplierAddressesByStreetNumberUnit(sid, street, number, unit)
        elif(len(args) == 3) and street and number and zip_code:
            addresses_list = dao.getSupplierAddressesByStreetNumberZipCode(sid, street, number, zip_code)
        elif(len(args) == 3) and street and zip_code and unit:
            addresses_list = dao.getSupplierAddressesByStreetZipCodeUnit(sid, street, zip_code, unit)
        elif(len(args) == 3) and number and unit and zip_code:
            addresses_list = dao.getSupplierAddressesByNumberUnitZipCode(sid, number, unit, zip_code)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getSupplierAddressesByStreetNumber(sid, street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getSupplierAddressesByStreetUnit(sid, street, unit)
        elif(len(args) == 2) and street and zip_code:
            addresses_list = dao.getSupplierAddressesByStreetZipCode(sid, street, zip_code)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getSupplierAddressesByNumberUnit(sid, number, unit)
        elif(len(args) == 2) and number and zip_code:
            addresses_list = dao.getSupplierAddressesByNumberZipCode(sid, number, zip_code)
        elif(len(args) == 2) and unit and zip_code:
            addresses_list = dao.getSupplierAddressesByUnitZipCode(sid, unit, zip_code)
        elif(len(args) == 1) and street:
            addresses_list = dao.getSupplierAddressesByStreet(sid, street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getSupplierAddressesByNumber(sid, number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getSupplierAddressesByUnit(sid, unit)
        elif(len(args) == 1) and zip_code:
            addresses_list = dao.getSupplierAddressesByZipCode(sid, zip_code)
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
            return jsonify(Error = 'Address Not Found'), 404

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
            return jsonify(Error = 'Address Not Found'), 404

        street = args.get('street')
        number = args.get('number')
        unit = args.get('unit')
        zip_code = args.get('zip_code')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zip_code:
            addresses_list = dao.getRequesterAddressesByStreetNumberUnitZipCode(rid, street, number, unit, zip_code)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getRequesterAddressesByStreetNumberUnit(rid, street, number, unit)
        elif(len(args) == 3) and street and number and zip_code:
            addresses_list = dao.getRequesterAddressesByStreetNumberZipCode(rid, street, number, zip_code)
        elif(len(args) == 3) and street and zip_code and unit:
            addresses_list = dao.getRequesterAddressesByStreetZipCodeUnit(rid, street, zip_code, unit)
        elif(len(args) == 3) and number and unit and zip_code:
            addresses_list = dao.getRequesterAddressesByNumberUnitZipCode(rid, number, unit, zip_code)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getRequesterAddressesByStreetNumber(rid, street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getRequesterAddressesByStreetUnit(rid, street, unit)
        elif(len(args) == 2) and street and zip_code:
            addresses_list = dao.getRequesterAddressesByStreetZipCode(rid, street, zip_code)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getRequesterAddressesByNumberUnit(rid, number, unit)
        elif(len(args) == 2) and number and zip_code:
            addresses_list = dao.getRequesterAddressesByNumberZipCode(rid, number, zip_code)
        elif(len(args) == 2) and unit and zip_code:
            addresses_list = dao.getRequesterAddressesByUnitZipCode(rid, unit, zip_code)
        elif(len(args) == 1) and street:
            addresses_list = dao.getRequesterAddressesByStreet(rid, street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getRequesterAddressesByNumber(rid, number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getRequesterAddressesByUnit(rid, unit)
        elif(len(args) == 1) and zip_code:
            addresses_list = dao.getRequesterAddressesByZipCode(rid, zip_code)
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
        zip_code = args.get('zip_code')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zip_code:
            addresses_list = dao.getAddressOnThisCityByStreetNumberUnitZipCode(cname, street, number, unit, zip_code)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getAddressesOnThisCityByStreetNumberUnit(cname, street, number, unit)
        elif(len(args) == 3) and street and number and zip_code:
            addresses_list = dao.getAddressesOnThisCityByStreetNumberZipCode(cname, street, number, zip_code)
        elif(len(args) == 3) and street and zip_code and unit:
            addresses_list = dao.getAddressesOnThisCityByStreetZipCodeUnit(cname, street, zip_code, unit)
        elif(len(args) == 3) and number and unit and zip_code:
            addresses_list = dao.getAddressesOnThisCityByNumberUnitZipCode(cname, number, unit, zip_code)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getAddressesOnThisCityByStreetNumber(cname, street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getAddressesOnThisCityByStreetUnit(cname, street, unit)
        elif(len(args) == 2) and street and zip_code:
            addresses_list = dao.getAddressesOnThisCityByStreetZipCode(cname, street, zip_code)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getAddressesOnThisCityByNumberUnit(cname, number, unit)
        elif(len(args) == 2) and number and zip_code:
            addresses_list = dao.getAddressesOnThisCityByNumberZipCode(cname, number, zip_code)
        elif(len(args) == 2) and unit and zip_code:
            addresses_list = dao.getAddressesOnThisCityByUnitZipCode(cname, unit, zip_code)
        elif(len(args) == 1) and street:
            addresses_list = dao.getAddressesOnThisCityByStreet(cname, street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getAddressesOnThisCityByNumber(cname, number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getAddressesOnThisCityByUnit(cname, unit)
        elif(len(args) == 1) and zip_code:
            addresses_list = dao.getAddressesOnThisCityByZipCode(cname, zip_code)
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
        zip_code = args.get('zip_code')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zip_code:
            addresses_list = dao.getAddressOnThisRegionByStreetNumberUnitZipCode(rname, street, number, unit, zip_code)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getAddressesOnThisRegionByStreetNumberUnit(rname, street, number, unit)
        elif(len(args) == 3) and street and number and zip_code:
            addresses_list = dao.getAddressesOnThisRegionByStreetNumberZipCode(rname, street, number, zip_code)
        elif(len(args) == 3) and street and zip_code and unit:
            addresses_list = dao.getAddressesOnThisRegionByStreetZipCodeUnit(rname, street, zip_code, unit)
        elif(len(args) == 3) and number and unit and zip_code:
            addresses_list = dao.getAddressesOnThisRegionByNumberUnitZipCode(rname, number, unit, zip_code)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getAddressesOnThisRegionByStreetNumber(rname, street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getAddressesOnThisRegionByStreetUnit(rname, street, unit)
        elif(len(args) == 2) and street and zip_code:
            addresses_list = dao.getAddressesOnThisRegionByStreetZipCode(rname, street, zip_code)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getAddressesOnThisRegionByNumberUnit(rname, number, unit)
        elif(len(args) == 2) and number and zip_code:
            addresses_list = dao.getAddressesOnThisRegionByNumberZipCode(rname, number, zip_code)
        elif(len(args) == 2) and unit and zip_code:
            addresses_list = dao.getAddressesOnThisRegionByUnitZipCode(rname, unit, zip_code)
        elif(len(args) == 1) and street:
            addresses_list = dao.getAddressesOnThisRegionByStreet(rname, street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getAddressesOnThisRegionByNumber(rname, number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getAddressesOnThisRegionByUnit(rname, unit)
        elif(len(args) == 1) and zip_code:
            addresses_list = dao.getAddressesOnThisRegionByZipCode(rname, zip_code)
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
        zip_code = args.get('zip_code')

        addresses_list = []

        if(len(args) == 4) and street and number and unit and zip_code:
            addresses_list = dao.getAddressOnThisCreditCardByStreetNumberUnitZipCode(cid, street, number, unit, zip_code)
        elif(len(args) == 3) and street and number and unit:
            addresses_list = dao.getAddressesOnThisCreditCardByStreetNumberUnit(cid, street, number, unit)
        elif(len(args) == 3) and street and number and zip_code:
            addresses_list = dao.getAddressesOnThisCreditCardByStreetNumberZipCode(cid, street, number, zip_code)
        elif(len(args) == 3) and street and zip_code and unit:
            addresses_list = dao.getAddressesOnThisCreditCardByStreetZipCodeUnit(cid, street, zip_code, unit)
        elif(len(args) == 3) and number and unit and zip_code:
            addresses_list = dao.getAddressesOnThisCreditCardByNumberUnitZipCode(cid, number, unit, zip_code)
        elif(len(args) == 2) and street and number:
            addresses_list = dao.getAddressesOnThisCreditCardByStreetNumber(cid, street, number)
        elif(len(args) == 2) and street and unit:
            addresses_list = dao.getAddressesOnThisCreditCardByStreetUnit(cid, street, unit)
        elif(len(args) == 2) and street and zip_code:
            addresses_list = dao.getAddressesOnThisCreditCardByStreetZipCode(cid, street, zip_code)
        elif(len(args) == 2) and number and unit:
            addresses_list = dao.getAddressesOnThisCreditCardByNumberUnit(cid, number, unit)
        elif(len(args) == 2) and number and zip_code:
            addresses_list = dao.getAddressesOnThisCreditCardByNumberZipCode(cid, number, zip_code)
        elif(len(args) == 2) and unit and zip_code:
            addresses_list = dao.getAddressesOnThisCreditCardByUnitZipCode(cid, unit, zip_code)
        elif(len(args) == 1) and street:
            addresses_list = dao.getAddressesOnThisCreditCardByStreet(cid, street)
        elif(len(args) == 1) and number:
            addresses_list = dao.getAddressesOnThisCreditCardByNumber(cid, number)
        elif(len(args) == 1) and unit:
            addresses_list = dao.getAddressesOnThisCreditCardByUnit(cid, unit)
        elif(len(args) == 1) and zip_code:
            addresses_list = dao.getAddressesOnThisCreditCardByZipCode(cid, zip_code)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in addresses_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list)