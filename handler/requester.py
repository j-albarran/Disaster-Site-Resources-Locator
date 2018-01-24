from flask import jsonify

from dao.requester import RequesterDAO
from dao.address import AddressDAO
from dao.city import CityDAO
from dao.region import RegionDAO
from dao.resource import ResourceDAO
from dao.resource_requested import ResourceRequestedDAO
from dao.category import CategoryDAO
from dao.transaction import TransactionDAO
from dao.credit_card import CreditCardDAO
from dao.payment import PaymentDAO
from dao.order import OrderDAO

class RequesterHandler:

# =========================================================================== #
#                                 Builders                                    #
# =========================================================================== #


    def build_requester_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['afirst'] = row[1]
        result['alast'] = row[2]
        result['email'] = row[3]
        result['phone'] = row[4]
        return result

    def build_requester_attributes(self, rid, afirst, alast, email, phone):
        result = {}
        result['rid'] = rid
        result['afirst'] = afirst
        result['alast'] = alast
        result['email'] = email
        result['phone'] = phone
        return result

# =========================================================================== #
#                                 Methods                                     #
# =========================================================================== #

    # ============ #
    #    Updates   #
    # ============ #

    def addNewRequester(self, form):
        if len(form) != 4:
            return jsonify(Error = "Malformed post request"), 400
        else:

            afirst = form['afirst']
            alast = form['alast']
            email = form['email']
            phone = form['phone']

            if afirst and alast and email and phone:
                dao = RequesterDAO()
                rid = dao.addNewRequester(afirst, alast, email, phone)
                result = self.build_requester_attributes(rid, afirst, alast, email, phone)
                return jsonify(Requester = result), 201
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400


    def updateRequester(self, rid, form):
        dao = RequesterDAO()
        if not dao.getRequesterById(rid):
            return jsonify(Error = "Requester not found"), 404
        else:
            if len(form) != 4:
                return jsonify(Error = "Malformed update request"), 400

            afirst = form['afirst']
            alast = form['alast']
            email = form['email']
            phone = form['phone']

            if afirst and alast and email and phone:
                dao.updateRequester(rid, afirst, alast, email, phone)
                result = self.build_requester_attributes(rid, afirst, alast, email, phone)
                return jsonify(Requester = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    def deleteRequester(self, rid):
        dao = RequesterDAO()
        if not dao.getRequesterById(rid):
            return jsonify(Error="Requester not found."), 404
        else:
            dao.deleteRequester(rid)
            return jsonify(DeleteStatus="OK"), 200
        
# ================ #
#    Requesters    #
# ================ #

    def getAllRequesters(self):
        dao = RequesterDAO()
        requesters_list = dao.getAllRequesters()
        result_list = []
        for requester in requesters_list:
            result = self.build_requester_dict(requester)
            result_list.append(result)
        return jsonify(Requesters=result_list)

    def getRequesterById(self, rid):
        dao = RequesterDAO()
        row = dao.getRequesterById(rid)
        if not row:
            return jsonify(Error = "Requester Not Found"), 404
        else:
            requester = self.build_requester_dict(row)
            return jsonify(Requester = requester)

    def searchRequesters(self, args):

        dao = RequesterDAO()

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        requesters_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            requesters_list = dao.getRequestersByAFirstALastEmailPhone(afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            requesters_list = dao.getRequestersByAFirstALastEmail(afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            requesters_list = dao.getRequestersByAFirstALastPhone(afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            requesters_list = dao.getRequestersByAFirstPhoneEmail(afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            requesters_list = dao.getRequestersByALastEmailPhone(alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            requesters_list = dao.getRequestersByAFirstALast(afirst, alast)
        elif(len(args) == 2) and afirst and email:
            requesters_list = dao.getRequestersByAFirstEmail(afirst, email)
        elif(len(args) == 2) and afirst and phone:
            requesters_list = dao.getRequestersByAFirstPhone(afirst, phone)
        elif(len(args) == 2) and alast and email:
            requesters_list = dao.getRequestersByALastEmail(alast, email)
        elif(len(args) == 2) and alast and phone:
            requesters_list = dao.getRequestersByALastPhone(alast, phone)
        elif(len(args) == 2) and email and phone:
            requesters_list = dao.getRequestersByEmailPhone(email, phone)
        elif(len(args) == 1) and afirst:
            requesters_list = dao.getRequestersByAFirst(afirst)
        elif(len(args) == 1) and alast:
            requesters_list = dao.getRequestersByALast(alast)
        elif(len(args) == 1) and email:
            requesters_list = dao.getRequestersByEmail(email)
        elif(len(args) == 1) and phone:
            requesters_list = dao.getRequestersByPhone(phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

# ================ #
#     Addresses    #
# ================ #

    def getRequestersOnThisAddressID(self, addId):

        dao = RequesterDAO()
        daoAdd = AddressDAO()

        if not daoAdd.getAddressById(addId):
            return jsonify(Error = 'Address Not Found'), 404

        requesters_list = dao.getRequestersWithThisAddressID(addId)
        result_list = []

        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

    def searchRequestersOnThisAddressID(self, addId, args):

        dao = RequesterDAO()
        daoAdd = AddressDAO()

        if not daoAdd.getAddressById(addId):
            return jsonify(Error = 'Address Not Found'), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        requesters_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            requesters_list = dao.getRequestersOnThisAddressIDByAfirstAlastEmailPhone(addId, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            requesters_list = dao.getRequestersOnThisAddressIDByAfirstAlastEmail(addId, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            requesters_list = dao.getRequestersOnThisAddressIDByAfirstAlastPhone(addId, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            requesters_list = dao.getRequestersOnThisAddressIDByAfirstPhoneEmail(addId, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            requesters_list = dao.getRequestersOnThisAddressIDByAlastEmailPhone(addId, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            requesters_list = dao.getRequestersOnThisAddressIDByAfirstAlast(addId, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            requesters_list = dao.getRequestersOnThisAddressIDByAfirstEmail(addId, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            requesters_list = dao.getRequestersOnThisAddressIDByAfirstPhone(addId, afirst, phone)
        elif(len(args) == 2) and alast and email:
            requesters_list = dao.getRequestersOnThisAddressIDByAlastEmail(addId, alast, email)
        elif(len(args) == 2) and alast and phone:
            requesters_list = dao.getRequestersOnThisAddressIDByAlastPhone(addId, alast, phone)
        elif(len(args) == 2) and email and phone:
            requesters_list = dao.getRequestersOnThisAddressIDByEmailPhone(addId, email, phone)
        elif(len(args) == 1) and afirst:
            requesters_list = dao.getRequestersOnThisAddressIDByAfirst(addId, afirst)
        elif(len(args) == 1) and alast:
            requesters_list = dao.getRequestersOnThisAddressIDByAlast(addId, alast)
        elif(len(args) == 1) and email:
            requesters_list = dao.getRequestersOnThisAddressIDByEmail(addId, email)
        elif(len(args) == 1) and phone:
            requesters_list = dao.getRequestersOnThisAddressIDByPhone(addId, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

# ================ #
#     Cities       #
# ================ #

    def getRequestersOnThisCity(self, cname):

        daoCity = CityDAO()
        dao = RequesterDAO()

        if not daoCity.getCityByName(cname):
            return jsonify(Error="City Not Found"), 404

        requesters_list = dao.getRequestersOnThisCity(cname)
        result_list = []

        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

    def searchRequestersOnThisCity(self, cname, args):

        daoCity = CityDAO()
        dao = RequesterDAO()

        if not daoCity.getCityByName(cname):
            return jsonify(Error = 'City Not Found'), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        requesters_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            requesters_list = dao.getRequestersOnThisCityAfirstAlastEmailPhone(cname, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            requesters_list = dao.getRequestersOnThisCityByAfirstAlastEmail(cname, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            requesters_list = dao.getRequestersOnThisCityByAfirstAlastPhone(cname, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            requesters_list = dao.getRequestersOnThisCityByAfirstPhoneEmail(cname, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            requesters_list = dao.getRequestersOnThisCityByAlastEmailPhone(cname, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            requesters_list = dao.getRequestersOnThisCityByAfirstAlast(cname, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            requesters_list = dao.getRequestersOnThisCityByAfirstEmail(cname, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            requesters_list = dao.getRequestersOnThisCityByAfirstPhone(cname, afirst, phone)
        elif(len(args) == 2) and alast and email:
            requesters_list = dao.getRequestersOnThisCityByAlastEmail(cname, alast, email)
        elif(len(args) == 2) and alast and phone:
            requesters_list = dao.getRequestersOnThisCityByAlastPhone(cname, alast, phone)
        elif(len(args) == 2) and email and phone:
            requesters_list = dao.getRequestersOnThisCityByEmailPhone(cname, email, phone)
        elif(len(args) == 1) and afirst:
            requesters_list = dao.getRequestersOnThisCityByAfirst(cname, afirst)
        elif(len(args) == 1) and alast:
            requesters_list = dao.getRequestersOnThisCityByAlast(cname, alast)
        elif(len(args) == 1) and email:
            requesters_list = dao.getRequestersOnThisCityByEmail(cname, email)
        elif(len(args) == 1) and phone:
            requesters_list = dao.getRequestersOnThisCityByPhone(cname, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

# ================ #
#     Regions      #
# ================ #

    def getRequestersOnThisRegion(self, rname):

        dao = RequesterDAO()
        daoReg = RegionDAO()

        if not daoReg.getRegionByName(rname):
            return jsonify(Error="Region Not Found"), 404

        requesters_list = dao.getRequestersOnThisRegion(rname)
        result_list = []

        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

    def searchRequestersOnThisRegion(self, rname, args):

        dao = RequesterDAO()
        daoReg = RegionDAO()

        if not daoReg.getRegionByName(rname):
            return jsonify(Error = 'Region Not Found'), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        requesters_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            requesters_list = dao.getRequestersOnThisRegionAfirstAlastEmailPhone(rname, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            requesters_list = dao.getRequestersOnThisRegionByAfirstAlastEmail(rname, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            requesters_list = dao.getRequestersOnThisRegionByAfirstAlastPhone(rname, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            requesters_list = dao.getRequestersOnThisRegionByAfirstPhoneEmail(rname, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            requesters_list = dao.getRequestersOnThisRegionByAlastEmailPhone(rname, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            requesters_list = dao.getRequestersOnThisRegionByAfirstAlast(rname, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            requesters_list = dao.getRequestersOnThisRegionByAfirstEmail(rname, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            requesters_list = dao.getRequestersOnThisRegionByAfirstPhone(rname, afirst, phone)
        elif(len(args) == 2) and alast and email:
            requesters_list = dao.getRequestersOnThisRegionByAlastEmail(rname, alast, email)
        elif(len(args) == 2) and alast and phone:
            requesters_list = dao.getRequestersOnThisRegionByAlastPhone(rname, alast, phone)
        elif(len(args) == 2) and email and phone:
            requesters_list = dao.getRequestersOnThisRegionByEmailPhone(rname, email, phone)
        elif(len(args) == 1) and afirst:
            requesters_list = dao.getRequestersOnThisRegionByAfirst(rname, afirst)
        elif(len(args) == 1) and alast:
            requesters_list = dao.getRequestersOnThisRegionByAlast(rname, alast)
        elif(len(args) == 1) and email:
            requesters_list = dao.getRequestersOnThisRegionByEmail(rname, email)
        elif(len(args) == 1) and phone:
            requesters_list = dao.getRequestersOnThisRegionByPhone(rname, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

# ================ #
#    Resources     #
# ================ #

    def getRequestersOfThisResource(self, rsid):

        dao = RequesterDAO()
        daoRec = ResourceDAO()

        if not daoRec.getResourceById(rsid):
            return jsonify(Error="Resource Not Found"), 404

        requesters_list = dao.getRequestersOnThisResource(rsid)
        result_list = []

        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

    def searchRequestersOfThisResource(self, rsid, args):

        dao = RequesterDAO()
        daoRec = ResourceDAO()

        if not daoRec.getResourceById(rsid):
            return jsonify(Error="Resource Not Found"), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        requesters_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            requesters_list = dao.getRequestersOnThisResourceAfirstAlastEmailPhone(rsid, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            requesters_list = dao.getRequestersOnThisResourceByAfirstAlastEmail(rsid, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            requesters_list = dao.getRequestersOnThisResourceByAfirstAlastPhone(rsid, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            requesters_list = dao.getRequestersOnThisResourceByAfirstPhoneEmail(rsid, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            requesters_list = dao.getRequestersOnThisResourceByAlastEmailPhone(rsid, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            requesters_list = dao.getRequestersOnThisResourceByAfirstAlast(rsid, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            requesters_list = dao.getRequestersOnThisResourceByAfirstEmail(rsid, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            requesters_list = dao.getRequestersOnThisResourceByAfirstPhone(rsid, afirst, phone)
        elif(len(args) == 2) and alast and email:
            requesters_list = dao.getRequestersOnThisResourceByAlastEmail(rsid, alast, email)
        elif(len(args) == 2) and alast and phone:
            requesters_list = dao.getRequestersOnThisResourceByAlastPhone(rsid, alast, phone)
        elif(len(args) == 2) and email and phone:
            requesters_list = dao.getRequestersOnThisResourceByEmailPhone(rsid, email, phone)
        elif(len(args) == 1) and afirst:
            requesters_list = dao.getRequestersOnThisResourceByAfirst(rsid, afirst)
        elif(len(args) == 1) and alast:
            requesters_list = dao.getRequestersOnThisResourceByAlast(rsid, alast)
        elif(len(args) == 1) and email:
            requesters_list = dao.getRequestersOnThisResourceByEmail(rsid, email)
        elif(len(args) == 1) and phone:
            requesters_list = dao.getRequestersOnThisResourceByPhone(rsid, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

# ========================= #
#    Resources Requested    #
# ========================= #

    def getRequestersOfThisResourceRequested(self, rrid):

        dao = RequesterDAO()
        daoRecRec = ResourceRequestedDAO()

        if not daoRecRec.getResourceRequestedById(rrid):
            return jsonify(Error="Resource Requested Not Found"), 404

        requesters_list = dao.getRequestersOnThisResourceRequested(rrid)
        result_list = []

        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

    def searchRequestersOfThisResourceRequested(self, rrid, args):

        dao = RequesterDAO()
        daoRecRec = ResourceRequestedDAO()

        if not daoRecRec.getResourceRequestedById(rrid):
            return jsonify(Error="Resource Requested Not Found"), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        requesters_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            requesters_list = dao.getRequestersOnThisResourceRequestedAfirstAlastEmailPhone(rrid, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            requesters_list = dao.getRequestersOnThisResourceRequestedByAfirstAlastEmail(rrid, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            requesters_list = dao.getRequestersOnThisResourceRequestedByAfirstAlastPhone(rrid, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            requesters_list = dao.getRequestersOnThisResourceRequestedByAfirstPhoneEmail(rrid, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            requesters_list = dao.getRequestersOnThisResourceRequestedByAlastEmailPhone(rrid, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            requesters_list = dao.getRequestersOnThisResourceRequestedByAfirstAlast(rrid, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            requesters_list = dao.getRequestersOnThisResourceRequestedByAfirstEmail(rrid, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            requesters_list = dao.getRequestersOnThisResourceRequestedByAfirstPhone(rrid, afirst, phone)
        elif(len(args) == 2) and alast and email:
            requesters_list = dao.getRequestersOnThisResourceRequestedByAlastEmail(rrid, alast, email)
        elif(len(args) == 2) and alast and phone:
            requesters_list = dao.getRequestersOnThisResourceRequestedByAlastPhone(rrid, alast, phone)
        elif(len(args) == 2) and email and phone:
            requesters_list = dao.getRequestersOnThisResourceRequestedByEmailPhone(rrid, email, phone)
        elif(len(args) == 1) and afirst:
            requesters_list = dao.getRequestersOnThisResourceRequestedByAfirst(rrid, afirst)
        elif(len(args) == 1) and alast:
            requesters_list = dao.getRequestersOnThisResourceRequestedByAlast(rrid, alast)
        elif(len(args) == 1) and email:
            requesters_list = dao.getRequestersOnThisResourceRequestedByEmail(rrid, email)
        elif(len(args) == 1) and phone:
            requesters_list = dao.getRequestersOnThisResourceRequestedByPhone(rrid, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

# ========================= #
#        Categories         #
# ========================= #

    def getRequestersOfThisCategory(self, cat_name):

        dao = RequesterDAO()
        daoCat = CategoryDAO()

        if not daoCat.getCategoryByName(cat_name):
            return jsonify(Error="Category Not Found"), 404

        requesters_list = dao.getRequestersOnThisCategory(cat_name)
        result_list = []

        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

    def searchRequestersOfThisCategory(self, cat_name, args):

        dao = RequesterDAO()
        daoCat = CategoryDAO()

        if not daoCat.getCategoryByName(cat_name):
            return jsonify(Error="Category Not Found"), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        requesters_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            requesters_list = dao.getRequestersOnThisCategoryAfirstAlastEmailPhone(cat_name, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            requesters_list = dao.getRequestersOnThisCategoryByAfirstAlastEmail(cat_name, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            requesters_list = dao.getRequestersOnThisCategoryByAfirstAlastPhone(cat_name, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            requesters_list = dao.getRequestersOnThisCategoryByAfirstPhoneEmail(cat_name, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            requesters_list = dao.getRequestersOnThisCategoryByAlastEmailPhone(cat_name, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            requesters_list = dao.getRequestersOnThisCategoryByAfirstAlast(cat_name, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            requesters_list = dao.getRequestersOnThisCategoryByAfirstEmail(cat_name, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            requesters_list = dao.getRequestersOnThisCategoryByAfirstPhone(cat_name, afirst, phone)
        elif(len(args) == 2) and alast and email:
            requesters_list = dao.getRequestersOnThisCategoryByAlastEmail(cat_name, alast, email)
        elif(len(args) == 2) and alast and phone:
            requesters_list = dao.getRequestersOnThisCategoryByAlastPhone(cat_name, alast, phone)
        elif(len(args) == 2) and email and phone:
            requesters_list = dao.getRequestersOnThisCategoryByEmailPhone(cat_name, email, phone)
        elif(len(args) == 1) and afirst:
            requesters_list = dao.getRequestersOnThisCategoryByAfirst(cat_name, afirst)
        elif(len(args) == 1) and alast:
            requesters_list = dao.getRequestersOnThisCategoryByAlast(cat_name, alast)
        elif(len(args) == 1) and email:
            requesters_list = dao.getRequestersOnThisCategoryByEmail(cat_name, email)
        elif(len(args) == 1) and phone:
            requesters_list = dao.getRequestersOnThisCategoryByPhone(cat_name, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

# ========================= #
#        Transactions       #
# ========================= #

    def getRequestersOfThisTransaction(self, tid):

        dao = RequesterDAO()
        daoT = TransactionDAO()

        if not daoT.getTransactionById(tid):
            return jsonify(Error="Transaction Not Found"), 404

        requesters_list = dao.getRequestersOnThisTransaction(tid)
        result_list = []

        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

    def searchRequestersOfThisTransaction(self, tid, args):

        dao = RequesterDAO()
        daoT = TransactionDAO()

        if not daoT.getTransactionById(tid):
            return jsonify(Error="Transaction Not Found"), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        requesters_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            requesters_list = dao.getRequestersOnThisTransactionAfirstAlastEmailPhone(tid, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            requesters_list = dao.getRequestersOnThisTransactionByAfirstAlastEmail(tid, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            requesters_list = dao.getRequestersOnThisTransactionByAfirstAlastPhone(tid, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            requesters_list = dao.getRequestersOnThisTransactionByAfirstPhoneEmail(tid, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            requesters_list = dao.getRequestersOnThisTransactionByAlastEmailPhone(tid, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            requesters_list = dao.getRequestersOnThisTransactionByAfirstAlast(tid, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            requesters_list = dao.getRequestersOnThisTransactionByAfirstEmail(tid, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            requesters_list = dao.getRequestersOnThisTransactionByAfirstPhone(tid, afirst, phone)
        elif(len(args) == 2) and alast and email:
            requesters_list = dao.getRequestersOnThisTransactionByAlastEmail(tid, alast, email)
        elif(len(args) == 2) and alast and phone:
            requesters_list = dao.getRequestersOnThisTransactionByAlastPhone(tid, alast, phone)
        elif(len(args) == 2) and email and phone:
            requesters_list = dao.getRequestersOnThisTransactionByEmailPhone(tid, email, phone)
        elif(len(args) == 1) and afirst:
            requesters_list = dao.getRequestersOnThisTransactionByAfirst(tid, afirst)
        elif(len(args) == 1) and alast:
            requesters_list = dao.getRequestersOnThisTransactionByAlast(tid, alast)
        elif(len(args) == 1) and email:
            requesters_list = dao.getRequestersOnThisTransactionByEmail(tid, email)
        elif(len(args) == 1) and phone:
            requesters_list = dao.getRequestersOnThisTransactionByPhone(tid, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

# ========================= #
#        Credit Cards       #
# ========================= #

    def getRequestersOfThisCreditCard(self, cid):

        dao = RequesterDAO()
        daoC = CreditCardDAO()

        if not daoC.getCreditCardById(cid):
            return jsonify(Error="Credit Card Not Found"), 404

        requesters_list = dao.getRequestersOnThisCreditCard(cid)
        result_list = []

        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

    def searchRequestersOfThisCreditCard(self, cid, args):

        dao = RequesterDAO()
        daoC = CreditCardDAO()

        if not daoC.getCreditCardById(cid):
            return jsonify(Error="Credit Card Not Found"), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        requesters_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            requesters_list = dao.getRequestersOnThisCreditCardAfirstAlastEmailPhone(cid, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            requesters_list = dao.getRequestersOnThisCreditCardByAfirstAlastEmail(cid, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            requesters_list = dao.getRequestersOnThisCreditCardByAfirstAlastPhone(cid, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            requesters_list = dao.getRequestersOnThisCreditCardByAfirstPhoneEmail(cid, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            requesters_list = dao.getRequestersOnThisCreditCardByAlastEmailPhone(cid, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            requesters_list = dao.getRequestersOnThisCreditCardByAfirstAlast(cid, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            requesters_list = dao.getRequestersOnThisCreditCardByAfirstEmail(cid, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            requesters_list = dao.getRequestersOnThisCreditCardByAfirstPhone(cid, afirst, phone)
        elif(len(args) == 2) and alast and email:
            requesters_list = dao.getRequestersOnThisCreditCardByAlastEmail(cid, alast, email)
        elif(len(args) == 2) and alast and phone:
            requesters_list = dao.getRequestersOnThisCreditCardByAlastPhone(cid, alast, phone)
        elif(len(args) == 2) and email and phone:
            requesters_list = dao.getRequestersOnThisCreditCardByEmailPhone(cid, email, phone)
        elif(len(args) == 1) and afirst:
            requesters_list = dao.getRequestersOnThisCreditCardByAfirst(cid, afirst)
        elif(len(args) == 1) and alast:
            requesters_list = dao.getRequestersOnThisCreditCardByAlast(cid, alast)
        elif(len(args) == 1) and email:
            requesters_list = dao.getRequestersOnThisCreditCardByEmail(cid, email)
        elif(len(args) == 1) and phone:
            requesters_list = dao.getRequestersOnThisCreditCardByPhone(cid, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

# ========================= #
#        Payments           #
# ========================= #

    def getRequestersOfThisPayment(self, payid):

        dao = RequesterDAO()
        daoP = PaymentDAO()

        if not daoP.getPaymentById(payid):
            return jsonify(Error="Payment Not Found"), 404

        requesters_list = dao.getRequestersOnThisPayment(payid)
        result_list = []

        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

    def searchRequestersOfThisPayment(self, payid, args):

        dao = RequesterDAO()
        daoP = PaymentDAO()

        if not daoP.getPaymentById(payid):
            return jsonify(Error="Payment Not Found"), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        requesters_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            requesters_list = dao.getRequestersOnThisPaymentAfirstAlastEmailPhone(payid, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            requesters_list = dao.getRequestersOnThisPaymentByAfirstAlastEmail(payid, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            requesters_list = dao.getRequestersOnThisPaymentByAfirstAlastPhone(payid, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            requesters_list = dao.getRequestersOnThisPaymentByAfirstPhoneEmail(payid, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            requesters_list = dao.getRequestersOnThisPaymentByAlastEmailPhone(payid, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            requesters_list = dao.getRequestersOnThisPaymentByAfirstAlast(payid, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            requesters_list = dao.getRequestersOnThisPaymentByAfirstEmail(payid, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            requesters_list = dao.getRequestersOnThisPaymentByAfirstPhone(payid, afirst, phone)
        elif(len(args) == 2) and alast and email:
            requesters_list = dao.getRequestersOnThisPaymentByAlastEmail(payid, alast, email)
        elif(len(args) == 2) and alast and phone:
            requesters_list = dao.getRequestersOnThisPaymentByAlastPhone(payid, alast, phone)
        elif(len(args) == 2) and email and phone:
            requesters_list = dao.getRequestersOnThisPaymentByEmailPhone(payid, email, phone)
        elif(len(args) == 1) and afirst:
            requesters_list = dao.getRequestersOnThisPaymentByAfirst(payid, afirst)
        elif(len(args) == 1) and alast:
            requesters_list = dao.getRequestersOnThisPaymentByAlast(payid, alast)
        elif(len(args) == 1) and email:
            requesters_list = dao.getRequestersOnThisPaymentByEmail(payid, email)
        elif(len(args) == 1) and phone:
            requesters_list = dao.getRequestersOnThisPaymentByPhone(payid, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

# ========================= #
#        Orders Info        #
# ========================= #

    def getRequestersOfThisOrderInfo(self, oid):

        dao = RequesterDAO()
        daoO = OrderDAO()

        if not daoO.getOrderById(oid):
            return jsonify(Error="Order Info Not Found"), 404

        requesters_list = dao.getRequestersOnThisOrderInfo(oid)
        result_list = []

        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requesters = result_list)

    def searchRequestersOfThisOrderInfo(self, oid, args):

        dao = RequesterDAO()
        daoO = OrderDAO()

        if not daoO.getOrderById(oid):
            return jsonify(Error="Order Info Not Found"), 404

        afirst = args.get('afirst')
        alast = args.get('alast')
        email = args.get('email')
        phone = args.get('phone')

        requesters_list = []

        if(len(args) == 4) and afirst and alast and email and phone:
            requesters_list = dao.getRequestersOnThisOrderInfoAfirstAlastEmailPhone(oid, afirst, alast, email, phone)
        elif(len(args) == 3) and afirst and alast and email:
            requesters_list = dao.getRequestersOnThisOrderInfoByAfirstAlastEmail(oid, afirst, alast, email)
        elif(len(args) == 3) and afirst and alast and phone:
            requesters_list = dao.getRequestersOnThisOrderInfoByAfirstAlastPhone(oid, afirst, alast, phone)
        elif(len(args) == 3) and afirst and phone and email:
            requesters_list = dao.getRequestersOnThisOrderInfoByAfirstPhoneEmail(oid, afirst, phone, email)
        elif(len(args) == 3) and alast and email and phone:
            requesters_list = dao.getRequestersOnThisOrderInfoByAlastEmailPhone(oid, alast, email, phone)
        elif(len(args) == 2) and afirst and alast:
            requesters_list = dao.getRequestersOnThisOrderInfoByAfirstAlast(oid, afirst, alast)
        elif(len(args) == 2) and afirst and email:
            requesters_list = dao.getRequestersOnThisOrderInfoByAfirstEmail(oid, afirst, email)
        elif(len(args) == 2) and afirst and phone:
            requesters_list = dao.getRequestersOnThisOrderInfoByAfirstPhone(oid, afirst, phone)
        elif(len(args) == 2) and alast and email:
            requesters_list = dao.getRequestersOnThisOrderInfoByAlastEmail(oid, alast, email)
        elif(len(args) == 2) and alast and phone:
            requesters_list = dao.getRequestersOnThisOrderInfoByAlastPhone(oid, alast, phone)
        elif(len(args) == 2) and email and phone:
            requesters_list = dao.getRequestersOnThisOrderInfoByEmailPhone(oid, email, phone)
        elif(len(args) == 1) and afirst:
            requesters_list = dao.getRequestersOnThisOrderInfoByAfirst(oid, afirst)
        elif(len(args) == 1) and alast:
            requesters_list = dao.getRequestersOnThisOrderInfoByAlast(oid, alast)
        elif(len(args) == 1) and email:
            requesters_list = dao.getRequestersOnThisOrderInfoByEmail(oid, email)
        elif(len(args) == 1) and phone:
            requesters_list = dao.getRequestersOnThisOrderInfoByPhone(oid, phone)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
            return jsonify(Requesters = result_list)