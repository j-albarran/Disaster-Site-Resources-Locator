from flask import jsonify
from dao.resource_requested import ResourceRequestedDAO
from dao.city import CityDAO
from dao.region import RegionDAO
from dao.keyword import KeywordDAO
from dao.requester import RequesterDAO
from dao.category import CategoryDAO

class ResourceRequestedHandler:

    def build_resource_requested_dict(self, row):
        result = {}
        result['rrid'] = row[0]
        result['rrqty'] = row[1]
        result['rrdescription'] = row[2]
        result['rr_request_date'] = row[3]
        result['rr_changed_date'] = row[4]
        return result

    def build_resource_requested_attributes(self, rrid, rrqty, rrdescription, rr_request_date, rr_changed_date):
        result = {}
        result['rrid'] = rrid
        result['rrqty'] = rrqty
        result['rrdescription'] = rrdescription
        result['rr_request_date'] = rr_request_date
        result['rr_changed_date'] = rr_changed_date
        return result

    def getAllResourcesRequested(self):
        dao = ResourceRequestedDAO()
        resource_requested_list = dao.getAllResourcesRequested()
        result_list = []
        for row in resource_requested_list:
            result = self.build_resource_requested_dict(row)
            result_list.append(result)
        return jsonify(Resources_Requested = result_list)

    def searchResourcesRequested(self, args):
        rrqty = args.get('rrqty')
        rr_request_date = args.get('rr_request_date')
        rr_changed_date = args.get('rr_changed_date')
        dao = ResourceRequestedDAO()
        resource_requested_list = []
        if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
            resource_requested_list = dao.getResourcesRequestedByQtyRequestDateChangedDate(rrqty, rr_request_date, rr_changed_date)
        elif (len(args) == 2) and rrqty and rr_request_date:
            resource_requested_list = dao.getResourcesRequestedByQtyRequestDate(rrqty, rr_request_date)
        elif (len(args) == 2) and rrqty and rr_changed_date:
            resource_requested_list = dao.getResourcesRequestedByQtyChangedDate(rrqty, rr_changed_date)
        elif (len(args) == 2) and rr_request_date and rr_changed_date:
            resource_requested_list = dao.getResourcesRequestedByRequestDateChangedDate(rr_request_date, rr_changed_date)
        elif (len(args) == 1) and rrqty:
            resource_requested_list = dao.getResourcesRequestedByQty(rrqty)
        elif (len(args) == 1) and rr_request_date:
            resource_requested_list = dao.getResourcesRequestedByRequestDate(rr_request_date)
        elif (len(args) == 1) and rr_changed_date:
            resource_requested_list = dao.getResourcesRequestedByChangedDate(rr_changed_date)
        else:
            return jsonify(Error = "Malformed Query String"), 400
        result_list = []
        for row in resource_requested_list:
            result = self.build_resource_requested_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error = "ResourceRequested Not Found"), 404
        else:
            return jsonify(Resources_Requested = result_list)

    def getResourceRequestedById(self, rrid):
        dao = ResourceRequestedDAO()
        resource_requested = dao.getResourceRequestedById(rrid)
        if not resource_requested:
            return jsonify(Error = "Resource Requested Not Found"), 404
        else:
            result = self.build_resource_requested_dict(resource_requested)
            return jsonify(Resource_Requested = result)

    def insertResourceRequested(self, form):
        if len(form) != 4:
            return jsonify(Error = "Malformed Post Request"), 400
        else:
            rrqty = form['rrqty']
            rrdescription = form['rrdescription']
            rr_request_date = form['rr_request_date']
            rr_changed_date = form['rr_changed_date']
            if rrqty and rrdescription and rr_request_date and rr_changed_date:
                dao = ResourceRequestedDAO()
                rrid = dao.insert(rrqty, rrdescription, rr_request_date, rr_changed_date)
                result = self.build_resource_requested_attributes(rrid, rrqty, rrdescription, rr_request_date, rr_changed_date)
                return jsonify(Resource_Requested = result), 201
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400

    def updateResourceRequested(self, rrid, form):
        dao = ResourceRequestedDAO()
        if not dao.getResourceRequestedById(rrid):
            return jsonify(Error = "Resource Requested Not Found"), 404
        else:
            if len(form) != 4:
                return jsonify(Error = "Malformed Update Request"), 400
            else:
                rrqty = form['rrqty']
                rrdescription = form['rrdescription']
                rr_request_date = form['rr_request_date']
                rr_changed_date = form['rr_changed_date']
                if rrqty and rrdescription and rr_request_date and rr_changed_date:
                    dao = ResourceRequestedDAO()
                    dao.update(rrid, rrqty, rrdescription, rr_request_date, rr_changed_date)
                    result = self.build_resource_requested_attributes(rrid, rrqty, rrdescription, rr_request_date, rr_changed_date)
                    return jsonify(Resource_Requested = result), 201
                else:
                    return jsonify(Error = "Unexpected attributes in post request"), 400

    def deleteResourceRequested(self, rrid):
        dao = ResourceRequestedDAO()
        if not dao.getResourceRequestedById(rrid):
            return jsonify(Error = "Resource Requested Not Found"), 404
        else:
            dao.delete(rrid)
            return jsonify(DeleteStatus = "OK"), 200

    def getResourcesRequestedByCityName(self, cname):
        if not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByCityName(cname)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByCityName(self, cname, args):
        if not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityNameByQtyRequestDateChangedDate(cname, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByCityNameByQtyRequestDate(cname, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityNameByQtyChangedDate(cname, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityNameByRequestDateChangedDate(cname, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByCityNameByQty(cname, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByCityNameByRequestDate(cname, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityNameByChangedDate(cname, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)

    def getResourcesRequestedByRegionName(self, rname):
        if not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByRegionName(rname)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByRegionName(self, rname, args):
        if not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionNameByQtyRequestDateChangedDate(rname, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByRegionNameByQtyRequestDate(rname, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionNameByQtyChangedDate(rname, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionNameByRequestDateChangedDate(rname, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByRegionNameByQty(rname, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByRegionNameByRequestDate(rname, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionNameByChangedDate(rname, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)

    def getResourcesRequestedByKeywordId(self, kid):
        if not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByKeywordId(kid)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByKeywordId(self, kid, args):
        if not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordIdByQtyRequestDateChangedDate(kid, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordIdByQtyRequestDate(kid, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordIdByQtyChangedDate(kid, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordIdByRequestDateChangedDate(kid, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByKeywordIdByQty(kid, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordIdByRequestDate(kid, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordIdByChangedDate(kid, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)

    def getResourcesRequestedByRequesterId(self, rid):
        if not RequesterDAO().getRequesterById(rid):
            return jsonify(Error = "Requester Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByRequesterId(rid)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByRequesterId(self, rid, args):
        if not RequesterDAO().getRequesterById(rid):
            return jsonify(Error = "Requester Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRequesterIdByQtyRequestDateChangedDate(rid, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByRequesterIdByQtyRequestDate(rid, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRequesterIdByQtyChangedDate(rid, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRequesterIdByRequestDateChangedDate(rid, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByRequesterIdByQty(rid, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByRequesterIdByRequestDate(rid, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRequesterIdByChangedDate(rid, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)

    def getResourcesRequestedByCategoryName(self, cat_name):
        if not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByCategoryName(cat_name)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByCategoryName(self, cat_name, args):
        if not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCategoryNameByQtyRequestDateChangedDate(cat_name, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByCategoryNameByQtyRequestDate(cat_name, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCategoryNameByQtyChangedDate(cat_name, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCategoryNameByRequestDateChangedDate(cat_name, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByCategoryNameByQty(cat_name, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByCategoryNameByRequestDate(cat_name, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCategoryNameByChangedDate(cat_name, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)

    def getResourcesRequestedByCityKeyword(self, cname, kid):
        if not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "City and Keyword Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByCityKeyword(cname, kid)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByCityKeyword(self, cname, kid, args):
        if not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "City and Keyword Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityKeywordByQtyRequestDateChangedDate(cname, kid, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByCityKeywordByQtyRequestDate(cname, kid, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityKeywordByQtyChangedDate(cname, kid, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityKeywordByRequestDateChangedDate(cname, kid, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByCityKeywordByQty(cname, kid, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByCityKeywordByRequestDate(cname, kid, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityKeywordByChangedDate(cname, kid, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)

    def getResourcesRequestedByCityCategory(self, cname, cat_name):
        if not CityDAO().getCityByName(cname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "City and Category Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByCityCategory(cname, cat_name)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByCityCategory(self, cname, cat_name, args):
        if not CityDAO().getCityByName(cname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "City and Category Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityCategoryByQtyRequestDateChangedDate(cname, cat_name, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByCityCategoryByQtyRequestDate(cname, cat_name, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityCategoryByQtyChangedDate(cname, cat_name, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityCategoryByRequestDateChangedDate(cname, cat_name, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByCityCategoryByQty(cname, cat_name, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByCityCategoryByRequestDate(cname, cat_name, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityCategoryByChangedDate(cname, cat_name, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)

    def getResourcesRequestedByRegionKeyword(self, rname, kid):
        if not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Region and Keyword Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByRegionKeyword(rname, kid)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByRegionKeyword(self, rname, kid, args):
        if not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Region and Keyword Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionKeywordByQtyRequestDateChangedDate(rname, kid, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByRegionKeywordByQtyRequestDate(rname, kid, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionKeywordByQtyChangedDate(rname, kid, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionKeywordByRequestDateChangedDate(rname, kid, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByRegionKeywordByQty(rname, kid, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByRegionKeywordByRequestDate(rname, kid, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionKeywordByChangedDate(rname, kid, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)

    def getResourcesRequestedByRegionCategory(self, rname, cat_name):
        if not RegionDAO().getRegionByName(rname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Region and Category Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByRegionCategory(rname, cat_name)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByRegionCategory(self, rname, cat_name, args):
        if not RegionDAO().getRegionByName(rname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Region and Category Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionCategoryByQtyRequestDateChangedDate(rname, cat_name, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByRegionCategoryByQtyRequestDate(rname, cat_name, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionCategoryByQtyChangedDate(rname, cat_name, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionCategoryByRequestDateChangedDate(rname, cat_name, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByRegionCategoryByQty(rname, cat_name, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByRegionCategoryByRequestDate(rname, cat_name, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionCategoryByChangedDate(rname, cat_name, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)

    def getResourcesRequestedByKeywordRequester(self, kid, rid):
        if not KeywordDAO().getKeywordById(kid) and not RequesterDAO().getRequesterById(rid):
            return jsonify(Error = "Keyword and Requester Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not RequesterDAO().getRequesterById(rid):
            return jsonify(Error = "Requester Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByKeywordRequester(kid, rid)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByKeywordRequester(self, kid, rid, args):
        if not KeywordDAO().getKeywordById(kid) and not RequesterDAO().getRequesterById(rid):
            return jsonify(Error = "Keyword and Requester Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not RequesterDAO().getRequesterById(rid):
            return jsonify(Error = "Requester Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordRequesterByQtyRequestDateChangedDate(kid, rid, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordRequesterByQtyRequestDate(kid, rid, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordRequesterByQtyChangedDate(kid, rid, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordRequesterByRequestDateChangedDate(kid, rid, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByKeywordRequesterByQty(kid, rid, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordRequesterByRequestDate(kid, rid, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordRequesterByChangedDate(kid, rid, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)

    def getResourcesRequestedByKeywordCategory(self, kid, cat_name):
        if not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByKeywordCategory(kid, cat_name)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByKeywordCategory(self, kid, cat_name, args):
        if not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordCategoryByQtyRequestDateChangedDate(kid, cat_name, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordCategoryByQtyRequestDate(kid, cat_name, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordCategoryByQtyChangedDate(kid, cat_name, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordCategoryByRequestDateChangedDate(kid, cat_name, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByKeywordCategoryByQty(kid, cat_name, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordCategoryByRequestDate(kid, cat_name, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordCategoryByChangedDate(kid, cat_name, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)

    def getResourcesRequestedByRequesterCategory(self, rid, cat_name):
        if not RequesterDAO().getRequesterById(rid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Requester and Category Not Found"), 404
        elif not RequesterDAO().getRequesterById(rid):
            return jsonify(Error = "Requester Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByRequesterCategory(rid, cat_name)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByRequesterCategory(self, rid, cat_name, args):
        if not RequesterDAO().getRequesterById(rid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Requester and Category Not Found"), 404
        elif not RequesterDAO().getRequesterById(rid):
            return jsonify(Error = "Requester Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRequesterCategoryByQtyRequestDateChangedDate(rid, cat_name, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByRequesterCategoryByQtyRequestDate(rid, cat_name, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRequesterCategoryByQtyChangedDate(rid, cat_name, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRequesterCategoryByRequestDateChangedDate(rid, cat_name, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByRequesterCategoryByQty(rid, cat_name, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByRequesterCategoryByRequestDate(rid, cat_name, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRequesterCategoryByChangedDate(rid, cat_name, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)

    def getResourcesRequestedByCityKeywordCategory(self, cname, kid, cat_name):
        if not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "City, Keyword, and Category Not Found"), 404
        elif not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "City and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByCityKeywordCategory(cname, kid, cat_name)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByCityKeywordCategory(self, cname, kid, cat_name, args):
        if not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "City, Keyword, and Category Not Found"), 404
        elif not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "City and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityKeywordCategoryByQtyRequestDateChangedDate(cname, kid, cat_name, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByCityKeywordCategoryByQtyRequestDate(cname, kid, cat_name, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityKeywordCategoryByQtyChangedDate(cname, kid, cat_name, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityKeywordCategoryByRequestDateChangedDate(cname, kid, cat_name, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByCityKeywordCategoryByQty(cname, kid, cat_name, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByCityKeywordCategoryByRequestDate(cname, kid, cat_name, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByCityKeywordCategoryByChangedDate(cname, kid, cat_name, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)

    def getResourcesRequestedByRegionKeywordCategory(self, rname, kid, cat_name):
        if not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Region, Keyword, and Category Not Found"), 404
        elif not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Region and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByRegionKeywordCategory(rname, kid, cat_name)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByRegionKeywordCategory(self, rname, kid, cat_name, args):
        if not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Region, Keyword, and Category Not Found"), 404
        elif not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Region and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionKeywordCategoryByQtyRequestDateChangedDate(rname, kid, cat_name, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByRegionKeywordCategoryByQtyRequestDate(rname, kid, cat_name, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionKeywordCategoryByQtyChangedDate(rname, kid, cat_name, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionKeywordCategoryByRequestDateChangedDate(rname, kid, cat_name, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByRegionKeywordCategoryByQty(rname, kid, cat_name, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByRegionKeywordCategoryByRequestDate(rname, kid, cat_name, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByRegionKeywordCategoryByChangedDate(rname, kid, cat_name, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)

    def getResourcesRequestedByKeywordRequesterCategory(self, kid, rid, cat_name):
        if not KeywordDAO().getKeywordById(kid) and not RequesterDAO().getRequesterById(rid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword, Requester, and Category Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not RequesterDAO().getRequesterById(rid):
            return jsonify(Error = "Keyword and Requester Not Found"), 404
        elif not RequesterDAO().getRequesterById(rid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Requester and Category Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not RequesterDAO().getRequesterById(rid):
            return jsonify(Error = "Requester Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            resource_requested_list = ResourceRequestedDAO().getResourcesRequestedByKeywordRequesterCategory(kid, rid, cat_name)
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourcesRequested Not Found"), 404
            else:
                return jsonify(ResourcesRequested = result_list)

    def searchResourcesRequestedByKeywordRequesterCategory(self, kid, rid, cat_name, args):
        if not KeywordDAO().getKeywordById(kid) and not RequesterDAO().getRequesterById(rid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword, Requester, and Category Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not RequesterDAO().getRequesterById(rid):
            return jsonify(Error = "Keyword and Requester Not Found"), 404
        elif not RequesterDAO().getRequesterById(rid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Requester and Category Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not RequesterDAO().getRequesterById(rid):
            return jsonify(Error = "Requester Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rrqty = args.get('rrqty')
            rr_request_date = args.get('rr_request_date')
            rr_changed_date = args.get('rr_changed_date')
            dao = ResourceRequestedDAO()
            resource_requested_list = []
            if (len(args) == 3) and rrqty and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordRequesterCategoryByQtyRequestDateChangedDate(kid, rid, cat_name, rrqty, rr_request_date, rr_changed_date)
            elif (len(args) == 2) and rrqty and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordRequesterCategoryByQtyRequestDate(kid, rid, cat_name, rrqty, rr_request_date)
            elif (len(args) == 2) and rrqty and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordRequesterCategoryByQtyChangedDate(kid, rid, cat_name, rrqty, rr_changed_date)
            elif (len(args) == 2) and rr_request_date and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordRequesterCategoryByRequestDateChangedDate(kid, rid, cat_name, rr_request_date, rr_changed_date)
            elif (len(args) == 1) and rrqty:
                resource_requested_list = dao.getResourcesRequestedByKeywordRequesterCategoryByQty(kid, rid, cat_name, rrqty)
            elif (len(args) == 1) and rr_request_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordRequesterCategoryByRequestDate(kid, rid, cat_name, rr_request_date)
            elif (len(args) == 1) and rr_changed_date:
                resource_requested_list = dao.getResourcesRequestedByKeywordRequesterCategoryByChangedDate(kid, rid, cat_name, rr_changed_date)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_requested_list:
                result = self.build_resource_requested_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "ResourceRequested Not Found"), 404
            else:
                return jsonify(Resources_Requested = result_list)
