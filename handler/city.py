from flask import jsonify

from dao.region import RegionDAO
from dao.city import CityDAO
from dao.account import AccountDAO
from dao.administrator import AdministratorDAO
from dao.requester import RequesterDAO
from dao.supplier import SupplierDAO
from dao.resource import ResourceDAO
from dao.resource_requested import ResourceRequestedDAO
from dao.address import AddressDAO

class CityHandler:

# =========================================================================== #
#                                 Builders                                    #
# =========================================================================== #

    def build_city_dict(self, row):
        result = {}
        result['cname'] = row[0]
        return result

    def build_city_attributes(self, cname):
        result = {}
        result['cname'] = cname
        return result


# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

# ================ #
#      Cities      #
# ================ #

    # ============ #
    #    Updates   #
    # ============ #

    def addNewCity(self, form):
        if len(form) != 2:
            return jsonify(Error = "Malformed post request"), 400
        else:
            cname = form['cname']
            rname = form['rname']
            if cname and rname:
                dao = CityDAO()
                cityName = dao.addNewCity(cname, rname)
                result = self.build_city_attributes(cityName)
                return jsonify(City = result), 201
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400


    def updateCity(self, cname, form):
        dao = CityDAO()
        if not dao.getCityByName(cname):
            return jsonify(Error = "City not found"), 404
        else:
            if len(form) != 1:
                return jsonify(Error = "Malformed update request"), 400
            rname = form['rname']
            if cname and rname:
                dao.updateCity(cname, rname)
                result = self.build_city_attributes(cname)
                return jsonify(City = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteCity(self, cname):
        dao = CityDAO()
        if not dao.getCityByName(cname):
            return jsonify(Error="City not found."), 404
        else:
            dao.deleteCity(cname)
            return jsonify(DeleteStatus="OK"), 200

    # ============ #
    #    Gets      #
    # ============ #

    def getAllCities(self):
        dao = CityDAO()
        cities_list = dao.getAllCities()
        result_list = []
        for city in cities_list:
            result = self.build_city_dict(city)
            result_list.append(result)
        return jsonify(Cities=result_list)

    def getCityByName(self, cname):
        dao = CityDAO()
        row = dao.getCityByName(cname)
        if not row:
            return jsonify(Error = "City Not Found"), 404
        else:
            city = self.build_city_dict(row)
            return jsonify(City = city)

    def searchCities(self, args):
        cname = args.get("cname")
        dao = CityDAO()
        cities_list = []
        if (len(args) == 1) and cname:
            cities_list = dao.getCitiesByName(cname)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in cities_list:
            result = self.build_city_dict(row)
            result_list.append(result)
        return jsonify(Cities=result_list)

# ================ #
#      Regions     #
# ================ #

    def getCitiesOnThisRegion(self, rname):

        daoReg = RegionDAO()
        dao = CityDAO()

        if not daoReg.getRegionByName(rname):
            return jsonify(Error = 'Region Not Found'), 404

        cities_list = dao.getCitiesOnThisRegion(rname)
        result_list = []
        for row in cities_list:
            result = self.build_city_dict(row)
            result_list.append(result)
        return jsonify(Cities = cities_list)

# ================ #
#     Addresses    #
# ================ #

    def getCityOfThisAddress(self, addId):

        daoAdd = AddressDAO()
        dao = CityDAO()

        if not daoAdd.getAddressById(addId):
            return jsonify(Error = 'Address Not Found'), 404

        cities_list = dao.getCityOfThisAddress(addId)
        result_list = []
        for row in cities_list:
            result = self.build_city_dict(row)
            result_list.append(result)
        return jsonify(City = result_list)

# ================ #
#      Accounts    #
# ================ #

    def getAccountCity(self, aid):

        daoAcc = AccountDAO()
        dao = CityDAO()

        if not daoAcc.getAccountById(aid):
            return jsonify(Error = 'Account Not Found'), 404

        cities_list = dao.getAccountCity(aid)
        result_list = []
        for row in cities_list:
            result = self.build_city_dict(row)
            result_list.append(result)
        return jsonify(City = result_list)

# ================ #
#   Administrators #
# ================ #

    def getAdministratorCity(self, adminId):

        daoAdmin = AdministratorDAO()
        dao = CityDAO()

        if not daoAdmin.getAdministratorById(adminId):
            return jsonify(Error = 'Administrator Not Found'), 404

        cities_list = dao.getAdministratorCity(adminId)
        result_list = []
        for row in cities_list:
            result = self.build_city_dict(row)
            result_list.append(result)
        return jsonify(City = result_list)


# ================ #
#    Suppliers     #
# ================ #

    def getSupplierCity(self, sid):

        daoSup = SupplierDAO()
        dao = CityDAO()

        if not daoSup.getSupplierById(sid):
            return jsonify(Error = 'Supplier Not Found'), 404

        cities_list = dao.getSupplierCity(sid)
        result_list = []
        for row in cities_list:
            result = self.build_city_dict(row)
            result_list.append(result)
        return jsonify(City = result_list)

# ================ #
#    Requesters    #
# ================ #

    def getRequesterCity(self, rid):

        daoReq = RequesterDAO()
        dao = CityDAO()

        if not daoReq.getRequesterById(rid):
            return jsonify(Error = 'Requester Not Found'), 404

        cities_list = dao.getRequesterCity(rid)
        result_list = []
        for row in cities_list:
            result = self.build_city_dict(row)
            result_list.append(result)
        return jsonify(City = result_list)