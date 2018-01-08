from flask import jsonify

from dao.administrator import AdministratorDAO
from dao.address import AddressDAO
from dao.city import CityDAO
from dao.region import RegionDAO

class AdministratorHandler:

# =========================================================================== #
#                                 Builder                                #
# =========================================================================== #


    def build_administrator_dict(self, row):
        result = {}
        result['adminId'] = row[0]
        result['afirst'] = row[1]
        result['alast'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        return result


# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

# ================ #
#  Administrators  #
# ================ #

    def getAllAdministrators(self):

        dao = AdministratorDAO()

        administrators_list = dao.getAllAdministrators()
        result_list = []

        for administrator in administrators_list:
            result = self.build_administrator_dict(administrator)
            result_list.append(result)
        return jsonify(Administrators=result_list)

    def getAdministratorById(self, adminId):

        dao = AdministratorDAO()

        row = dao.getAdministratorById(adminId)
        if not row:
            return jsonify(Error = "Administrator Not Found"), 404
        else:
            administrator = self.build_administrator_dict(row)
            return jsonify(Administrator = administrator)

    def searchAdministrators(self, args):

        dao = AdministratorDAO()

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        administrators_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            administrators_list = dao.getAdministratorsByAFirstALastEmailPhone(afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            administrators_list = dao.getAdministratorsByAFirstALastEmail(afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            administrators_list = dao.getAdministratorsByAFirstALastPhone(afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            administrators_list = dao.getAdministratorsByAFirstPhoneEmail(afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            administrators_list = dao.getAdministratorsByALastEmailPhone(alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            administrators_list = dao.getAdministratorsByAFirstALast(afirst, alast)
        elif(len(args) == 2) and afirst and email:
            administrators_list = dao.getAdministratorsByAFirstEmail(afirst, email)
        elif(len(args) == 2) and afirst and phone:
            administrators_list = dao.getAdministratorsByAFirstPhone(afirst, phone)
        elif(len(args) == 2) and alast and email:
            administrators_list = dao.getAdministratorsByALastEmail(alast, email)
        elif(len(args) == 2) and alast and phone:
            administrators_list = dao.getAdministratorsByALastPhone(alast, phone)
        elif(len(args) == 2) and email and phone:
            administrators_list = dao.getAdministratorsByEmailPhone(email, phone)
        elif(len(args) == 1) and afirst:
            administrators_list = dao.getAdministratorsByAFirst(afirst)
        elif(len(args) == 1) and alast:
            administrators_list = dao.getAdministratorsByALast(alast)
        elif(len(args) == 1) and email:
            administrators_list = dao.getAdministratorsByEmail(email)
        elif(len(args) == 1) and phone:
            administrators_list = dao.getAdministratorsByPhone(phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in administrators_list:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        return jsonify(Administrators = result_list)

    # ================ #
    #     Addresses    #
    # ================ #

    def getAdministratorsOnThisAddressID(self, addId):

        daoAd = AddressDAO()
        dao = AdministratorDAO()

        if not daoAd.getAddressById(addId):
            return jsonify(Error = 'Address Not Found'), 404

        administrators_list = dao.getAdministratorsWithThisAddressID(addId)
        result_list = []

        for row in administrators_list:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        return jsonify(Administrators = result_list)

    def searchAdministratorsOnThisAddressID(self, addId, args):

        daoAd = AddressDAO()
        dao = AdministratorDAO()

        if not daoAd.getAddressById(addId):
            return jsonify(Error = 'Address Not Found'), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        administrators_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            administrators_list = dao.getAdministratorsOnThisAddressIDByAfirstAlastEmailPhone(addId, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            administrators_list = dao.getAdministratorsOnThisAddressIDByAfirstAlastEmail(addId, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            administrators_list = dao.getAdministratorsOnThisAddressIDByAfirstAlastPhone(addId, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            administrators_list = dao.getAdministratorsOnThisAddressIDByAfirstPhoneEmail(addId, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            administrators_list = dao.getAdministratorsOnThisAddressIDByAlastEmailPhone(addId, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            administrators_list = dao.getAdministratorsOnThisAddressIDByAfirstAlast(addId, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            administrators_list = dao.getAdministratorsOnThisAddressIDByAfirstEmail(addId, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            administrators_list = dao.getAdministratorsOnThisAddressIDByAfirstPhone(addId, afirst, phone)
        elif(len(args) == 2) and alast and email:
            administrators_list = dao.getAdministratorsOnThisAddressIDByAlastEmail(addId, alast, email)
        elif(len(args) == 2) and alast and phone:
            administrators_list = dao.getAdministratorsOnThisAddressIDByAlastPhone(addId, alast, phone)
        elif(len(args) == 2) and email and phone:
            administrators_list = dao.getAdministratorsOnThisAddressIDByEmailPhone(addId, email, phone)
        elif(len(args) == 1) and afirst:
            administrators_list = dao.getAdministratorsOnThisAddressIDByAfirst(addId, afirst)
        elif(len(args) == 1) and alast:
            administrators_list = dao.getAdministratorsOnThisAddressIDByAlast(addId, alast)
        elif(len(args) == 1) and email:
            administrators_list = dao.getAdministratorsOnThisAddressIDByEmail(addId, email)
        elif(len(args) == 1) and phone:
            administrators_list = dao.getAdministratorsOnThisAddressIDByPhone(addId, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in administrators_list:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        return jsonify(Administrators = result_list)

    # ================ #
    #     Cities       #
    # ================ #

    def getAdministratorsOnThisCity(self, cname):

        daoCity = CityDAO()
        dao = AdministratorDAO()

        if not daoCity.getCityByName(cname):
            return jsonify(Error="City Not Found"), 404

        administrators_list = dao.getAdministratorsOnThisCity(cname)
        result_list = []

        for row in administrators_list:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        return jsonify(Administrators = result_list)

    def searchAdministratorsOnThisCity(self, cname, args):

        daoCity = CityDAO()
        dao = AdministratorDAO()

        if not daoCity.getCityByName(cname):
            return jsonify(Error = 'City Not Found'), 404

        afirst = args.get('afirst') #street
        alast = args.get('alast') #number
        email = args.get('email') #unit
        phone = args.get('phone') #zipcode

        administrators_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            administrators_list = dao.getAdministratorsOnThisCityAfirstAlastEmailPhone(cname, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            administrators_list = dao.getAdministratorsOnThisCityByAfirstAlastEmail(cname, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            administrators_list = dao.getAdministratorsOnThisCityByAfirstAlastPhone(cname, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            administrators_list = dao.getAdministratorsOnThisCityByAfirstPhoneEmail(cname, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            administrators_list = dao.getAdministratorsOnThisCityByAlastEmailPhone(cname, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            administrators_list = dao.getAdministratorsOnThisCityByAfirstAlast(cname, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            administrators_list = dao.getAdministratorsOnThisCityByAfirstEmail(cname, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            administrators_list = dao.getAdministratorsOnThisCityByAfirstPhone(cname, afirst, phone)
        elif(len(args) == 2) and alast and email:
            administrators_list = dao.getAdministratorsOnThisCityByAlastEmail(cname, alast, email)
        elif(len(args) == 2) and alast and phone:
            administrators_list = dao.getAdministratorsOnThisCityByAlastPhone(cname, alast, phone)
        elif(len(args) == 2) and email and phone:
            administrators_list = dao.getAdministratorsOnThisCityByEmailPhone(cname, email, phone)
        elif(len(args) == 1) and afirst:
            administrators_list = dao.getAdministratorsOnThisCityByAfirst(cname, afirst)
        elif(len(args) == 1) and alast:
            administrators_list = dao.getAdministratorsOnThisCityByAlast(cname, alast)
        elif(len(args) == 1) and email:
            administrators_list = dao.getAdministratorsOnThisCityByEmail(cname, email)
        elif(len(args) == 1) and phone:
            administrators_list = dao.getAdministratorsOnThisCityByPhone(cname, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in administrators_list:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        return jsonify(Administrators = result_list)

# ================ #
#     Regions      #
# ================ #

    def getAdministratorsOnThisRegion(self, rname):

        daoReg = RegionDAO()
        dao = AdministratorDAO()

        if not daoReg.getRegionByName(rname):
            return jsonify(Error="Region Not Found"), 404

        administrators_list = dao.getAdministratorsOnThisRegion(rname)
        result_list = []

        for row in administrators_list:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        return jsonify(Administrators = result_list)

    def searchAdministratorsOnThisRegion(self, rname, args):

        daoReg = RegionDAO()
        dao = AdministratorDAO()

        if not daoReg.getRegionByName(rname):
            return jsonify(Error = 'Region Not Found'), 404

        afirst = args.get('afirst') #street
        alast = args.get('alast') #number
        email = args.get('email') #unit
        phone = args.get('phone') #zipcode

        administrators_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            administrators_list = dao.getAdministratorsOnThisRegionAfirstAlastEmailPhone(rname, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            administrators_list = dao.getAdministratorsOnThisRegionByAfirstAlastEmail(rname, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            administrators_list = dao.getAdministratorsOnThisRegionByAfirstAlastPhone(rname, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            administrators_list = dao.getAdministratorsOnThisRegionByAfirstPhoneEmail(rname, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            administrators_list = dao.getAdministratorsOnThisRegionByAlastEmailPhone(rname, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            administrators_list = dao.getAdministratorsOnThisRegionByAfirstAlast(rname, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            administrators_list = dao.getAdministratorsOnThisRegionByAfirstEmail(rname, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            administrators_list = dao.getAdministratorsOnThisRegionByAfirstPhone(rname, afirst, phone)
        elif(len(args) == 2) and alast and email:
            administrators_list = dao.getAdministratorsOnThisRegionByAlastEmail(rname, alast, email)
        elif(len(args) == 2) and alast and phone:
            administrators_list = dao.getAdministratorsOnThisRegionByAlastPhone(rname, alast, phone)
        elif(len(args) == 2) and email and phone:
            administrators_list = dao.getAdministratorsOnThisRegionByEmailPhone(rname, email, phone)
        elif(len(args) == 1) and afirst:
            administrators_list = dao.getAdministratorsOnThisRegionByAfirst(rname, afirst)
        elif(len(args) == 1) and alast:
            administrators_list = dao.getAdministratorsOnThisRegionByAlast(rname, alast)
        elif(len(args) == 1) and email:
            administrators_list = dao.getAdministratorsOnThisRegionByEmail(rname, email)
        elif(len(args) == 1) and phone:
            administrators_list = dao.getAdministratorsOnThisRegionByPhone(rname, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in administrators_list:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        return jsonify(Administrators = result_list)