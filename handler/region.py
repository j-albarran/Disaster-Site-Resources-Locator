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

class RegionHandler:

# =========================================================================== #
#                                 Builders                                    #
# =========================================================================== #

    def build_region_dict(self, row):
        result = {}
        result['rname'] = row[0]
        return result

    def build_region_attribute(self, rname):
        result = {}
        result['rname'] = rname
        return result

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

# ================ #
#      Regions     #
# ================ #

    # ============ #
    #    Updates   #
    # ============ #

    def addNewRegion(self, form):
        if len(form) != 1:
            return jsonify(Error = "Malformed post request"), 400
        else:
            rname = form['rname']
            if rname:
                dao = RegionDAO()
                regionName = dao.addNewRegion(rname)
                result = self.build_region_attribute(regionName)
                return jsonify(Region = result), 201
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400


    def deleteRegion(self, rname):
        dao = RegionDAO()
        if not dao.getRegionByName(rname):
            return jsonify(Error="Region not found."), 404
        else:
            dao.deleteRegion(rname)
            return jsonify(DeleteStatus="OK"), 200

    # ============ #
    #    Gets      #
    # ============ #

    def getAllRegions(self):
        dao = RegionDAO()
        regions_list = dao.getAllRegions()
        result_list = []
        for region in regions_list:
            result = self.build_region_dict(region)
            result_list.append(result)
        return jsonify(Regions=result_list)

    def getRegionByName(self, rname):
        dao = RegionDAO()
        row = dao.getRegionByName(rname)
        if not row:
            return jsonify(Error = "Region Not Found"), 404
        else:
            region = self.build_region_dict(row)
            return jsonify(Region = region)

    def searchRegions(self, args):
        rname = args.get("rname")
        dao = RegionDAO()
        regions_list = []
        if (len(args) == 1) and rname:
            regions_list = dao.getRegionsByName(rname)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in regions_list:
            result = self.build_region_dict(row)
            result_list.append(result)
        return jsonify(Regions=result_list)

# ================ #
#      Cities      #
# ================ #

    def getCityRegion(self, cname):

        daoCities = CityDAO()
        dao = RegionDAO()

        if not daoCities.getCityByName(cname):
            return jsonify(Error="City Not Found"), 404

        regions_list = dao.getCityRegion(cname)

        result_list = []
        for row in regions_list:
            result = self.build_region_dict(row)
            result_list.append(result)
        return jsonify(Regions = result_list)


# ================ #
#     Addresses    #
# ================ #

    def getRegionOfThisAddress(self, addId):

        daoAdd = AddressDAO()
        dao = RegionDAO()

        if not daoAdd.getAddressById(addId):
            return jsonify(Error = 'Address Not Found'), 404

        regions_list = dao.getRegionOfThisAddress(addId)
        result_list = []
        for row in regions_list:
            result = self.build_region_dict(row)
            result_list.append(result)
        return jsonify(Region = result_list)

# ================ #
#      Accounts    #
# ================ #

    def getAccountRegion(self, aid):

        daoAcc = AccountDAO()
        dao = RegionDAO()

        if not daoAcc.getAccountById(aid):
            return jsonify(Error = 'Account Not Found'), 404

        regions_list = dao.getAccountRegion(aid)
        result_list = []
        for row in regions_list:
            result = self.build_region_dict(row)
            result_list.append(result)
        return jsonify(Region = result_list)


# ================ #
#   Administrators #
# ================ #

    def getAdministratorRegion(self, adminId):

        daoAdmin = AdministratorDAO()
        dao = RegionDAO()

        if not daoAdmin.getAdministratorById(adminId):
            return jsonify(Error = 'Administrator Not Found'), 404

        regions_list = dao.getAdministratorRegion(adminId)
        result_list = []
        for row in regions_list:
            result = self.build_region_dict(row)
            result_list.append(result)
        return jsonify(Region = result_list)

# ================ #
#    Suppliers     #
# ================ #

    def getSupplierRegion(self, sid):

        daoSup = SupplierDAO()
        dao = RegionDAO()

        if not daoSup.getSupplierById(sid):
            return jsonify(Error = 'Supplier Not Found'), 404

        regions_list = dao.getSupplierRegion(sid)
        result_list = []

        for row in regions_list:
            result = self.build_region_dict(row)
            result_list.append(result)
        return jsonify(Region = result_list)

# ================ #
#    Requesters    #
# ================ #

    def getRequesterRegion(self, rid):

        daoReq = RequesterDAO()
        dao = RegionDAO()

        if not daoReq.getRequesterById(rid):
            return jsonify(Error = 'Requester Not Found'), 404

        regions_list = dao.getRequesterRegion(rid)
        result_list = []
        for row in regions_list:
            result = self.build_region_dict(row)
            result_list.append(result)
        return jsonify(Region = result_list)

# ================ #
#    Resources     #
# ================ #

    def getResourceRegion(self, rsid):

        daoRes = ResourceDAO()
        dao = RegionDAO()

        if not daoRes.getResourceById(rsid):
            return jsonify(Error = 'Resource Not Found'), 404

        regions_list = dao.getResourceRegion(rsid)

        result_list = []

        for row in regions_list:
            result = self.build_region_dict(row)
            result_list.append(result)
        return jsonify(Region = result_list)

# ======================== #
#    Resources Requested   #
# ======================== #

    def getResourceRequestedRegion(self, rrid):

        daoResRec = ResourceRequestedDAO()
        dao = RegionDAO()

        if not daoResRec.getResourceRequestedById(rrid):
            return jsonify(Error = 'Resource Not Found'), 404

        regions_list = dao.getResourceRequestedRegion(rrid)

        result_list = []

        for row in regions_list:
            result = self.build_region_dict(row)
            result_list.append(result)
        return jsonify(Region = result_list)