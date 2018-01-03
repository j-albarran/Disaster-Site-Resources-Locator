from flask import jsonify
from dao.resource import ResourceDAO

class ResourceHandler:

    def build_resource_dict(self, row):
        result = {}
        result['rsid'] = row[0]
        result['rname'] = row[1]
        result['rdescription'] = row[2]
        result['r_changed_date'] = row[3]
        result['rqty'] = row[4]
        result['rprice'] = row[5]
        result['r_supply_date'] = row[6]
        return result

    def build_resource_attributes(self, rsid, rname, rdescription, r_changed_date, rqty, rprice, r_supply_date):
        result = {}
        result['rsid'] = rsid
        result['rname'] = rname
        result['rdescription'] = rdescription
        result['r_changed_date'] = r_changed_date
        result['rqty'] = rqty
        result['rprice'] = rprice
        result['r_supply_date'] = r_supply_date
        return result

    def getAllResources(self):
        dao = ResourceDAO()
        resource_list = dao.getAllResources()
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error = "Resources Not Found"), 404
        else:
            return jsonify(Resources = result_list)

    def searchResources(self, args):
        rname = args.get('rname')
        r_changed_date = args.get('r_changed_date')
        rqty = args.get('rqty')
        rprice = args.get('rprice')
        r_supply_date = args.get('r_supply_date')
        dao = ResourceDAO()
        resource_list = []
        if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
            resource_list = dao.getResourcesByNameChangedDateQtyPriceSupplyDate(Name, ChangedDate, Qty, Price, SupplyDate)
        elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
            resource_list = dao.getResourcesByNameChangedDateQtyPrice(Name, ChangedDate, Qty, Price)
        elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
            resource_list = dao.getResourcesByNameChangedDateQtySupplyDate(Name, ChangedDate, Qty, SupplyDate)
        elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
            resource_list = dao.getResourcesByNameChangedDatePriceSupplyDate(Name, ChangedDate, Price, SupplyDate)
        elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
            resource_list = dao.getResourcesByNameQtyPriceSupplyDate(Name, Qty, Price, SupplyDate)
        elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
            resource_list = dao.getResourcesByChangedDateQtyPriceSupplyDate(ChangedDate, Qty, Price, SupplyDate)
        elif (len(args) == 3) and rname and r_changed_date and rqty:
            resource_list = dao.getResourcesByNameChangedDateQty(Name, ChangedDate, Qty)
        elif (len(args) == 3) and rname and r_changed_date and rprice:
            resource_list = dao.getResourcesByNameChangedDatePrice(Name, ChangedDate, Price)
        elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
            resource_list = dao.getResourcesByNameChangedDateSupplyDate(Name, ChangedDate, SupplyDate)
        elif (len(args) == 3) and rname and rqty and rprice:
            resource_list = dao.getResourcesByNameQtyPrice(Name, Qty, Price)
        elif (len(args) == 3) and rname and rqty and r_supply_date:
            resource_list = dao.getResourcesByNameQtySupplyDate(Name, Qty, SupplyDate)
        elif (len(args) == 3) and rname and rprice and r_supply_date:
            resource_list = dao.getResourcesByNamePriceSupplyDate(Name, Price, SupplyDate)
        elif (len(args) == 3) and r_changed_date and rqty and rprice:
            resource_list = dao.getResourcesByChangedDateQtyPrice(ChangedDate, Qty, Price)
        elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
            resource_list = dao.getResourcesByChangedDateQtySupplyDate(ChangedDate, Qty, SupplyDate)
        elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
            resource_list = dao.getResourcesByChangedDatePriceSupplyDate(ChangedDate, Price, SupplyDate)
        elif (len(args) == 3) and rqty and rprice and r_supply_date:
            resource_list = dao.getResourcesByQtyPriceSupplyDate(Qty, Price, SupplyDate)
        elif (len(args) == 2) and rname and r_changed_date:
            resource_list = dao.getResourcesByNameChangedDate(Name, ChangedDate)
        elif (len(args) == 2) and rname and rqty:
            resource_list = dao.getResourcesByNameQty(Name, Qty)
        elif (len(args) == 2) and rname and rprice:
            resource_list = dao.getResourcesByNamePrice(Name, Price)
        elif (len(args) == 2) and rname and r_supply_date:
            resource_list = dao.getResourcesByNameSupplyDate(Name, SupplyDate)
        elif (len(args) == 2) and r_changed_date and rqty:
            resource_list = dao.getResourcesByChangedDateQty(ChangedDate, Qty)
        elif (len(args) == 2) and r_changed_date and rprice:
            resource_list = dao.getResourcesByChangedDatePrice(ChangedDate, Price)
        elif (len(args) == 2) and r_changed_date and r_supply_date:
            resource_list = dao.getResourcesByChangedDateSupplyDate(ChangedDate, SupplyDate)
        elif (len(args) == 2) and rqty and rprice:
            resource_list = dao.getResourcesByQtyPrice(Qty, Price)
        elif (len(args) == 2) and rqty and r_supply_date:
            resource_list = dao.getResourcesByQtySupplyDate(Qty, SupplyDate)
        elif (len(args) == 2) and rprice and r_supply_date:
            resource_list = dao.getResourcesByPriceSupplyDate(Price, SupplyDate)
        elif (len(args) == 1) and rname:
            resource_list = dao.getResourcesByName(Name)
        elif (len(args) == 1) and r_changed_date:
            resource_list = dao.getResourcesByChangedDate(ChangedDate)
        elif (len(args) == 1) and rqty:
            resource_list = dao.getResourcesByQty(Qty)
        elif (len(args) == 1) and rprice:
            resource_list = dao.getResourcesByPrice(Price)
        elif (len(args) == 1) and r_supply_date:
            resource_list = dao.getResourcesBySupplyDate(SupplyDate)
        else:
            return jsonify(Error = "Malformed Query String"), 400
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        if not result_list:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            return jsonify(Resources = result_list)

    def getResourceById(self, rsid):
        dao = ResourceDAO()
        resource = dao.getResourceById(rsid)
        if not resource:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            result = self.build_resource_dict(resource)
            return jsonify(Resource = result)

    ***def insertResource(self, form):
        if len(form) != 1:
            return jsonify(Error = "Malformed Post Request"), 400
        else:
            resource = form['resource']
            if resource:
                dao = ResourceDAO()
                rsid = dao.insert(resource)
                result = self.build_resource_attributes(rsid, resource)
                return jsonify(Resource = result), 201
            else:
                return jsonify(Error = "Unexpected attributes in post request"), 400

    ***def updateResource(self, rsid, form):
        dao = ResourceDAO()
        if not dao.getResourceById(rsid):
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = form['resource']
            if resource:
                dao.update(rsid, resource)
                result = self.build_resource_attributes(rsid, resource)
                return jsonify(Resource = result), 200
            else:
                return jsonify(Error = "Unexpected attributes in update request"), 400

    ***def deleteResource(self, rsid):
        dao = ResourceDAO()
        if not dao.getResourceById(rsid):
            return jsonify(Error = "Resource Not Found"), 404
        else:
            dao.delete(rsid)
            return jsonify(DeleteStatus = "OK"), 200

    def getResourcesByCityName(self, cname):
        pass

    def searchResourcesByCityName(self, cname, args):
        if not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDateQtyPriceSupplyDate(cname, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityNameByNameChangedDateQtyPrice(cname, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDateQtySupplyDate(cname, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDatePriceSupplyDate(cname, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameQtyPriceSupplyDate(cname, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByChangedDateQtyPriceSupplyDate(cname, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityNameByNameChangedDateQty(cname, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityNameByNameChangedDatePrice(cname, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDateSupplyDate(cname, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByCityNameByNameQtyPrice(cname, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameQtySupplyDate(cname, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNamePriceSupplyDate(cname, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityNameByChangedDateQtyPrice(cname, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityNameByChangedDateQtySupplyDate(cname, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByChangedDatePriceSupplyDate(cname, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByQtyPriceSupplyDate(cname, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDate(cname, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByCityNameByNameQty(cname, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByCityNameByNamePrice(cname, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameSupplyDate(cname, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityNameByChangedDateQty(cname, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityNameByChangedDatePrice(cname, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityNameByChangedDateSupplyDate(cname, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCityNameByQtyPrice(cname, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityNameByQtySupplyDate(cname, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByPriceSupplyDate(cname, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByCityNameByName(cname, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCityNameByChangedDate(cname, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCityNameByQty(cname, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCityNameByPrice(cname, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCityNameBySupplyDate(cname, SupplyDate)
            else:
                return jsonify(Error = "Malformed Query String"), 400
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            if not result_list:
                return jsonify(Error = "Resource Not Found"), 404
            else:
                return jsonify(Resources = result_list)

    def getResourcesByRegionName(self, rname):
        pass

-----------------------------------------------------------------------------------------

    def searchResourcesByRegionName(self, rname, args):
        pass

    def getResourcesBySupplierId(self, sid):
        pass

    def searchResourcesBySupplierId(self, sid, args):
        pass

    def getResourcesByKeywordId(self, kid):
        pass

    def searchResourcesByKeywordId(self, kid, args):
        pass

    def getResourcesByCategoryName(self, cat_name):
        pass

    def searchResourcesByCategoryName(self, cat_name, args):
        pass

    def getResourcesByTransactionId(self, tid):
        pass

    def searchResourcesByTransactionId(self, tid, args):
        pass

    def getResourcesByOrderId(self, oid):
        pass

    def searchResourcesByOrderId(self, oid, args):
        pass

    !!!def getResourcesByCitySupplier(self, cname, sid):
        pass

    !!!def searchResourcesByCitySupplier(self, cname, sid, args):
        pass

    def getResourcesByCityKeyword(self, cname, kid):
        pass

    def searchResourcesByCityKeyword(self, cname, kid, args):
        pass

    def getResourcesByCityCategory(self, cname, cat_name):
        pass

    def searchResourcesByCityCategory(self, cname, cat_name, args):
        pass

    !!!def getResourcesByCityTransaction(self, cname, tid):
        pass

    !!!def searchResourcesByCityTransaction(self, cname, tid, args):
        pass

    !!!def getResourcesByCityOrder(self, cname, oid):
        pass

    !!!def searchResourcesByCityOrder(self, cname, oid, args):
        pass

    !!!def getResourcesByRegionSupplier(self, rname, sid):
        pass

    !!!def searchResourcesByRegionSupplier(self, rname, sid, args):
        pass

    def getResourcesByRegionKeyword(self, rname, kid):
        pass

    def searchResourcesByRegionKeyword(self, rname, kid, args):
        pass

    def getResourcesByRegionCategory(self, rname, cat_name):
        pass

    def searchResourcesByRegionCategory(self, rname, cat_name, args):
        pass

    !!!def getResourcesByRegionTransaction(self, rname, tid):
        pass

    !!!def searchResourcesByRegionTransaction(self, rname, tid, args):
        pass

    !!!def getResourcesByRegionOrder(self, rname, oid):
        pass

    !!!def searchResourcesByRegionOrder(self, rname, oid, args):
        pass

    def getResourcesBySupplierKeyword(self, sid, kid):
        pass

    def searchResourcesBySupplierKeyword(self, sid, kid, args):
        pass

    def getResourcesBySupplierCategory(self, sid, cat_name):
        pass

    def searchResourcesBySupplierCategory(self, sid, cat_name, args):
        pass

    !!!def getResourcesBySupplierTransaction(self, sid, tid):
        pass

    !!!def searchResourcesBySupplierTransaction(self, sid, tid, args):
        pass

    def getResourcesBySupplierOrder(self, sid, oid):
        pass

    def searchResourcesBySupplierOrder(self, sid, oid, args):
        pass

    def getResourcesByKeywordCategory(self, kid, cat_name):
        pass

    def searchResourcesByKeywordCategory(self, kid, cat_name, args):
        pass

    !!!def getResourcesByKeywordTransaction(self, kid, tid):
        pass

    !!!def searchResourcesByKeywordTransaction(self, kid, tid, args):
        pass

    def getResourcesByKeywordOrder(self, kid, oid):
        pass

    def searchResourcesByKeywordOrder(self, kid, oid, args):
        pass

    !!!def getResourcesByCategoryTransaction(self, cat_name, tid):
        pass

    !!!def searchResourcesByCategoryTransaction(self, cat_name, tid, args):
        pass

    def getResourcesByCategoryOrder(self, cat_name, oid):
        pass

    def searchResourcesByCategoryOrder(self, cat_name, oid, args):
        pass

    def getResourcesByTransactionOrder(self, tid, oid):
        pass

    def searchResourcesByTransactionOrder(self, tid, oid, args):
        pass

    !!!def getResourcesByCitySupplierKeyword(self, cname, sid, kid):
        pass

    !!!def searchResourcesByCitySupplierKeyword(self, cname, sid, kid, args):
        pass

    !!!def getResourcesByCitySupplierCategory(self, cname, sid, cat_name):
        pass

    !!!def searchResourcesByCitySupplierCategory(self, cname, sid, cat_name, args):
        pass

    !!!def getResourcesByCitySupplierTransaction(self, cname, sid, tid):
        pass

    !!!def searchResourcesByCitySupplierTransaction(self, cname, sid, tid, args):
        pass

    !!!def getResourcesByCitySupplierOrder(self, cname, sid, oid):
        pass

    !!!def searchResourcesByCitySupplierOrder(self, cname, sid, oid, args):
        pass

    def getResourcesByCityKeywordCategory(self, cname, kid, cat_name):
        pass

    def searchResourcesByCityKeywordCategory(self, cname, kid, cat_name, args):
        pass

    !!!def getResourcesByCityKeywordTransaction(self, cname, kid, tid):
        pass

    !!!def searchResourcesByCityKeywordTransaction(self, cname, kid, tid, args):
        pass

    def getResourcesByCityKeywordOrder(self, cname, kid, oid):
        pass

    def searchResourcesByCityKeywordOrder(self, cname, kid, oid, args):
        pass

    !!!def getResourcesByCityCategoryTransaction(self, cname, cat_name, tid):
        pass

    !!!def searchResourcesByCityCategoryTransaction(self, cname, cat_name, tid, args):
        pass

    def getResourcesByCityCategoryOrder(self, cname, cat_name, oid):
        pass

    def searchResourcesByCityCategoryOrder(self, cname, cat_name, oid, args):
        pass

    !!!def getResourcesByCityTransactionOrder(self, cname, tid, oid):
        pass

    !!!def searchResourcesByCityTransactionOrder(self, cname, tid, oid, args):
        pass

    !!!def getResourcesByRegionSupplierKeyword(self, rname, sid, kid):
        pass

    !!!def searchResourcesByRegionSupplierKeyword(self, rname, sid, kid, args):
        pass

    !!!def getResourcesByRegionSupplierCategory(self, rname, sid, cat_name):
        pass

    !!!def searchResourcesByRegionSupplierCategory(self, rname, sid, cat_name, args):
        pass

    !!!def getResourcesByRegionSupplierTransaction(self, rname, sid, cat_name):
        pass

    !!!def searchResourcesByRegionSupplierTransaction(self, rname, sid, cat_name, args):
        pass

    !!!def getResourcesByRegionSupplierOrder(self, rname, sid, oid):
        pass

    !!!def searchResourcesByRegionSupplierOrder(self, rname, sid, oid, args):
        pass

    def getResourcesByRegionKeywordCategory(self, rname, kid, cat_name):
        pass

    def searchResourcesByRegionKeywordCategory(self, rname, kid, cat_name, args):
        pass

    !!!def getResourcesByRegionKeywordTransaction(self, rname, kid, tid):
        pass

    !!!def searchResourcesByRegionKeywordTransaction(self, rname, kid, tid, args):
        pass

    def getResourcesByRegionKeywordOrder(self, rname, kid, oid):
        pass

    def searchResourcesByRegionKeywordOrder(self, rname, kid, oid, args):
        pass

    !!!def getResourcesByRegionCategoryTransaction(self, rname, cat_name, tid):
        pass

    !!!def searchResourcesByRegionCategoryTransaction(self, rname, cat_name, tid, args):
        pass

    def getResourcesByRegionCategoryOrder(self, rname, cat_name, oid):
        pass

    def searchResourcesByRegionCategoryOrder(self, rname, cat_name, oid, args):
        pass

    !!!def getResourcesByRegionTransactionOrder(self, rname, tid, oid):
        pass

    !!!def searchResourcesByRegionTransactionOrder(self, rname, tid, oid, args):
        pass

    def getResourcesBySupplierKeywordCategory(self, sid, kid, cat_name):
        pass

    def searchResourcesBySupplierKeywordCategory(self, sid, kid, cat_name, args):
        pass

    !!!def getResourcesBySupplierKeywordTransaction(self, sid, kid, tid):
        pass

    !!!def searchResourcesBySupplierKeywordTransaction(self, sid, kid, tid, args):
        pass

    def getResourcesBySupplierKeywordOrder(self, sid, kid, oid):
        pass

    def searchResourcesBySupplierKeywordOrder(self, sid, kid, oid, args):
        pass

    !!!def getResourcesBySupplierCategoryTransaction(self, sid, cat_name, tid):
        pass

    !!!def searchResourcesBySupplierCategoryTransaction(self, sid, cat_name, tid, args):
        pass

    def getResourcesBySupplierCategoryOrder(self, sid, cat_name, oid):
        pass

    def searchResourcesBySupplierCategoryOrder(self, sid, cat_name, oid, args):
        pass

    !!!def getResourcesBySupplierTransactionOrder(self, sid, tid, oid):
        pass

    !!!def searchResourcesBySupplierTransactionOrder(self, sid, tid, oid, args):
        pass

    !!!def getResourcesByKeywordCategoryTransaction(self, kid, cat_name, tid):
        pass

    !!!def searchResourcesByKeywordCategoryTransaction(self, kid, cat_name, tid, args):
        pass

    def getResourcesByKeywordCategoryOrder(self, kid, cat_name, oid):
        pass

    def searchResourcesByKeywordCategoryOrder(self, kid, cat_name, oid, args):
        pass

    !!!def getResourcesByKeywordTransactionOrder(self, kid, tid, oid):
        pass

    !!!def searchResourcesByKeywordTransactionOrder(self, kid, tid, oid, args):
        pass

    !!!def getResourcesByCategoryTransactionOrder(self, cat_name, tid, oid):
        pass

    !!!def searchResourcesByCategoryTransactionOrder(self, cat_name, tid, oid, args):
        pass
