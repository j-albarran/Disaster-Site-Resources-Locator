from flask import jsonify

class ResourceRequestedHandler:

    def build_resource_requested_dict(self, row):
        result = {}
        result['rrid'] = row[0]
        result['rrqty'] = row[1]
        result['rrdescription'] = row[2]
        result['rr_request_date'] = row[3]
        result['rr_changed_date'] = row[4]

    def getAllResourcesRequested(self):
        dao = ResourceRequestedDAO()
        resources_requested_list = dao.getAllResourcesRequested()
        result_list = []
        for row in resources_requested_list:
            result = self.build_resource_requested_dict(row)
            result_list.append(result)
        return jsonify(Resources_Requested = result_list)

    def searchResourcesRequested(self, args):
        rrqty = args.get('rrqty')
        rrdescription = args.get('rrdescription')
        rr_request_date = args.get('rr_request_date')
        rr_changed_date = args.get('rr_changed_date')

        dao = ResourceRequestedDAO()

        for row in resources_requested_list:
            result = self.build_resource_requested_dict(row)
            result_list.append(result)
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
        pass

    def updateResourceRequested(self, rrid, form):
        pass

    def deleteResourceRequested(self, rrid):
        pass

    def getResourcesRequestedByCityName(self, cname):
        pass

    def searchResourcesRequestedByCityName(self, cname, args):
        pass

    def getResourcesRequestedByRegionName(self, rname):
        pass

    def searchResourcesRequestedByRegionName(self, rname, args):
        pass

    def getResourcesRequestedByKeywordId(self, kid):
        pass

    def searchResourcesRequestedByKeywordId(self, kid, args):
        pass

    def getResourcesRequestedByRequesterId(self, rid):
        pass

    def searchResourcesRequestedByRequesterId(self, rid, args):
        pass

    def getResourcesRequestedByCategoryName(self, cat_name):
        pass

    def searchResourcesRequestedByCategoryName(self, cat_name, args):
        pass

    def getResourcesRequestedByCityKeyword(self, cname, kid):
        pass

    def searchResourcesRequestedByCityKeyword(self, cname, kid, args):
        pass

    def getResourcesRequestedByCityCategory(self, cname, cay_name):
        pass

    def searchResourcesRequestedByCityCategory(self, cname, cay_name, args):
        pass

    def getResourcesRequestedByRegionKeyword(self, rname, kid):
        pass

    def searchResourcesRequestedByRegionKeyword(self, rname, kid, args):
        pass

    def getResourcesRequestedByRegionCategory(self, rname, cat_name):
        pass

    def searchResourcesRequestedByRegionCategory(self, rname, cat_name, args):
        pass

    def getResourcesRequestedByKeywordRequester(self, kid, rid):
        pass

    def searchResourcesRequestedByKeywordRequester(self, kid, rid, args):
        pass

    def getResourcesRequestedByKeywordCategory(self, kid, cat_name):
        pass

    def searchResourcesRequestedByKeywordCategory(self, kid, cat_name, args):
        pass

    def getResourcesRequestedByRequesterCategory(self, rid, cat_name):
        pass

    def searchResourcesRequestedByRequesterCategory(self, rid, cat_name, args):
        pass

    def getResourcesRequestedByCityKeywordCategory(self, cname, kid, cat_name):
        pass

    def searchResourcesRequestedByCityKeywordCategory(self, cname, kid, cat_name, args):
        pass

    def getResourcesRequestedByRegionKeywordCategory(self, rname, kid, cat_name):
        pass

    def searchResourcesRequestedByRegionKeywordCategory(self, rname, kid, cat_name, args):
        pass

    def getResourcesRequestedByKeywordRequesterCategory(self, kid, rid, cat_name):
        pass

    def searchResourcesRequestedByKeywordRequesterCategory(self, kid, rid, cat_name, args):
        pass
