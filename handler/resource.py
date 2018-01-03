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
        if not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNameChangedDateQtyPriceSupplyDate(rname, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionNameByNameChangedDateQtyPrice(rname, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNameChangedDateQtySupplyDate(rname, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNameChangedDatePriceSupplyDate(rname, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNameQtyPriceSupplyDate(rname, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByChangedDateQtyPriceSupplyDate(rname, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionNameByNameChangedDateQty(rname, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionNameByNameChangedDatePrice(rname, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNameChangedDateSupplyDate(rname, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByRegionNameByNameQtyPrice(rname, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNameQtySupplyDate(rname, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNamePriceSupplyDate(rname, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionNameByChangedDateQtyPrice(rname, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByChangedDateQtySupplyDate(rname, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByChangedDatePriceSupplyDate(rname, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByQtyPriceSupplyDate(rname, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByRegionNameByNameChangedDate(rname, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByRegionNameByNameQty(rname, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByRegionNameByNamePrice(rname, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByNameSupplyDate(rname, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionNameByChangedDateQty(rname, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionNameByChangedDatePrice(rname, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByChangedDateSupplyDate(rname, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByRegionNameByQtyPrice(rname, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByQtySupplyDate(rname, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionNameByPriceSupplyDate(rname, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByRegionNameByName(rname, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByRegionNameByChangedDate(rname, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByRegionNameByQty(rname, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByRegionNameByPrice(rname, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByRegionNameBySupplyDate(rname, SupplyDate)
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

    def getResourcesBySupplierId(self, sid):
        pass

    def searchResourcesBySupplierId(self, sid, args):
        if not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDateQtyPriceSupplyDate(sid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDateQtyPrice(sid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDateQtySupplyDate(sid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDatePriceSupplyDate(sid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNameQtyPriceSupplyDate(sid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByChangedDateQtyPriceSupplyDate(sid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDateQty(sid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDatePrice(sid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDateSupplyDate(sid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesBySupplierIdByNameQtyPrice(sid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNameQtySupplyDate(sid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNamePriceSupplyDate(sid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierIdByChangedDateQtyPrice(sid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByChangedDateQtySupplyDate(sid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByChangedDatePriceSupplyDate(sid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByQtyPriceSupplyDate(sid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesBySupplierIdByNameChangedDate(sid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesBySupplierIdByNameQty(sid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesBySupplierIdByNamePrice(sid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByNameSupplyDate(sid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierIdByChangedDateQty(sid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierIdByChangedDatePrice(sid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByChangedDateSupplyDate(sid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesBySupplierIdByQtyPrice(sid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByQtySupplyDate(sid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdByPriceSupplyDate(sid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesBySupplierIdByName(sid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesBySupplierIdByChangedDate(sid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesBySupplierIdByQty(sid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesBySupplierIdByPrice(sid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesBySupplierIdBySupplyDate(sid, SupplyDate)
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

    def getResourcesByKeywordId(self, kid):
        pass

    def searchResourcesByKeywordId(self, kid, args):
        if not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDateQtyPriceSupplyDate(kid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDateQtyPrice(kid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDateQtySupplyDate(kid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDatePriceSupplyDate(kid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNameQtyPriceSupplyDate(kid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByChangedDateQtyPriceSupplyDate(kid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDateQty(kid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDatePrice(kid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDateSupplyDate(kid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByKeywordIdByNameQtyPrice(kid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNameQtySupplyDate(kid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNamePriceSupplyDate(kid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordIdByChangedDateQtyPrice(kid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByChangedDateQtySupplyDate(kid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByChangedDatePriceSupplyDate(kid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByQtyPriceSupplyDate(kid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByKeywordIdByNameChangedDate(kid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByKeywordIdByNameQty(kid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByKeywordIdByNamePrice(kid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByNameSupplyDate(kid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordIdByChangedDateQty(kid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordIdByChangedDatePrice(kid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByChangedDateSupplyDate(kid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByKeywordIdByQtyPrice(kid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByQtySupplyDate(kid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdByPriceSupplyDate(kid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByKeywordIdByName(kid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByKeywordIdByChangedDate(kid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByKeywordIdByQty(kid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByKeywordIdByPrice(kid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByKeywordIdBySupplyDate(kid, SupplyDate)
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

    def getResourcesByCategoryName(self, cat_name):
        pass

    def searchResourcesByCategoryName(self, cat_name, args):
        if not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDateQtyPriceSupplyDate(cat_name, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDateQtyPrice(cat_name, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDateQtySupplyDate(cat_name, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDatePriceSupplyDate(cat_name, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNameQtyPriceSupplyDate(cat_name, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByChangedDateQtyPriceSupplyDate(cat_name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDateQty(cat_name, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDatePrice(cat_name, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDateSupplyDate(cat_name, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByCategoryNameByNameQtyPrice(cat_name, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNameQtySupplyDate(cat_name, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNamePriceSupplyDate(cat_name, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCategoryNameByChangedDateQtyPrice(cat_name, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByChangedDateQtySupplyDate(cat_name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByChangedDatePriceSupplyDate(cat_name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByQtyPriceSupplyDate(cat_name, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByCategoryNameByNameChangedDate(cat_name, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByCategoryNameByNameQty(cat_name, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByCategoryNameByNamePrice(cat_name, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByNameSupplyDate(cat_name, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCategoryNameByChangedDateQty(cat_name, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCategoryNameByChangedDatePrice(cat_name, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByChangedDateSupplyDate(cat_name, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCategoryNameByQtyPrice(cat_name, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByQtySupplyDate(cat_name, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameByPriceSupplyDate(cat_name, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByCategoryNameByName(cat_name, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCategoryNameByChangedDate(cat_name, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCategoryNameByQty(cat_name, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCategoryNameByPrice(cat_name, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCategoryNameBySupplyDate(cat_name, SupplyDate)
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

    def getResourcesByTransactionId(self, tid):
        pass

    def searchResourcesByTransactionId(self, tid, args):
        if not TransactionDAO().getTransactionById(tid):
            return jsonify(Error = "Transaction Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDateQtyPriceSupplyDate(tid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDateQtyPrice(tid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDateQtySupplyDate(tid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDatePriceSupplyDate(tid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNameQtyPriceSupplyDate(tid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByChangedDateQtyPriceSupplyDate(tid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDateQty(tid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDatePrice(tid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDateSupplyDate(tid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByTransactionIdByNameQtyPrice(tid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNameQtySupplyDate(tid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNamePriceSupplyDate(tid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByTransactionIdByChangedDateQtyPrice(tid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByChangedDateQtySupplyDate(tid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByChangedDatePriceSupplyDate(tid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByQtyPriceSupplyDate(tid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByTransactionIdByNameChangedDate(tid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByTransactionIdByNameQty(tid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByTransactionIdByNamePrice(tid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByNameSupplyDate(tid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByTransactionIdByChangedDateQty(tid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByTransactionIdByChangedDatePrice(tid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByChangedDateSupplyDate(tid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByTransactionIdByQtyPrice(tid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByQtySupplyDate(tid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdByPriceSupplyDate(tid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByTransactionIdByName(tid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByTransactionIdByChangedDate(tid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByTransactionIdByQty(tid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByTransactionIdByPrice(tid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByTransactionIdBySupplyDate(tid, SupplyDate)
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

    def getResourcesByOrderId(self, oid):
        pass

    def searchResourcesByOrderId(self, oid, args):
        if not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNameChangedDateQtyPriceSupplyDate(oid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByOrderIdByNameChangedDateQtyPrice(oid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNameChangedDateQtySupplyDate(oid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNameChangedDatePriceSupplyDate(oid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNameQtyPriceSupplyDate(oid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByChangedDateQtyPriceSupplyDate(oid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByOrderIdByNameChangedDateQty(oid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByOrderIdByNameChangedDatePrice(oid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNameChangedDateSupplyDate(oid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByOrderIdByNameQtyPrice(oid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNameQtySupplyDate(oid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNamePriceSupplyDate(oid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByOrderIdByChangedDateQtyPrice(oid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByChangedDateQtySupplyDate(oid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByChangedDatePriceSupplyDate(oid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByQtyPriceSupplyDate(oid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByOrderIdByNameChangedDate(oid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByOrderIdByNameQty(oid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByOrderIdByNamePrice(oid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByNameSupplyDate(oid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByOrderIdByChangedDateQty(oid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByOrderIdByChangedDatePrice(oid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByChangedDateSupplyDate(oid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByOrderIdByQtyPrice(oid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByQtySupplyDate(oid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByOrderIdByPriceSupplyDate(oid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByOrderIdByName(oid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByOrderIdByChangedDate(oid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByOrderIdByQty(oid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByOrderIdByPrice(oid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByOrderIdBySupplyDate(oid, SupplyDate)
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

    def getResourcesByCityKeyword(self, cname, kid):
        pass

    def searchResourcesByCityKeyword(self, cname, kid, args):
        if not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "City and Keyword Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDateQtyPriceSupplyDate(cname, kid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDateQtyPrice(cname, kid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDateQtySupplyDate(cname, kid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDatePriceSupplyDate(cname, kid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNameQtyPriceSupplyDate(cname, kid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByChangedDateQtyPriceSupplyDate(cname, kid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDateQty(cname, kid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDatePrice(cname, kid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDateSupplyDate(cname, kid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordByNameQtyPrice(cname, kid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNameQtySupplyDate(cname, kid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNamePriceSupplyDate(cname, kid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordByChangedDateQtyPrice(cname, kid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByChangedDateQtySupplyDate(cname, kid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByChangedDatePriceSupplyDate(cname, kid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByQtyPriceSupplyDate(cname, kid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByCityKeywordByNameChangedDate(cname, kid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByCityKeywordByNameQty(cname, kid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByCityKeywordByNamePrice(cname, kid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByNameSupplyDate(cname, kid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityKeywordByChangedDateQty(cname, kid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityKeywordByChangedDatePrice(cname, kid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByChangedDateSupplyDate(cname, kid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordByQtyPrice(cname, kid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByQtySupplyDate(cname, kid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordByPriceSupplyDate(cname, kid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByCityKeywordByName(cname, kid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCityKeywordByChangedDate(cname, kid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCityKeywordByQty(cname, kid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCityKeywordByPrice(cname, kid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordBySupplyDate(cname, kid, SupplyDate)
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

    def getResourcesByCityCategory(self, cname, cat_name):
        pass

    def searchResourcesByCityCategory(self, cname, cat_name, args):
        if not CityDAO().getCityByName(cname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "City and Category Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDateQtyPriceSupplyDate(cname, cat_name, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDateQtyPrice(cname, cat_name, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDateQtySupplyDate(cname, cat_name, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDatePriceSupplyDate(cname, cat_name, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNameQtyPriceSupplyDate(cname, cat_name, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByChangedDateQtyPriceSupplyDate(cname, cat_name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDateQty(cname, cat_name, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDatePrice(cname, cat_name, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDateSupplyDate(cname, cat_name, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryByNameQtyPrice(cname, cat_name, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNameQtySupplyDate(cname, cat_name, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNamePriceSupplyDate(cname, cat_name, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryByChangedDateQtyPrice(cname, cat_name, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByChangedDateQtySupplyDate(cname, cat_name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByChangedDatePriceSupplyDate(cname, cat_name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByQtyPriceSupplyDate(cname, cat_name, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByCityCategoryByNameChangedDate(cname, cat_name, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByCityCategoryByNameQty(cname, cat_name, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByCityCategoryByNamePrice(cname, cat_name, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByNameSupplyDate(cname, cat_name, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityCategoryByChangedDateQty(cname, cat_name, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityCategoryByChangedDatePrice(cname, cat_name, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByChangedDateSupplyDate(cname, cat_name, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryByQtyPrice(cname, cat_name, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByQtySupplyDate(cname, cat_name, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryByPriceSupplyDate(cname, cat_name, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByCityCategoryByName(cname, cat_name, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCityCategoryByChangedDate(cname, cat_name, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCityCategoryByQty(cname, cat_name, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCityCategoryByPrice(cname, cat_name, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryBySupplyDate(cname, cat_name, SupplyDate)
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

    def getResourcesByRegionKeyword(self, rname, kid):
        pass

    def searchResourcesByRegionKeyword(self, rname, kid, args):
        if not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Region and Keyword Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDateQtyPriceSupplyDate(rname, kid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityNameByNameChangedDateQtyPrice(rname, kid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDateQtySupplyDate(rname, kid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDatePriceSupplyDate(rname, kid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameQtyPriceSupplyDate(rname, kid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByChangedDateQtyPriceSupplyDate(rname, kid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityNameByNameChangedDateQty(rname, kid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityNameByNameChangedDatePrice(rname, kid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDateSupplyDate(rname, kid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByCityNameByNameQtyPrice(rname, kid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameQtySupplyDate(rname, kid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNamePriceSupplyDate(rname, kid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityNameByChangedDateQtyPrice(rname, kid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityNameByChangedDateQtySupplyDate(rname, kid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByChangedDatePriceSupplyDate(rname, kid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByQtyPriceSupplyDate(rname, kid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByCityNameByNameChangedDate(rname, kid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByCityNameByNameQty(rname, kid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByCityNameByNamePrice(rname, kid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByCityNameByNameSupplyDate(rname, kid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityNameByChangedDateQty(rname, kid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityNameByChangedDatePrice(rname, kid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityNameByChangedDateSupplyDate(rname, kid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCityNameByQtyPrice(rname, kid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityNameByQtySupplyDate(rname, kid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityNameByPriceSupplyDate(rname, kid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByCityNameByName(rname, kid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCityNameByChangedDate(rname, kid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCityNameByQty(rname, kid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCityNameByPrice(rname, kid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCityNameBySupplyDate(rname, kid, SupplyDate)
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

    def getResourcesByRegionCategory(self, rname, cat_name):
        pass

    def searchResourcesByRegionCategory(self, rname, cat_name, args):
        if not RegionDAO().getRegionByName(rname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Region and Category Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDateQtyPriceSupplyDate(rname, cat_name, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDateQtyPrice(rname, cat_name, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDateQtySupplyDate(rname, cat_name, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDatePriceSupplyDate(rname, cat_name, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNameQtyPriceSupplyDate(rname, cat_name, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByChangedDateQtyPriceSupplyDate(rname, cat_name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDateQty(rname, cat_name, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDatePrice(rname, cat_name, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDateSupplyDate(rname, cat_name, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryByNameQtyPrice(rname, cat_name, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNameQtySupplyDate(rname, cat_name, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNamePriceSupplyDate(rname, cat_name, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryByChangedDateQtyPrice(rname, cat_name, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByChangedDateQtySupplyDate(rname, cat_name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByChangedDatePriceSupplyDate(rname, cat_name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByQtyPriceSupplyDate(rname, cat_name, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByRegionCategoryByNameChangedDate(rname, cat_name, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByRegionCategoryByNameQty(rname, cat_name, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByRegionCategoryByNamePrice(rname, cat_name, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByNameSupplyDate(rname, cat_name, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionCategoryByChangedDateQty(rname, cat_name, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionCategoryByChangedDatePrice(rname, cat_name, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByChangedDateSupplyDate(rname, cat_name, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryByQtyPrice(rname, cat_name, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByQtySupplyDate(rname, cat_name, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryByPriceSupplyDate(rname, cat_name, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByRegionCategoryByName(rname, cat_name, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByRegionCategoryByChangedDate(rname, cat_name, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByRegionCategoryByQty(rname, cat_name, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByRegionCategoryByPrice(rname, cat_name, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryBySupplyDate(rname, cat_name, SupplyDate)
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

    def getResourcesBySupplierKeyword(self, sid, kid):
        pass

    def searchResourcesBySupplierKeyword(self, sid, kid, args):
        if not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Supplier and Keyword Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDateQtyPriceSupplyDate(sid, kid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDateQtyPrice(sid, kid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDateQtySupplyDate(sid, kid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDatePriceSupplyDate(sid, kid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameQtyPriceSupplyDate(sid, kid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDateQtyPriceSupplyDate(sid, kid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDateQty(sid, kid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDatePrice(sid, kid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDateSupplyDate(sid, kid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByNameQtyPrice(sid, kid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameQtySupplyDate(sid, kid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNamePriceSupplyDate(sid, kid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDateQtyPrice(sid, kid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDateQtySupplyDate(sid, kid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDatePriceSupplyDate(sid, kid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByQtyPriceSupplyDate(sid, kid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameChangedDate(sid, kid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesBySupplierKeywordByNameQty(sid, kid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByNamePrice(sid, kid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByNameSupplyDate(sid, kid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDateQty(sid, kid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDatePrice(sid, kid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDateSupplyDate(sid, kid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByQtyPrice(sid, kid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByQtySupplyDate(sid, kid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordByPriceSupplyDate(sid, kid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesBySupplierKeywordByName(sid, kid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesBySupplierKeywordByChangedDate(sid, kid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesBySupplierKeywordByQty(sid, kid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesBySupplierKeywordByPrice(sid, kid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordBySupplyDate(sid, kid, SupplyDate)
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

    def getResourcesBySupplierCategory(self, sid, cat_name):
        pass

    def searchResourcesBySupplierCategory(self, sid, cat_name, args):
        if not SupplierDAO().getSupplierById(sid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Supplier and Category Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDateQtyPriceSupplyDate(sid, cat_name, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDateQtyPrice(sid, cat_name, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDateQtySupplyDate(sid, cat_name, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDatePriceSupplyDate(sid, cat_name, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameQtyPriceSupplyDate(sid, cat_name, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDateQtyPriceSupplyDate(sid, cat_name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDateQty(sid, cat_name, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDatePrice(sid, cat_name, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDateSupplyDate(sid, cat_name, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByNameQtyPrice(sid, cat_name, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameQtySupplyDate(sid, cat_name, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNamePriceSupplyDate(sid, cat_name, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDateQtyPrice(sid, cat_name, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDateQtySupplyDate(sid, cat_name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDatePriceSupplyDate(sid, cat_name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByQtyPriceSupplyDate(sid, cat_name, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameChangedDate(sid, cat_name, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesBySupplierCategoryByNameQty(sid, cat_name, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByNamePrice(sid, cat_name, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByNameSupplyDate(sid, cat_name, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDateQty(sid, cat_name, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDatePrice(sid, cat_name, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDateSupplyDate(sid, cat_name, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByQtyPrice(sid, cat_name, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByQtySupplyDate(sid, cat_name, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryByPriceSupplyDate(sid, cat_name, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesBySupplierCategoryByName(sid, cat_name, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesBySupplierCategoryByChangedDate(sid, cat_name, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesBySupplierCategoryByQty(sid, cat_name, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesBySupplierCategoryByPrice(sid, cat_name, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryBySupplyDate(sid, cat_name, SupplyDate)
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

    def getResourcesBySupplierOrder(self, sid, oid):
        pass

    def searchResourcesBySupplierOrder(self, sid, oid, args):
        if not SupplierDAO().getSupplierById(sid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Supplier and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDateQtyPriceSupplyDate(sid, oid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDateQtyPrice(sid, oid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDateQtySupplyDate(sid, oid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDatePriceSupplyDate(sid, oid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNameQtyPriceSupplyDate(sid, oid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByChangedDateQtyPriceSupplyDate(sid, oid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDateQty(sid, oid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDatePrice(sid, oid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDateSupplyDate(sid, oid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesBySupplierOrderByNameQtyPrice(sid, oid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNameQtySupplyDate(sid, oid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNamePriceSupplyDate(sid, oid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierOrderByChangedDateQtyPrice(sid, oid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByChangedDateQtySupplyDate(sid, oid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByChangedDatePriceSupplyDate(sid, oid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByQtyPriceSupplyDate(sid, oid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesBySupplierOrderByNameChangedDate(sid, oid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesBySupplierOrderByNameQty(sid, oid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesBySupplierOrderByNamePrice(sid, oid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByNameSupplyDate(sid, oid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierOrderByChangedDateQty(sid, oid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierOrderByChangedDatePrice(sid, oid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByChangedDateSupplyDate(sid, oid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesBySupplierOrderByQtyPrice(sid, oid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByQtySupplyDate(sid, oid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderByPriceSupplyDate(sid, oid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesBySupplierOrderByName(sid, oid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesBySupplierOrderByChangedDate(sid, oid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesBySupplierOrderByQty(sid, oid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesBySupplierOrderByPrice(sid, oid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesBySupplierOrderBySupplyDate(sid, oid, SupplyDate)
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

    def getResourcesByKeywordCategory(self, kid, cat_name):
        pass

    def searchResourcesByKeywordCategory(self, kid, cat_name, args):
        if not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDateQtyPriceSupplyDate(kid, cat_name, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDateQtyPrice(kid, cat_name, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDateQtySupplyDate(kid, cat_name, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDatePriceSupplyDate(kid, cat_name, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameQtyPriceSupplyDate(kid, cat_name, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDateQtyPriceSupplyDate(kid, cat_name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDateQty(kid, cat_name, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDatePrice(kid, cat_name, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDateSupplyDate(kid, cat_name, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByNameQtyPrice(kid, cat_name, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameQtySupplyDate(kid, cat_name, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNamePriceSupplyDate(kid, cat_name, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDateQtyPrice(kid, cat_name, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDateQtySupplyDate(kid, cat_name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDatePriceSupplyDate(kid, cat_name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByQtyPriceSupplyDate(kid, cat_name, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameChangedDate(kid, cat_name, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByKeywordCategoryByNameQty(kid, cat_name, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByNamePrice(kid, cat_name, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByNameSupplyDate(kid, cat_name, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDateQty(kid, cat_name, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDatePrice(kid, cat_name, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDateSupplyDate(kid, cat_name, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByQtyPrice(kid, cat_name, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByQtySupplyDate(kid, cat_name, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryByPriceSupplyDate(kid, cat_name, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByKeywordCategoryByName(kid, cat_name, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByKeywordCategoryByChangedDate(kid, cat_name, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByKeywordCategoryByQty(kid, cat_name, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByKeywordCategoryByPrice(kid, cat_name, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryBySupplyDate(kid, cat_name, SupplyDate)
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

    def getResourcesByKeywordOrder(self, kid, oid):
        pass

    def searchResourcesByKeywordOrder(self, kid, oid, args):
        if not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword and Order Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDateQtyPriceSupplyDate(kid, oid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDateQtyPrice(kid, oid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDateQtySupplyDate(kid, oid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDatePriceSupplyDate(kid, oid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNameQtyPriceSupplyDate(kid, oid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByChangedDateQtyPriceSupplyDate(kid, oid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDateQty(kid, oid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDatePrice(kid, oid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDateSupplyDate(kid, oid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByKeywordOrderByNameQtyPrice(kid, oid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNameQtySupplyDate(kid, oid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNamePriceSupplyDate(kid, oid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordOrderByChangedDateQtyPrice(kid, oid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByChangedDateQtySupplyDate(kid, oid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByChangedDatePriceSupplyDate(kid, oid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByQtyPriceSupplyDate(kid, oid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByKeywordOrderByNameChangedDate(kid, oid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByKeywordOrderByNameQty(kid, oid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByKeywordOrderByNamePrice(kid, oid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByNameSupplyDate(kid, oid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordOrderByChangedDateQty(kid, oid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordOrderByChangedDatePrice(kid, oid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByChangedDateSupplyDate(kid, oid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByKeywordOrderByQtyPrice(kid, oid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByQtySupplyDate(kid, oid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderByPriceSupplyDate(kid, oid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByKeywordOrderByName(kid, oid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByKeywordOrderByChangedDate(kid, oid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByKeywordOrderByQty(kid, oid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByKeywordOrderByPrice(kid, oid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByKeywordOrderBySupplyDate(kid, oid, SupplyDate)
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

    def getResourcesByCategoryOrder(self, cat_name, oid):
        pass

    def searchResourcesByCategoryOrder(self, cat_name, oid, args):
        if not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDateQtyPriceSupplyDate(cat_name, oid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDateQtyPrice(cat_name, oid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDateQtySupplyDate(cat_name, oid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDatePriceSupplyDate(cat_name, oid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNameQtyPriceSupplyDate(cat_name, oid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByChangedDateQtyPriceSupplyDate(cat_name, oid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDateQty(cat_name, oid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDatePrice(cat_name, oid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDateSupplyDate(cat_name, oid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByCategoryOrderByNameQtyPrice(cat_name, oid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNameQtySupplyDate(cat_name, oid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNamePriceSupplyDate(cat_name, oid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCategoryOrderByChangedDateQtyPrice(cat_name, oid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByChangedDateQtySupplyDate(cat_name, oid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByChangedDatePriceSupplyDate(cat_name, oid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByQtyPriceSupplyDate(cat_name, oid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByCategoryOrderByNameChangedDate(cat_name, oid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByCategoryOrderByNameQty(cat_name, oid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByCategoryOrderByNamePrice(cat_name, oid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByNameSupplyDate(cat_name, oid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCategoryOrderByChangedDateQty(cat_name, oid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCategoryOrderByChangedDatePrice(cat_name, oid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByChangedDateSupplyDate(cat_name, oid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCategoryOrderByQtyPrice(cat_name, oid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByQtySupplyDate(cat_name, oid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderByPriceSupplyDate(cat_name, oid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByCategoryOrderByName(cat_name, oid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCategoryOrderByChangedDate(cat_name, oid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCategoryOrderByQty(cat_name, oid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCategoryOrderByPrice(cat_name, oid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCategoryOrderBySupplyDate(cat_name, oid, SupplyDate)
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

    def getResourcesByTransactionOrder(self, tid, oid):
        pass

    def searchResourcesByTransactionOrder(self, tid, oid, args):
        if not TransactionDAO().getTransactionById(tid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Transaction and Order Not Found"), 404
        elif not TransactionDAO().getTransactionById(tid):
            return jsonify(Error = "Transaction Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDateQtyPriceSupplyDate(tid, oid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDateQtyPrice(tid, oid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDateQtySupplyDate(tid, oid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDatePriceSupplyDate(tid, oid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNameQtyPriceSupplyDate(tid, oid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByChangedDateQtyPriceSupplyDate(tid, oid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDateQty(tid, oid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDatePrice(tid, oid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDateSupplyDate(tid, oid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByTransactionOrderByNameQtyPrice(tid, oid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNameQtySupplyDate(tid, oid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNamePriceSupplyDate(tid, oid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByTransactionOrderByChangedDateQtyPrice(tid, oid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByChangedDateQtySupplyDate(tid, oid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByChangedDatePriceSupplyDate(tid, oid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByQtyPriceSupplyDate(tid, oid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByTransactionOrderByNameChangedDate(tid, oid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByTransactionOrderByNameQty(tid, oid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByTransactionOrderByNamePrice(tid, oid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByNameSupplyDate(tid, oid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByTransactionOrderByChangedDateQty(tid, oid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByTransactionOrderByChangedDatePrice(tid, oid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByChangedDateSupplyDate(tid, oid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByTransactionOrderByQtyPrice(tid, oid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByQtySupplyDate(tid, oid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderByPriceSupplyDate(tid, oid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByTransactionOrderByName(tid, oid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByTransactionOrderByChangedDate(tid, oid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByTransactionOrderByQty(tid, oid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByTransactionOrderByPrice(tid, oid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByTransactionOrderBySupplyDate(tid, oid, SupplyDate)
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

    def getResourcesByCityKeywordCategory(self, cname, kid, cat_name):
        pass

    def searchResourcesByCityKeywordCategory(self, cname, kid, cat_name, args):
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
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDateQtyPriceSupplyDate(cname, kid, cat_name, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDateQtyPrice(cname, kid, cat_name, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDateQtySupplyDate(cname, kid, cat_name, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDatePriceSupplyDate(cname, kid, cat_name, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameQtyPriceSupplyDate(cname, kid, cat_name, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDateQtyPriceSupplyDate(cname, kid, cat_name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDateQty(cname, kid, cat_name, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDatePrice(cname, kid, cat_name, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDateSupplyDate(cname, kid, cat_name, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameQtyPrice(cname, kid, cat_name, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameQtySupplyDate(cname, kid, cat_name, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNamePriceSupplyDate(cname, kid, cat_name, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDateQtyPrice(cname, kid, cat_name, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDateQtySupplyDate(cname, kid, cat_name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDatePriceSupplyDate(cname, kid, cat_name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByQtyPriceSupplyDate(cname, kid, cat_name, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameChangedDate(cname, kid, cat_name, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameQty(cname, kid, cat_name, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByNamePrice(cname, kid, cat_name, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByNameSupplyDate(cname, kid, cat_name, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDateQty(cname, kid, cat_name, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDatePrice(cname, kid, cat_name, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDateSupplyDate(cname, kid, cat_name, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByQtyPrice(cname, kid, cat_name, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByQtySupplyDate(cname, kid, cat_name, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByPriceSupplyDate(cname, kid, cat_name, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByCityKeywordCategoryByName(cname, kid, cat_name, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCityKeywordCategoryByChangedDate(cname, kid, cat_name, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCityKeywordCategoryByQty(cname, kid, cat_name, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCityKeywordCategoryByPrice(cname, kid, cat_name, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordCategoryBySupplyDate(cname, kid, cat_name, SupplyDate)
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

    def getResourcesByCityKeywordOrder(self, cname, kid, oid):
        pass

    def searchResourcesByCityKeywordOrder(self, cname, kid, oid, args):
        if not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "City, Keyword, and Order Not Found"), 404
        elif not CityDAO().getCityByName(cname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "City and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword and Order Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDateQtyPriceSupplyDate(cname, kid, oid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDateQtyPrice(cname, kid, oid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDateQtySupplyDate(cname, kid, oid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDatePriceSupplyDate(cname, kid, oid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameQtyPriceSupplyDate(cname, kid, oid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDateQtyPriceSupplyDate(cname, kid, oid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDateQty(cname, kid, oid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDatePrice(cname, kid, oid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDateSupplyDate(cname, kid, oid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByNameQtyPrice(cname, kid, oid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameQtySupplyDate(cname, kid, oid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNamePriceSupplyDate(cname, kid, oid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDateQtyPrice(cname, kid, oid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDateQtySupplyDate(cname, kid, oid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDatePriceSupplyDate(cname, kid, oid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByQtyPriceSupplyDate(cname, kid, oid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameChangedDate(cname, kid, oid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByCityKeywordOrderByNameQty(cname, kid, oid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByNamePrice(cname, kid, oid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByNameSupplyDate(cname, kid, oid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDateQty(cname, kid, oid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDatePrice(cname, kid, oid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDateSupplyDate(cname, kid, oid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByQtyPrice(cname, kid, oid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByQtySupplyDate(cname, kid, oid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderByPriceSupplyDate(cname, kid, oid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByCityKeywordOrderByName(cname, kid, oid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCityKeywordOrderByChangedDate(cname, kid, oid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCityKeywordOrderByQty(cname, kid, oid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCityKeywordOrderByPrice(cname, kid, oid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCityKeywordOrderBySupplyDate(cname, kid, oid, SupplyDate)
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

    def getResourcesByCityCategoryOrder(self, cname, cat_name, oid):
        pass

    def searchResourcesByCityCategoryOrder(self, cname, cat_name, oid, args):
        if not CityDAO().getCityByName(cname) and not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "City, Category, and Order Not Found"), 404
        elif not CityDAO().getCityByName(cname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "City and Category Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not CityDAO().getCityByName(cname):
            return jsonify(Error = "City Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDateQtyPriceSupplyDate(cname, cat_name, oid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDateQtyPrice(cname, cat_name, oid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDateQtySupplyDate(cname, cat_name, oid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDatePriceSupplyDate(cname, cat_name, oid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameQtyPriceSupplyDate(cname, cat_name, oid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDateQtyPriceSupplyDate(cname, cat_name, oid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDateQty(cname, cat_name, oid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDatePrice(cname, cat_name, oid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDateSupplyDate(cname, cat_name, oid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByNameQtyPrice(cname, cat_name, oid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameQtySupplyDate(cname, cat_name, oid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNamePriceSupplyDate(cname, cat_name, oid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDateQtyPrice(cname, cat_name, oid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDateQtySupplyDate(cname, cat_name, oid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDatePriceSupplyDate(cname, cat_name, oid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByQtyPriceSupplyDate(cname, cat_name, oid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameChangedDate(cname, cat_name, oid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByCityCategoryOrderByNameQty(cname, cat_name, oid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByNamePrice(cname, cat_name, oid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByNameSupplyDate(cname, cat_name, oid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDateQty(cname, cat_name, oid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDatePrice(cname, cat_name, oid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDateSupplyDate(cname, cat_name, oid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByQtyPrice(cname, cat_name, oid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByQtySupplyDate(cname, cat_name, oid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderByPriceSupplyDate(cname, cat_name, oid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByCityCategoryOrderByName(cname, cat_name, oid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByCityCategoryOrderByChangedDate(cname, cat_name, oid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByCityCategoryOrderByQty(cname, cat_name, oid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByCityCategoryOrderByPrice(cname, cat_name, oid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByCityCategoryOrderBySupplyDate(cname, cat_name, oid, SupplyDate)
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

    def getResourcesByRegionKeywordCategory(self, rname, kid, cat_name):
        pass

    def searchResourcesByRegionKeywordCategory(self, rname, kid, cat_name, args):
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
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDateQtyPriceSupplyDate(rname, kid, cat_name, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDateQtyPrice(rname, kid, cat_name, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDateQtySupplyDate(rname, kid, cat_name, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDatePriceSupplyDate(rname, kid, cat_name, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameQtyPriceSupplyDate(rname, kid, cat_name, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDateQtyPriceSupplyDate(rname, kid, cat_name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDateQty(rname, kid, cat_name, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDatePrice(rname, kid, cat_name, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDateSupplyDate(rname, kid, cat_name, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameQtyPrice(rname, kid, cat_name, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameQtySupplyDate(rname, kid, cat_name, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNamePriceSupplyDate(rname, kid, cat_name, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDateQtyPrice(rname, kid, cat_name, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDateQtySupplyDate(rname, kid, cat_name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDatePriceSupplyDate(rname, kid, cat_name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByQtyPriceSupplyDate(rname, kid, cat_name, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameChangedDate(rname, kid, cat_name, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameQty(rname, kid, cat_name, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNamePrice(rname, kid, cat_name, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByNameSupplyDate(rname, kid, cat_name, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDateQty(rname, kid, cat_name, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDatePrice(rname, kid, cat_name, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDateSupplyDate(rname, kid, cat_name, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByQtyPrice(rname, kid, cat_name, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByQtySupplyDate(rname, kid, cat_name, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByPriceSupplyDate(rname, kid, cat_name, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByRegionKeywordCategoryByName(rname, kid, cat_name, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryByChangedDate(rname, kid, cat_name, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByRegionKeywordCategoryByQty(rname, kid, cat_name, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByRegionKeywordCategoryByPrice(rname, kid, cat_name, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordCategoryBySupplyDate(rname, kid, cat_name, SupplyDate)
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

    def getResourcesByRegionKeywordOrder(self, rname, kid, oid):
        pass

    def searchResourcesByRegionKeywordOrder(self, rname, kid, oid, args):
        if not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Region, Keyword, and Order Not Found"), 404
        elif not RegionDAO().getRegionByName(rname) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Region and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword and Order Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDateQtyPriceSupplyDate(rname, kid, oid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDateQtyPrice(rname, kid, oid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDateQtySupplyDate(rname, kid, oid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDatePriceSupplyDate(rname, kid, oid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameQtyPriceSupplyDate(rname, kid, oid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDateQtyPriceSupplyDate(rname, kid, oid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDateQty(rname, kid, oid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDatePrice(rname, kid, oid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDateSupplyDate(rname, kid, oid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameQtyPrice(rname, kid, oid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameQtySupplyDate(rname, kid, oid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNamePriceSupplyDate(rname, kid, oid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDateQtyPrice(rname, kid, oid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDateQtySupplyDate(rname, kid, oid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDatePriceSupplyDate(rname, kid, oid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByQtyPriceSupplyDate(rname, kid, oid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameChangedDate(rname, kid, oid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameQty(rname, kid, oid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByNamePrice(rname, kid, oid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByNameSupplyDate(rname, kid, oid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDateQty(rname, kid, oid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDatePrice(rname, kid, oid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDateSupplyDate(rname, kid, oid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByQtyPrice(rname, kid, oid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByQtySupplyDate(rname, kid, oid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByPriceSupplyDate(rname, kid, oid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByRegionKeywordOrderByName(rname, kid, oid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByRegionKeywordOrderByChangedDate(rname, kid, oid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByRegionKeywordOrderByQty(rname, kid, oid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByRegionKeywordOrderByPrice(rname, kid, oid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByRegionKeywordOrderBySupplyDate(rname, kid, oid, SupplyDate)
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

    def getResourcesByRegionCategoryOrder(self, rname, cat_name, oid):
        pass

    def searchResourcesByRegionCategoryOrder(self, rname, cat_name, oid, args):
        if not RegionDAO().getRegionByName(rname) and not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Region, Category, and Order Not Found"), 404
        elif not RegionDAO().getRegionByName(rname) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Region and Category Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not RegionDAO().getRegionByName(rname):
            return jsonify(Error = "Region Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDateQtyPriceSupplyDate(rname, cat_name, oid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDateQtyPrice(rname, cat_name, oid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDateQtySupplyDate(rname, cat_name, oid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDatePriceSupplyDate(rname, cat_name, oid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameQtyPriceSupplyDate(rname, cat_name, oid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDateQtyPriceSupplyDate(rname, cat_name, oid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDateQty(rname, cat_name, oid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDatePrice(rname, cat_name, oid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDateSupplyDate(rname, cat_name, oid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameQtyPrice(rname, cat_name, oid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameQtySupplyDate(rname, cat_name, oid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNamePriceSupplyDate(rname, cat_name, oid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDateQtyPrice(rname, cat_name, oid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDateQtySupplyDate(rname, cat_name, oid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDatePriceSupplyDate(rname, cat_name, oid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByQtyPriceSupplyDate(rname, cat_name, oid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameChangedDate(rname, cat_name, oid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameQty(rname, cat_name, oid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByNamePrice(rname, cat_name, oid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByNameSupplyDate(rname, cat_name, oid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDateQty(rname, cat_name, oid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDatePrice(rname, cat_name, oid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDateSupplyDate(rname, cat_name, oid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByQtyPrice(rname, cat_name, oid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByQtySupplyDate(rname, cat_name, oid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByPriceSupplyDate(rname, cat_name, oid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByRegionCategoryOrderByName(rname, cat_name, oid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByRegionCategoryOrderByChangedDate(rname, cat_name, oid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByRegionCategoryOrderByQty(rname, cat_name, oid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByRegionCategoryOrderByPrice(rname, cat_name, oid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByRegionCategoryOrderBySupplyDate(rname, cat_name, oid, SupplyDate)
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

    def getResourcesBySupplierKeywordCategory(self, sid, kid, cat_name):
        pass

    def searchResourcesBySupplierKeywordCategory(self, sid, kid, cat_name, args):
        if not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Supplier, Keyword, and Category Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Supplier and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDateQtyPriceSupplyDate(sid, kid, cat_name, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDateQtyPrice(sid, kid, cat_name, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDateQtySupplyDate(sid, kid, cat_name, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDatePriceSupplyDate(sid, kid, cat_name, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameQtyPriceSupplyDate(sid, kid, cat_name, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDateQtyPriceSupplyDate(sid, kid, cat_name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDateQty(sid, kid, cat_name, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDatePrice(sid, kid, cat_name, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDateSupplyDate(sid, kid, cat_name, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameQtyPrice(sid, kid, cat_name, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameQtySupplyDate(sid, kid, cat_name, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNamePriceSupplyDate(sid, kid, cat_name, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDateQtyPrice(sid, kid, cat_name, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDateQtySupplyDate(sid, kid, cat_name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDatePriceSupplyDate(sid, kid, cat_name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByQtyPriceSupplyDate(sid, kid, cat_name, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameChangedDate(sid, kid, cat_name, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameQty(sid, kid, cat_name, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNamePrice(sid, kid, cat_name, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByNameSupplyDate(sid, kid, cat_name, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDateQty(sid, kid, cat_name, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDatePrice(sid, kid, cat_name, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDateSupplyDate(sid, kid, cat_name, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByQtyPrice(sid, kid, cat_name, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByQtySupplyDate(sid, kid, cat_name, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByPriceSupplyDate(sid, kid, cat_name, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByName(sid, kid, cat_name, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByChangedDate(sid, kid, cat_name, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByQty(sid, kid, cat_name, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesBySupplierKeywordCategoryByPrice(sid, kid, cat_name, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordCategoryBySupplyDate(sid, kid, cat_name, SupplyDate)
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

    def getResourcesBySupplierKeywordOrder(self, sid, kid, oid):
        pass

    def searchResourcesBySupplierKeywordOrder(self, sid, kid, oid, args):
        if not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Supplier, Keyword, and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid) and not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Supplier and Keyword Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDateQtyPriceSupplyDate(sid, kid, oid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDateQtyPrice(sid, kid, oid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDateQtySupplyDate(sid, kid, oid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDatePriceSupplyDate(sid, kid, oid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameQtyPriceSupplyDate(sid, kid, oid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDateQtyPriceSupplyDate(sid, kid, oid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDateQty(sid, kid, oid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDatePrice(sid, kid, oid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDateSupplyDate(sid, kid, oid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameQtyPrice(sid, kid, oid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameQtySupplyDate(sid, kid, oid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNamePriceSupplyDate(sid, kid, oid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDateQtyPrice(sid, kid, oid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDateQtySupplyDate(sid, kid, oid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDatePriceSupplyDate(sid, kid, oid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByQtyPriceSupplyDate(sid, kid, oid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameChangedDate(sid, kid, oid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameQty(sid, kid, oid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNamePrice(sid, kid, oid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByNameSupplyDate(sid, kid, oid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDateQty(sid, kid, oid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDatePrice(sid, kid, oid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDateSupplyDate(sid, kid, oid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByQtyPrice(sid, kid, oid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByQtySupplyDate(sid, kid, oid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByPriceSupplyDate(sid, kid, oid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesBySupplierKeywordOrderByName(sid, kid, oid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderByChangedDate(sid, kid, oid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesBySupplierKeywordOrderByQty(sid, kid, oid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesBySupplierKeywordOrderByPrice(sid, kid, oid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesBySupplierKeywordOrderBySupplyDate(sid, kid, oid, SupplyDate)
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

    def getResourcesBySupplierCategoryOrder(self, sid, cat_name, oid):
        pass

    def searchResourcesBySupplierCategoryOrder(self, sid, cat_name, oid, args):
        if not SupplierDAO().getSupplierById(sid) and not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Supplier, Category, and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Supplier and Category Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not SupplierDAO().getSupplierById(sid):
            return jsonify(Error = "Supplier Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDateQtyPriceSupplyDate(sid, cat_name, oid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDateQtyPrice(sid, cat_name, oid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDateQtySupplyDate(sid, cat_name, oid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDatePriceSupplyDate(sid, cat_name, oid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameQtyPriceSupplyDate(sid, cat_name, oid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDateQtyPriceSupplyDate(sid, cat_name, oid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDateQty(sid, cat_name, oid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDatePrice(sid, cat_name, oid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDateSupplyDate(sid, cat_name, oid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameQtyPrice(sid, cat_name, oid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameQtySupplyDate(sid, cat_name, oid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNamePriceSupplyDate(sid, cat_name, oid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDateQtyPrice(sid, cat_name, oid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDateQtySupplyDate(sid, cat_name, oid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDatePriceSupplyDate(sid, cat_name, oid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByQtyPriceSupplyDate(sid, cat_name, oid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameChangedDate(sid, cat_name, oid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameQty(sid, cat_name, oid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNamePrice(sid, cat_name, oid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByNameSupplyDate(sid, cat_name, oid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDateQty(sid, cat_name, oid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDatePrice(sid, cat_name, oid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDateSupplyDate(sid, cat_name, oid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByQtyPrice(sid, cat_name, oid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByQtySupplyDate(sid, cat_name, oid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByPriceSupplyDate(sid, cat_name, oid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesBySupplierCategoryOrderByName(sid, cat_name, oid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderByChangedDate(sid, cat_name, oid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesBySupplierCategoryOrderByQty(sid, cat_name, oid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesBySupplierCategoryOrderByPrice(sid, cat_name, oid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesBySupplierCategoryOrderBySupplyDate(sid, cat_name, oid, SupplyDate)
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

    def getResourcesByKeywordCategoryOrder(self, kid, cat_name, oid):
        pass

    def searchResourcesByKeywordCategoryOrder(self, kid, cat_name, oid, args):
        if not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Keyword, Category, and Order Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid) and not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Keyword and Category Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name) and not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Category and Order Not Found"), 404
        elif not KeywordDAO().getKeywordById(kid):
            return jsonify(Error = "Keyword Not Found"), 404
        elif not CategoryDAO().getCategoryByName(cat_name):
            return jsonify(Error = "Category Not Found"), 404
        elif not OrderDAO().getOrderById(oid):
            return jsonify(Error = "Order Not Found"), 404
        else:
            rname = args.get('rname')
            r_changed_date = args.get('r_changed_date')
            rqty = args.get('rqty')
            rprice = args.get('rprice')
            r_supply_date = args.get('r_supply_date')
            dao = ResourceDAO()
            resource_list = []
            if (len(args) == 5) and rname and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDateQtyPriceSupplyDate(kid, cat_name, oid, Name, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDateQtyPrice(kid, cat_name, oid, Name, ChangedDate, Qty, Price)
            elif (len(args) == 4) and rname and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDateQtySupplyDate(kid, cat_name, oid, Name, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 4) and rname and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDatePriceSupplyDate(kid, cat_name, oid, Name, ChangedDate, Price, SupplyDate)
            elif (len(args) == 4) and rname and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameQtyPriceSupplyDate(kid, cat_name, oid, Name, Qty, Price, SupplyDate)
            elif (len(args) == 4) and r_changed_date and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDateQtyPriceSupplyDate(kid, cat_name, oid, ChangedDate, Qty, Price, SupplyDate)
            elif (len(args) == 3) and rname and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDateQty(kid, cat_name, oid, Name, ChangedDate, Qty)
            elif (len(args) == 3) and rname and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDatePrice(kid, cat_name, oid, Name, ChangedDate, Price)
            elif (len(args) == 3) and rname and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDateSupplyDate(kid, cat_name, oid, Name, ChangedDate, SupplyDate)
            elif (len(args) == 3) and rname and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameQtyPrice(kid, cat_name, oid, Name, Qty, Price)
            elif (len(args) == 3) and rname and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameQtySupplyDate(kid, cat_name, oid, Name, Qty, SupplyDate)
            elif (len(args) == 3) and rname and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNamePriceSupplyDate(kid, cat_name, oid, Name, Price, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDateQtyPrice(kid, cat_name, oid, ChangedDate, Qty, Price)
            elif (len(args) == 3) and r_changed_date and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDateQtySupplyDate(kid, cat_name, oid, ChangedDate, Qty, SupplyDate)
            elif (len(args) == 3) and r_changed_date and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDatePriceSupplyDate(kid, cat_name, oid, ChangedDate, Price, SupplyDate)
            elif (len(args) == 3) and rqty and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByQtyPriceSupplyDate(kid, cat_name, oid, Qty, Price, SupplyDate)
            elif (len(args) == 2) and rname and r_changed_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameChangedDate(kid, cat_name, oid, Name, ChangedDate)
            elif (len(args) == 2) and rname and rqty:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameQty(kid, cat_name, oid, Name, Qty)
            elif (len(args) == 2) and rname and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNamePrice(kid, cat_name, oid, Name, Price)
            elif (len(args) == 2) and rname and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByNameSupplyDate(kid, cat_name, oid, Name, SupplyDate)
            elif (len(args) == 2) and r_changed_date and rqty:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDateQty(kid, cat_name, oid, ChangedDate, Qty)
            elif (len(args) == 2) and r_changed_date and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDatePrice(kid, cat_name, oid, ChangedDate, Price)
            elif (len(args) == 2) and r_changed_date and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDateSupplyDate(kid, cat_name, oid, ChangedDate, SupplyDate)
            elif (len(args) == 2) and rqty and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByQtyPrice(kid, cat_name, oid, Qty, Price)
            elif (len(args) == 2) and rqty and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByQtySupplyDate(kid, cat_name, oid, Qty, SupplyDate)
            elif (len(args) == 2) and rprice and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByPriceSupplyDate(kid, cat_name, oid, Price, SupplyDate)
            elif (len(args) == 1) and rname:
                resource_list = dao.getResourcesByKeywordCategoryOrderByName(kid, cat_name, oid, Name)
            elif (len(args) == 1) and r_changed_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderByChangedDate(kid, cat_name, oid, ChangedDate)
            elif (len(args) == 1) and rqty:
                resource_list = dao.getResourcesByKeywordCategoryOrderByQty(kid, cat_name, oid, Qty)
            elif (len(args) == 1) and rprice:
                resource_list = dao.getResourcesByKeywordCategoryOrderByPrice(kid, cat_name, oid, Price)
            elif (len(args) == 1) and r_supply_date:
                resource_list = dao.getResourcesByKeywordCategoryOrderBySupplyDate(kid, cat_name, oid, SupplyDate)
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
